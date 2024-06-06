from typing import Union

from wlkc_core import RedisHelper
from wlkc_admin.modules.sys import Config


def queryAll() -> list[Config]:
    return Config.query.all()


def queryByKey(key: str) -> Union[Config, None]:
    if key:
        return Config.query.filter_by(key=key).first()
    return None


def queryValueByKey(key: str) -> Union[Config, None]:
    config = queryByKey(key)
    if config:
        return config.value
    return None


def loadDictToCache():
    for key in RedisHelper.keys("sys_config:"):
        RedisHelper.expire(key, 0)
    for item in queryAll():
        RedisHelper.set(f"sys_config:{item.key}", item.value, None)
