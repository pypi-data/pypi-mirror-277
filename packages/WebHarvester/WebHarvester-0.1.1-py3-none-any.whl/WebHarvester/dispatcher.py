import asyncio
from typing import List

from .logger_ex import LoggerEx


class Dispatcher:
    def __init__(self, request_queue: asyncio.Queue, spider_queue_list: List[asyncio.Queue]):
        """
        初始化AsyncTaskDispatcher实例。

        Args:
            request_queue (asyncio.Queue): 请求队列。
            spider_queue_list (List[asyncio.Queue]): 爬虫队列列表。
        """
        self.request_queue = request_queue
        self.spider_queue_list = spider_queue_list
        self._logger = LoggerEx(self.__class__.__name__).get_logger()

    async def dispatch(self) -> None:
        """
        将请求队列中的请求分发到各个爬虫队列中。

        Returns:
            None
        """
        spider_count = len(self.spider_queue_list)
        index = 0
        while True:
            request = await self.request_queue.get()
            await self.spider_queue_list[index].put(request)
            self._logger.info(f"Request dispatched to spider queue {index}: {request}")
            index = (index + 1) % spider_count
            self.request_queue.task_done()

    def add_spider_queue(self, spider_queue: asyncio.Queue) -> None:
        """
        动态添加一个新的爬虫队列。

        Args:
            spider_queue (asyncio.Queue): 要添加的新的爬虫队列。

        Returns:
            None
        """
        self.spider_queue_list.append(spider_queue)
        self._logger.info(f"New spider queue added. Total queues: {len(self.spider_queue_list)}")

    def start(self) -> None:
        """
        启动任务分发器，开始分发任务。

        Returns:
            None
        """
        asyncio.create_task(self.dispatch())
