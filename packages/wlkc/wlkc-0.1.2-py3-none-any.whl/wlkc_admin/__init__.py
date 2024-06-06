import logging
from datetime import datetime

from wlkc_core import scheduler, app


def initAdminView():
    """
    初始化视图
    :return:
    """
    from wlkc_admin.views import home, mainView, userView, dictView, configView, roleView, menuView
    logging.debug('加载后台管理接口')
    app.register_blueprint(home.mod)
    app.register_blueprint(mainView.mod)
    app.register_blueprint(userView.mod)
    app.register_blueprint(dictView.mod)
    app.register_blueprint(configView.mod)
    app.register_blueprint(roleView.mod)
    app.register_blueprint(menuView.mod)
    logging.debug('加载后台管理接口完成！')


def adminViews():
    """
    返回视图列表
    :return:
    """
    from wlkc_admin.views import home, mainView, userView, dictView, configView, roleView, menuView
    return [home.mod, mainView.mod, userView.mod, dictView.mod, configView.mod, roleView.mod, menuView.mod]


@scheduler.scheduler.scheduled_job(trigger='date', run_date=datetime.now(), id='cache_load')
def initCache():
    logging.debug("基础数据写入缓存。")
    try:
        from wlkc_admin.services import sysConfig, sysDict
        sysConfig.loadDictToCache()
        sysDict.loadDictToCache()
    except:
        pass
    logging.debug("缓存写入完成。")
