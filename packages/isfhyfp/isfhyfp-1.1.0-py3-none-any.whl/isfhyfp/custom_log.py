# -*- coding: utf-8 -*-
# @Author  : isFhy
# @Email   : fhy.sdwh@gmail.com
# @File    : custom_log.py
# @Time    : 2023/10/16 15:45
# **********************************************

"""
项目日志功能模块
"""

import logging
from logging import handlers

LOG_FILE_FMT = '[%(asctime)s][%(funcName)s:%(lineno)d][%(levelname)s] : %(message)s'  # 文件日志格式
LOG_CONSOLE_FMT = '[%(asctime)s] %(message)s'  # 控制台日志格式
LOG_DATEFMT = '%Y-%m-%d %H:%M:%S'  # 日期格式
LOG_LEVEL = logging.DEBUG  # 日志级别
LOG_CONSOLE_LEVEL = logging.INFO  # 日志级别
LOG_FILE_LEVEL = logging.DEBUG  # 日志级别


class CustomLog:
    def __init__(self, log_name, file_name):
        """

        :param log_name: 日志别名
        :param file_name: 日志保存的绝对路径
        """
        # 创建日志记录器
        self._logger = logging.getLogger(log_name)
        self._logger.setLevel(LOG_LEVEL)
        # 设置日志格式
        self.file_formatter = logging.Formatter(fmt=LOG_FILE_FMT, datefmt=LOG_DATEFMT)
        self.console_formatter = logging.Formatter(fmt=LOG_CONSOLE_FMT, datefmt=LOG_DATEFMT)
        # 日志控制台输出
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(self.console_formatter)
        console_handler.setLevel(LOG_CONSOLE_LEVEL)
        # 日志文件输出
        file_handler = handlers.RotatingFileHandler(
            # filename=os.path.join(BASE_DIR, LOG_DIR, file_name),
            filename=file_name,
            maxBytes=548576,
            backupCount=10,
            encoding='utf-8'
        )
        file_handler.setFormatter(self.file_formatter)
        file_handler.setLevel(LOG_FILE_LEVEL)
        # 将控制台输出和文件输出添加到日志记录器
        self._logger.addHandler(console_handler)
        self._logger.addHandler(file_handler)

    @property
    def logger(self):
        return self._logger
