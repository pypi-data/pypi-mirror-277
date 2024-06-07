import asyncio
from typing import Any, Callable, List, Coroutine

from .logger_ex import LoggerEx


class Collector:
    def __init__(self, result_queue: asyncio.Queue[Any], processing_queue: asyncio.Queue[Any]):
        """
        初始化AsyncResultCollector, 用于收集数据结果、清洗数据、格式化数据等等。

        Args:
            result_queue (asyncio.Queue): 结果队列，存储待处理的结果。
            processing_queue (asyncio.Queue): 处理队列，存储处理后的结果。
        """
        self.result_queue = result_queue
        self.processing_queue = processing_queue
        self.process_functions: List[Callable[[Any], Coroutine[Any, Any, Any]]] = []
        self.logger = LoggerEx(self.__class__.__name__).get_logger()

    def register_process_func(self, func: Callable[[Any], Coroutine[Any, Any, Any]]) -> None:
        """
        注册自定义数据处理函数。

        Args:
            func (Callable[[Any], Coroutine[Any, Any, Any]]): 自定义结果处理函数，接受一个结果参数并返回处理后的结果。

        Returns:
            None
        """
        self.process_functions.append(func)
        self.logger.info(f"Result collect function {func.__name__} is registered.")

    async def _default_process(self, result: Any) -> Any:
        """
        默认处理函数，直接返回结果。

        Args:
            result (Any): 要处理的结果。

        Returns:
            Any: 处理后的结果。
        """
        self.logger.info(f"Collector result with default process")
        return result

    async def collect(self) -> None:
        """
        从结果队列中获取结果，依次调用所有注册的处理函数，并将处理后的结果存储到处理队列。

        Returns:
            None
        """
        while True:
            result = await self.result_queue.get()
            try:
                self.logger.info("Result collecting ...")
                if self.process_functions:
                    for func in self.process_functions:
                        result = await func(result)
                        await self.processing_queue.put(result)
                else:
                    await self.processing_queue.put(await self._default_process(result))
                self.logger.info("Result collecting is complete")
            except Exception as e:
                self.logger.error(f"Failed to process result: {str(e)}")
            finally:
                self.result_queue.task_done()

    def start(self) -> None:
        """
        启动结果收集器，开始收集和处理结果。

        Returns:
            None
        """
        asyncio.create_task(self.collect())
