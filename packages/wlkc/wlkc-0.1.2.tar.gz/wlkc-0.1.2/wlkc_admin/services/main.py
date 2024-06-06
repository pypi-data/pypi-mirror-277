import base64
import json
import logging
import traceback
from datetime import datetime
from io import BytesIO

import bcrypt
from cuid import cuid
from flask import request
from sqlalchemy import and_

from wlkc_admin.services import BaseService, permission
from wlkc_core import redis_client, UserException, app
from wlkc_core.cache_modules import LoginUser
from wlkc_core.utils import RedisHelper, iputils, SessionHelper, JWTAuthorize
from wlkc_core.utils.imgCode import generate_code


class VCodeService(BaseService):
    @staticmethod
    def make():
        uid = str(cuid())
        # 生成验证码
        code, image = generate_code()
        # 将图像保存到字节流中
        image_stream = BytesIO()
        image.save(image_stream, 'PNG')
        logging.debug(f"验证码：{code}; ID:{uid}")
        b64img = (base64.b64encode(image_stream.getvalue()).decode('utf-8'))
        RedisHelper.set(f"{app.config.get('CAPTCHA_IMAGE_PREFIX')}{uid}", code)
        return {"img": b64img, "uuid": uid, "captchaEnabled": RedisHelper.get_str('sys_config:sys.account.captchaEnabled') == 'true'}


class LoginService(BaseService):
    from wlkc_admin.modules.sys import User

    def __init__(self):
        super().__init__()
        self.exclude = ["create_by", "create_time", "update_time", "update_by", "password"]
        self.token_prefix = app.config.get('LOGIN_TOKEN_PREFIX')

    def login(self, loginData):
        # 验证码校验
        if self.checkAuthCode(loginData):
            self.checkBlackIp()

            # 登录前置校验，校验密码
            user = self.loadUser(loginData)
            if user:
                # 生成新的会话ID
                login_id = self.cuid_gen(user)
                token = JWTAuthorize().encode({"login_user_key": login_id})
                # 用户权限配置 login_tokens:
                userDetail = LoginUser(user=user, permissions=permission.getMenuPermission(user))
                self.setUserAgent(userDetail)
                # 过期时间设置
                self.refreshToken(userDetail, login_id)
                return True, token
        return False, None

    def getLoginData(self, token_key):
        cache_key = f"{self.token_prefix}{token_key}"
        if RedisHelper.exists(cache_key):
            return json.loads(RedisHelper.get_str(cache_key))
        return None

    @staticmethod
    def setUserAgent(userDetail):
        try:
            # TODO 待优化浏览器头部信息
            userAgent = request.environ.get("HTTP_USER_AGENT")
            ip = iputils.getIpAdd()
            login_time = int(datetime.now().timestamp() * 1000)
            expTime = request.json.get("expTime")
            expTime = int(expTime) if type(expTime) == int else 30
            expTime = expTime * 60 if expTime in [30, 120, 720, 1440, 2880] else 30 * 60
            userDetail.setLoginInfo(loginTime=login_time, expireTime=expTime, ipaddr=ip, loginLocation="", browser="", os="")
        except Exception as e:
            logging.error(traceback.format_exc())
            raise e

    def checkBlackIp(self):
        """拉取IP黑名单"""
        blackList = self.redisClient.get_str("sys_config:sys.login.blackIPList")
        if iputils.isMatchedIp(blackList, iputils.getIpAdd()):
            raise UserException(4, "很遗憾，访问IP已被列入系统黑名单")

    @staticmethod
    def checkAuthCode(loginData):
        """校验验证码信息"""
        try:
            access = True
            if loginData.get("code"):
                code = redis_client.get(f"{app.config.get('CAPTCHA_IMAGE_PREFIX')}{loginData.get('uuid')}")
                if not code or code.decode("utf-8") != loginData.get('code'):
                    raise UserException(3, "验证码错误")
                access = (code.decode("utf-8") == loginData.get('code'))
            return access
        finally:
            # redis_client.delete(f"{app.config.get('CAPTCHA_IMAGE_PREFIX')}{loginData.get('uuid')}")
            pass

    def loadUser(self, loginData) -> dict:
        from wlkc_admin.modules.sys import User
        if loginData.get("username") and loginData.get("password"):
            user = User.query.filter(and_(User.user_name == loginData.get("username"), User.del_flag == 0)).first()
            if user is None:
                raise UserException(1, f"{loginData.get('username')} 用户名或者密码错误")
            elif user.status == 1:
                raise UserException(1, f"{loginData.get('username')} 用户已停用")
            # 用户密码校验
            if not self.validatePasswd(loginData, user):
                raise UserException(2, f'用户名或者密码错误')
            user = self.loadUserRoles(user.to_json(exclude=self.exclude))
            return user
        raise UserException(3, "用户名或者密码不能为空")

    @staticmethod
    def validatePasswd(loginData, user: User) -> bool:

        """校验密码"""
        return bcrypt.checkpw(loginData.get("password").encode("utf-8"), user.password.encode("utf-8"))

    def cuid_gen(self, user: dict):
        cuid_obj = cuid()
        return cuid_obj

    def refreshToken(self, userDetail, login_id: str):
        try:
            expTime = userDetail.expireTime
            RedisHelper.set(f"{self.token_prefix}{login_id}", json.dumps(userDetail.to_json(), ensure_ascii=False), expTime)
        except:
            logging.error(traceback.format_exc())

    def loadUserRoles(self, user: dict) -> dict:
        from wlkc_admin.modules.sys import UserRole, Role
        userRole = UserRole.query.filter(and_(UserRole.user_id == user.get("userId"))).all()
        userRoles = []
        if userRole:
            role_ids = [item.role_id for item in userRole]
            roles = Role.query.filter(Role.role_id.in_(role_ids)).all()
            userRoles = [item.to_json(exclude=self.exclude) for item in roles]
        user.update({"roles": userRoles})
        return user

    @staticmethod
    def logout():
        """登出，根据头部的认证信息，删除Redis中的登录信息"""
        token_key = SessionHelper.get_token_key()
        if token_key:
            token_key = f"login_tokens:{token_key}"
            RedisHelper.expire(token_key, 1)

    @staticmethod
    def getInfo():
        return SessionHelper.get_token_info()


class BaseInfo(BaseService):

    @staticmethod
    def query_info():
        """返回网站基础信息，包含 标题，ICP，copyRight，过期时间"""
        key = "sys_config:"
        base = (dict(title=RedisHelper.get_str(f"{key}sys.title", "管理平台"), icp=RedisHelper.get_str(f"{key}sys.icp"),
                     copyright=RedisHelper.get_str(f"{key}sys.copyright"), cookieExp=RedisHelper.get_str(f"{key}sys.cookie.exptime", 'false')))
        return base
