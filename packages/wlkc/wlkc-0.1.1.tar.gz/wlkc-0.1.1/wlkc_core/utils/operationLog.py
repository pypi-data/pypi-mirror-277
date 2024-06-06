import logging

import time


def LOG(title=None, businessType=None, operatorType="", isSaveRequestData=True, isSaveResponseData=True, excludeParamNames: list = None):
    """

    :param title: 模块
    :param businessType: 功能
    :param operatorType: 操作人类别
    :param isSaveRequestData: 是否保存请求的参数
    :param isSaveResponseData: 是否保存响应的参数
    :param excludeParamNames: 排除指定的请求参数
    :return:
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            operLog = dict(startTime=time.ctime(), success=True)
            try:
                logging.debug("开始记录日志")
                run = func(*args, **kwargs)
                return run
            except Exception as e:
                operLog.update(dict(success=False))
                raise e
            finally:
                operLog.update(dict(endTime=time.ctime()))
                logging.debug("日志记录结束")

        return wrapper

    return decorator
