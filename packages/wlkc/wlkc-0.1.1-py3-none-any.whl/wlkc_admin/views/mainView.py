from flask import Blueprint

from wlkc_core import ResHelper
from wlkc_admin.services import router
from wlkc_admin.services.main import LoginService
from wlkc_core.utils.auth import login_handler

mod = Blueprint('main', __name__, url_prefix='/')


@mod.route('/getInfo', methods=['GET'])
@login_handler()
def func1():
    dd = LoginService().getInfo()
    dd = {"permissions": dd.get("permissions"), "roles": dd.get("roles"), "user": dd.get("user")}
    return ResHelper.success(extend=dd)


@mod.route('/getRouters', methods=['GET', 'POST'])
@login_handler()
def func2():
    db_data = router.selectUserMenuTree()
    return ResHelper.success(data=db_data)
