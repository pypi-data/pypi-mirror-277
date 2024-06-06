import inspect
import json
import logging
import traceback

from flask import request

from wlkc_core import app
from wlkc_core.utils import RedisHelper, SessionHelper, ResHelper


def checkLogin(token):
    def update_ttl(key):
        if RedisHelper.ttl(key) < 30 * 60:
            RedisHelper.expire(key, 30 * 60)

    msg = None
    try:
        result = SessionHelper.decode_token(token).get("login_user_key")
        # 判断登录信息正确性
        if result:
            key = f"{app.config.get('LOGIN_TOKEN_PREFIX')}{result}"
            request.token_key = key
            # 登录信息正确，正常调用接口
            if RedisHelper.exists(key):
                update_ttl(key)
                return True, json.loads(RedisHelper.get_str(key).replace("L", "").replace(":Set", ":"))
            # 判断权限是否正确
            return False, "会话已过期"
    except:
        logging.error(traceback.format_exc())
        msg = "登录信息错误"
    return False, msg


def login_handler():
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                # RedisHelper.get_json("sys_dict:launch_channel")
                # 从redis获取权限信息，无权限则返回错误
                token = request.headers.get('Authorization')
                if not token:
                    return ResHelper.failed("Token参数不存在")
                check, data = checkLogin(token)
                if check is True:
                    request.user_id = data.get('user').get('userId')
                    request.user_name = data.get('user').get('userName')
                    request.token = token
                    if [item for item in inspect.signature(func).parameters.keys()].count("kwargs") > 0 and func.__name__ == "permission":
                        kwargs.update({"userName": data.get('user').get("userName"), "permissions": data.get("permissions")})
                    return func(*args, **kwargs)
                else:
                    return ResHelper.failed(data, code=401)
            except Exception as e:
                logging.error(traceback.format_exc())
                raise e

        # Renaming the function name:
        wrapper.__name__ = func.__name__
        return wrapper

    return decorator


def hasPermission(permissions):
    """判断功能权限"""

    def decorator(func):
        @login_handler()
        def permission(*args, **kwargs):
            if not app.config.get('AUTH_CHECK'):
                return func(*args, **kwargs)

            hasPermission = False
            if kwargs.get("permissions").count("*:*:*") or kwargs.get("permissions").count(permissions) > 0:
                hasPermission = True

            del kwargs["permissions"]
            del kwargs["userName"]
            if not hasPermission:
                return ResHelper.not_permission("您没有当前页面相关权限，请联系管理员")
            # if [item for item in inspect.signature(func).parameters.keys()].count("kwargs") == 0:
            #     kwargs.update({})
            # print("用户权限")
            return func(*args, **kwargs)

        permission.__name__ = func.__name__
        return permission

    return decorator
