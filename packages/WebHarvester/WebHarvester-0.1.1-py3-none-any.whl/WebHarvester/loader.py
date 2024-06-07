import asyncio
from typing import List

from .counter import Counter
from .logger_ex import LoggerEx


class Loader:
    def __init__(self, url_list: List[str], concurrency_limit: int = 10):
        """
        初始化AsyncRequestLoader实例。

        Args:
            url_list (List[str]): 要加载的URL列表。
            concurrency_limit (int): 并发限制，控制一次性加载的最大请求数。
        """
        self.url_list = url_list
        self.concurrency_limit = concurrency_limit
        self.task_counter = Counter()
        self._logger = LoggerEx(self.__class__.__name__).get_logger()

    async def load_requests(self, queue: asyncio.Queue) -> None:
        """
        将URL列表中的URL装载到请求队列中。

        Args:
            queue (asyncio.Queue): 请求队列。

        Returns:
            None
        """
        semaphore = asyncio.Semaphore(self.concurrency_limit)

        async def put_request(url: str) -> None:
            async with semaphore:
                await queue.put(url)
                await self.task_counter.increment_total()
                self._logger.info(f"URL added to queue: {url}")

        await asyncio.gather(*(put_request(url) for url in self.url_list))

    async def add_url(self, queue: asyncio.Queue, url: str) -> None:
        """
        动态添加单个URL到请求队列中。

        Args:
            queue (asyncio.Queue): 请求队列。
            url (str): 要添加的URL。

        Returns:
            None
        """
        await queue.put(url)
        self._logger.info(f"URL added to queue dynamically: {url}")
