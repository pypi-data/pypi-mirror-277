import logging
from logging import Logger
from .path_helper import ensurePathExist


def createLogger(path: str) -> Logger:
    # 创建一个日志记录器
    logger = logging.getLogger(__name__)

    # 设置全局日志级别（可选）
    logger.setLevel(logging.DEBUG)

    # 创建一个控制台处理程序
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)  # 设置控制台日志级别

    # 创建一个文件处理程序
    ensurePathExist(path)
    file_handler = logging.FileHandler(path)
    file_handler.setLevel(logging.DEBUG)  # 设置文件日志级别

    # 创建日志格式
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # 将处理程序添加到日志记录器
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger


__all__ = ["loggerHelper"]
