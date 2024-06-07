import logging

from . import settings


class LoggerEx:
    def __init__(self, name: str = "LoggerEx", level: str = settings.LOG_LEVEL):
        """
        初始化CustomLogger实例。

        Args:
            name (str): 日志记录器的名称。
            level (str): 日志记录级别。
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(getattr(logging, level.upper()))

        # 创建控制台处理器并设置级别
        ch = logging.StreamHandler()
        ch.setLevel(getattr(logging, level.upper()))

        # 创建格式化器
        formatter = logging.Formatter('%(asctime)s - [%(module)s/%(funcName)s] - %(levelname)s - %(message)s')

        # 将格式化器添加到处理器
        ch.setFormatter(formatter)

        # 将处理器添加到记录器
        if not self.logger.handlers:
            self.logger.addHandler(ch)

    def get_logger(self):
        """
        获取配置好的日志记录器。

        Returns:
            logging.Logger: 配置好的日志记录器。
        """
        return self.logger
