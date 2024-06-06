import json
import traceback

from flask import Response, request

from wlkc_core.utils.jwt import JWTAuthorize


class ResHelper:
    """基础返回"""
    JSON = "application/json;chart-set=utf-8"

    @staticmethod
    def page_not_found(message, code=404, status=404):
        return ResHelper.success(code=code, message=message, status=status)

    @staticmethod
    def not_permission(message, code=403, status=403):
        return ResHelper.success(code=code, message=message, status=status)

    @staticmethod
    def failed(message, code=1, status=200):
        """返回失败信息"""
        return ResHelper.success(code=code, message=message, status=status)

    @staticmethod
    def success(message="success", code=200, data=None, extend=None, status=200):
        result = {'code': code, 'msg': message}
        if data is not None:
            result.update({'data': data})
        if extend and type(extend) is dict:
            result.update(extend)
        return Response(json.dumps(result, ensure_ascii=False), mimetype=ResHelper.JSON), status

    @staticmethod
    def json_message(message, status=200):
        return Response(json.dumps(message, ensure_ascii=False), mimetype=ResHelper.JSON), status


class RedisHelper:
    @staticmethod
    def get_json(key, default=None):
        import re
        channel = RedisHelper.get_bytes(key)
        if channel:
            try:
                channel = re.sub(r"(\d+)L", r"\1", re.sub(r'"@[^\"]+":"[^\"]+"', "", channel.decode("utf-8") if channel else '{}')).replace('{,', '{')
                channel = json.loads(channel)
            except:
                print(traceback.format_exc())
                pass
        return channel if channel else default

    @staticmethod
    def get_str(key, default=""):
        channel = RedisHelper.get_bytes(key)
        return channel.decode("utf-8") if channel else default

    @staticmethod
    def get_bytes(key, default=None):
        from wlkc_core import redis_client
        channel = redis_client.get(key)
        return channel if channel else default

    @staticmethod
    def set(key, value, expire=3600):
        from wlkc_core import redis_client
        redis_client.set(key, value, ex=expire)

    @classmethod
    def exists(cls, key):
        from wlkc_core import redis_client
        return redis_client.exists(key)

    @classmethod
    def ttl(cls, key):
        from wlkc_core import redis_client
        return redis_client.ttl(key)

    @classmethod
    def expire(cls, key, exp):
        from wlkc_core import redis_client
        redis_client.expire(key, exp)

    @staticmethod
    def keys(key):
        from wlkc_core import redis_client
        return [item.decode("utf-8") for item in redis_client.keys("{}*".format(key))]


class SessionHelper(object):
    @staticmethod
    def get_token_key():
        token = request.headers.get('Authorization')
        if token:
            return SessionHelper.decode_token(token).get("login_user_key")
        return None

    @staticmethod
    def get_token_info():
        t_key = f"login_tokens:{SessionHelper.get_token_key()}"
        if RedisHelper.exists(t_key):
            token_data = RedisHelper.get_str(t_key)
            return json.loads(token_data) if token_data else None
        return {}

    @staticmethod
    def decode_token(token):
        return JWTAuthorize().decode(str(token).replace("Bearer ", ""))

    @staticmethod
    def userId():
        loginDetail = SessionHelper.get_token_info()
        if loginDetail and loginDetail != {}:
            return loginDetail.get("user").get("userId")
        return None

    @staticmethod
    def userName():
        loginDetail = SessionHelper.get_token_info()
        if loginDetail and loginDetail != {}:
            return loginDetail.get("user").get("userName")
        return None

    @staticmethod
    def isAdminUser():
        userId = SessionHelper.userId()
        return userId and 1 == userId

    @staticmethod
    def isAdminRole(role_id):
        return role_id and 1 == role_id
