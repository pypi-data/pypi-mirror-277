import datetime
import logging
import os
from typing import Any

from flask import Flask, request
from flask_apscheduler import APScheduler
from flask_redis import FlaskRedis

from wlkc_core.exceptions import UserException, OtherException
from wlkc_core.utils import ResHelper, iputils, RedisHelper

# 实例化并命名为app实例
app = Flask(__name__)
app.config.from_object(os.getenv("ACTIVE_CONFIGS_FILE", 'wlkc_core.settings'))
redis_client = FlaskRedis(app)

# 配置scheduler
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

# scheduler.add_job(func=your_job_function, id='1', trigger='cron', second='*/5')
timeFormat = "%Y-%m-%d %H:%M:%S.%f"


@app.before_request
def before_request(*args, **kwargs):
    # print("Request URL:", request.url)
    # logging.info("此处用来校验秘钥登录状态")
    # print(request.headers.get('Connection'))
    # session
    kwargs.update({"request": request})
    request.client_ip = iputils.getIpAdd()
    request.environ.setdefault("TTT", datetime.datetime.now().strftime(timeFormat))
    logging.debug("before")
    # if request.path not in app.config.get("STATIC_PATH"):
    #     return ResHelper.not_permission("Request URL用户权限不足")
    # return result(203, {"info": "未登录"})
    # return jsonify({"sdkjfdsf": "sdfdsf"})


@app.after_request
def handle_after_request(response, **kwargs):
    """在每次请求(视图函数处理)之后都被执行, 前提是视图函数没有出现异常"""
    # logging.info("handle_after_request 被执行")
    # logging.debug(f'{request.environ.get("TTT")},{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")}')
    times = datetime.datetime.now() - datetime.datetime.strptime(request.environ.get("TTT"), timeFormat)
    logging.debug(f"after>>{times.microseconds}")

    return response


@app.errorhandler(404)
def not_found(error):
    return ResHelper.page_not_found(f"{request.path}请求地址不存在！")


@app.errorhandler(405)
def not_found(error):
    return ResHelper.page_not_found("请求方式不存在", code=405)


@app.errorhandler(UserException)
def custom_error(error):
    from wlkc_core.database import db_session
    db_session.rollback()
    logging.error(f"操作用户异常：{error.message}")
    return ResHelper.failed(error.message)


@app.errorhandler(OtherException)
def other_error(error):
    from wlkc_core.database import db_session
    db_session.rollback()
    logging.error(f"操作异常：{error.message}")
    return ResHelper.failed(error.message)


@app.errorhandler(Exception)
def custom_error(error):
    from wlkc_core.database import db_session
    db_session.rollback()
    logging.error(error)
    # traceback.format_exc(error)
    return ResHelper.failed("系统异常")


def registryViews(view_list: Any, name="视图模块"):
    """
    注册路由mod信息
    :param view_list: 返回mod列表的方法
    :param name:
    :return:
    """
    for view in view_list():
        logging.debug(f'注册 [{name} - {view.name}]，路径 ： {view.url_prefix}')
        app.register_blueprint(view)
