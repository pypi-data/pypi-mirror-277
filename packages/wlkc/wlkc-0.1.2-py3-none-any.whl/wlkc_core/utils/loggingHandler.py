import logging
import os
from logging.handlers import TimedRotatingFileHandler

import time

from wlkc_core.utils import iputils


# 自定义日志处理程序
class CustomFormatter(logging.Formatter):
    def format(self, record):
        # 如果日志记录包含请求上下文
        ip = iputils.getIpAdd()
        if ip:
            record.msg = f"[{ip}] {record.msg}"
        return super().format(record)


class TimeLoggerRolloverHandler(TimedRotatingFileHandler):
    """
    日志输出，默认为按天输出
    """

    def __init__(self, filename, when='midnight', interval=1, backupCount=10, encoding='utf-8', delay=False, utc=False, atTime=None):
        super(TimeLoggerRolloverHandler, self).__init__(filename, when, interval, backupCount, encoding, delay, utc)

    def doRollover(self):
        """
        """
        if self.stream:
            self.stream.close()
            # self.stream.
        currentTime = int(time.time())
        dstNow = time.localtime(currentTime)[-1]
        t = self.rolloverAt - self.interval
        if self.utc:
            timeTuple = time.gmtime(t)
        else:
            timeTuple = time.localtime(t)
            dstThen = timeTuple[-1]
            if dstNow != dstThen:
                if dstNow:
                    addend = 3600
                else:
                    addend = -3600
                timeTuple = time.localtime(t + addend)
        # log_type = 'info' if self.level == 20 else 'error'
        # dfn = f"my.{datetime.datetime.now().strftime('%Y%m%d')}.{log_type}.log"
        dfn = self.baseFilename.replace(".log", ".{}.log".format(time.strftime(self.suffix, timeTuple)))
        if os.path.exists(dfn):
            os.remove(dfn)
        self.rotate(self.baseFilename, dfn)
        # self.baseFilename = dfn
        if not self.delay:
            self.stream = self._open()
        newRolloverAt = self.computeRollover(currentTime)
        while newRolloverAt <= currentTime:
            newRolloverAt = newRolloverAt + self.interval
        if (self.when == 'MIDNIGHT' or self.when.startswith('W')) and not self.utc:
            dstAtRollover = time.localtime(newRolloverAt)[-1]
            if dstNow != dstAtRollover:
                if not dstNow:
                    addend = -3600
                else:
                    addend = 3600
                newRolloverAt += addend
        self.rolloverAt = newRolloverAt
