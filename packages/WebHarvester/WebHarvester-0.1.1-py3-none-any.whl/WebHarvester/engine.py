import asyncio
from typing import List, Callable, Any

from . import settings
from .collector import Collector
from .dispatcher import Dispatcher
from .loader import Loader
from .processor import Processor
from .request import Request
from .spider import Spider
from .logger_ex import LoggerEx
from .counter import Counter


class MainEngine:
    def __init__(self, url_list: List[str] = settings.URL_LIST, num_spiders: int = settings.NUM_SPIDERS,
                 retries: int = settings.RETRIES):
        """
        初始化MainEngine实例。

        Args:
            url_list (List[str]): 要爬取的URL列表。
            num_spiders (int): 爬虫的数量。默认值为settings.NUM_SPIDERS。
            retries (int): 请求失败后的重试次数。默认值为settings.RETRIES。
        """
        self.url_list = url_list
        self.num_spiders = num_spiders
        self.retries = retries

        self.request_queue = asyncio.Queue()
        self.spider_queue_list = [asyncio.Queue() for _ in range(num_spiders)]
        self.result_queue = asyncio.Queue()
        self.processing_queue = asyncio.Queue()
        self.task_counter = Counter()

        self.request = Request(retries)
        self.request_loader = Loader(url_list)
        self.task_dispatcher = Dispatcher(self.request_queue, self.spider_queue_list)
        self.spider_processors = [
            Spider(spider_queue, self.result_queue)
            for spider_queue in self.spider_queue_list
        ]
        self.result_collector = Collector(self.result_queue, self.processing_queue)
        self.result_processor = Processor(self.processing_queue)
        self.logger = LoggerEx(self.__class__.__name__).get_logger()

    def register_spider_process(self, process_func: Callable[..., Any]) -> None:
        """
        注册自定义爬虫处理函数到所有的爬虫处理器中。

        Args:
            process_func (Callable[[str, Any, Any], Any]): 自定义的爬虫处理函数。

        Returns:
            None
        """
        for spider_processor in self.spider_processors:
            spider_processor.register_process_func(process_func)

    def register_result_process(self, process_func: Callable[..., Any]) -> None:
        """
        注册自定义爬虫处理函数到所有的爬虫处理器中。

        Args:
            process_func (Callable[[str, Any, Any], Any]): 自定义的爬虫处理函数。

        Returns:
            None
        """
        self.result_processor.register_process_func(process_func)

    async def run(self):
        """
        启动主引擎，运行爬虫任务。

        Returns:
            None
        """
        self.logger.info("Loading requests into request queue")
        await self.request_loader.load_requests(self.request_queue)
        self.logger.info("Starting TaskDispatcher ...")
        dispatcher_task = asyncio.create_task(self.task_dispatcher.dispatch())
        self.logger.info("Starting SpiderProcessors ...")
        spider_tasks = [asyncio.create_task(spider_processor.process()) for spider_processor in self.spider_processors]
        self.logger.info("Starting ResultCollector ...")
        collector_task = asyncio.create_task(self.result_collector.collect())
        self.logger.info("Starting ResultProcessor ...")
        processor_task = asyncio.create_task(self.result_processor.process())

        self.logger.info("MainEngine is Running ...")
        await self.request_queue.join()
        for spider_queue in self.spider_queue_list:
            await spider_queue.join()
        await self.result_queue.join()
        await self.processing_queue.join()

        dispatcher_task.cancel()
        for task in spider_tasks:
            task.cancel()
        collector_task.cancel()
        processor_task.cancel()

        self.logger.info(f"Task Summary: {self.task_counter.get_summary()}")
        self.logger.info("MainEngine stopped.")

# if __name__ == "__main__":
#     engine = MainEngine(["https://httpbin.org/get", "https://httpbin.org/"])
#     asyncio.run(engine.run())
