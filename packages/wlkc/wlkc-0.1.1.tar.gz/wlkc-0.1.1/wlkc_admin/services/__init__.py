import re

from wlkc_core.utils import RedisHelper


class BaseService(object):
    def __init__(self):
        self.redisClient = RedisHelper

    @staticmethod
    def to_snake_case(x):
        """转下划线命名"""
        return re.sub('(?<=[a-z])[A-Z]|(?<!^)[A-Z](?=[a-z])', '_\g<0>', x).lower()

    @staticmethod
    def to_camel_case(x):
        """转小驼峰法命名"""
        s = re.sub('_([a-zA-Z])', lambda m: (m.group(1).upper()), x)
        return s[0].lower() + s[1:]

    @staticmethod
    def isAdmin(user_id):
        return user_id and 1 == user_id
