from flask import Blueprint, request

from wlkc_core import app
from wlkc_admin.services.main import LoginService
from wlkc_core.utils import ResHelper
from wlkc_core.utils import iputils

mod = Blueprint('home', __name__, url_prefix='/')


@mod.route("/login", methods=['POST'])
def login(*args, **kwargs):
    """登录"""
    from wlkc_admin.services.main import LoginService
    success, token = LoginService().login(request.json)
    return ResHelper.success(extend={app.config.get("TOKEN"): token})


@mod.route("/logout", methods=['POST'])
def logout():
    """退出"""
    LoginService.logout()
    return ResHelper.success()


@mod.route("/captchaImage")
def captcha():
    """生成图形验证码"""
    from wlkc_admin.services.main import VCodeService
    iputils.getIpAdd()
    return ResHelper.json_message(VCodeService.make())


@mod.route("/baseInfo", methods=['GET'])
def baseInfo():
    """获取基础信息，包含标题，ICP，备案信息"""
    from wlkc_admin.services.main import BaseInfo
    return ResHelper.success(extend=BaseInfo.query_info())
