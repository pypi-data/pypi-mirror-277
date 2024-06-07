import asyncio
from typing import Any, Callable, List, Dict

from .logger_ex import LoggerEx
from .request import Request


class Spider:
    def __init__(self, spider_queue: asyncio.Queue, result_queue: asyncio.Queue):
        """
        初始化AsyncSpiderProcessor实例。

        Args:
            spider_queue (asyncio.Queue): 爬虫队列，存储待处理的URL。
            result_queue (asyncio.Queue): 结果队列，存储处理后的结果。
        """
        self.spider_queue = spider_queue
        self.result_queue = result_queue
        self.process_spiders: List[Callable[[str, Any, Any], Any]] = []
        self.logger = LoggerEx(self.__class__.__name__).get_logger()

    def register_process_func(self, func: Callable[..., Any]) -> None:
        """
        注册自定义爬虫处理函数。

        Args:
            func (Callable[[str, *args, **kwargs], Any]): 自定义爬虫处理函数，接受一个URL参数和可变参数，并返回一个异步迭代器。

        Returns:
            None
        """
        self.process_spiders.append(func)
        self.logger.info(f"Spider process function {func.__name__} registered.")

    async def _default_process(self, url: str) -> Dict[str, Any]:
        """
        默认处理函数，发送GET请求并返回响应的文本内容。

        Args:
            url (str): 要处理的URL。

        Returns:
            Dict[str, Any]: 包含响应文本内容的字典。
        """
        self.logger.info(f"Processed URL: {url} with default process")
        async with Request() as request:
            response = await request.get(url)
            return await response.text()

    async def process(self, *args: Any, **kwargs: Any) -> None:
        """
        从爬虫队列中获取URL，依次调用所有注册的处理函数，并将结果存储到结果队列。

        Args:
            *args: 传递给处理函数的可变参数。
            **kwargs: 传递给处理函数的关键字参数。

        Returns:
            None
        """
        while True:
            url = await self.spider_queue.get()
            try:
                self.logger.info(f"Processing URL: {url}")
                if self.process_spiders:
                    for process_spider in self.process_spiders:
                        async for result in process_spider(url, *args, **kwargs):
                            await self.result_queue.put(result)
                        self.logger.info(f"Processed URL: {url} with function {process_spider.__name__}")
                else:
                    await self.result_queue.put(await self._default_process(url))
            except Exception as e:
                self.logger.error(f"Failed to process URL: {url} with error: {str(e)}")
            finally:
                self.spider_queue.task_done()

    def start(self, *args: Any, **kwargs: Any) -> None:
        """
        启动爬虫处理器，开始处理任务。

        Args:
            *args: 传递给处理函数的可变参数。
            **kwargs: 传递给处理函数的关键字参数。

        Returns:
            None
        """
        asyncio.create_task(self.process(*args, **kwargs))
