import asyncio
from typing import Any, Callable, List, Coroutine

from .logger_ex import LoggerEx
from .counter import Counter


class Processor:
    def __init__(self, processing_queue: asyncio.Queue):
        """
        初始化AsyncResultProcessor实例。

        Args:
            processing_queue (asyncio.Queue): 处理队列，存储待处理的结果。
        """
        self.processing_queue = processing_queue
        self.process_functions: List[Callable[[Any], Coroutine[Any, Any, None]]] = []
        self.logger = LoggerEx(self.__class__.__name__).get_logger()
        self.task_counter = Counter()

    def register_process_func(self, func: Callable[[Any], Coroutine[Any, Any, None]]) -> None:
        """
        注册自定义结果处理函数。

        Args:
            func (Callable[[Any], Coroutine[Any, Any, None]]): 自定义结果处理函数，接受一个结果参数并返回处理后的结果。

        Returns:
            None
        """
        self.process_functions.append(func)
        self.logger.info(f"Result process function {func.__name__} is registered.")

    async def _default_process(self, result: Any) -> None:
        """
        默认处理函数，直接打印结果。

        Args:
            result (Any): 要处理的结果。

        Returns:
            None
        """
        try:
            print(result)
            with open('results.txt', 'a', encoding='utf-8') as f:
                f.write(f"{result}\n")
            self.logger.info(
                f"{self.task_counter.get_completed_tasks()}/{self.task_counter.get_total_tasks()}\t"
                f"Result saved to {'results.txt'}"
            )
        except Exception as e:
            self.logger.error(f"Failed to save result to {'results.txt'}: {str(e)}")

    async def process(self) -> None:
        """
        从处理队列中获取结果，依次调用所有注册的处理函数，处理结果。

        Returns:
            None
        """
        while True:
            result = await self.processing_queue.get()
            try:
                self.logger.info("Result processing ...")
                if self.process_functions:
                    for func in self.process_functions:
                        await func(result)
                else:
                    await self._default_process(result)
                self.logger.info("Result processing is complete")
            except TypeError:
                self.logger.error(f"Result function should be asynchronous. like async def xxx()")
            except Exception as e:
                self.logger.error(f"Failed to process result: {str(e)}")
            finally:
                self.processing_queue.task_done()

    def start(self) -> None:
        """
        启动结果处理器，开始处理结果。

        Returns:
            None
        """
        asyncio.create_task(self.process())
