from flask import Blueprint

from wlkc_core import ResHelper
from wlkc_admin.services import sysMenu
from wlkc_core.utils.auth import login_handler

mod = Blueprint('menuView', __name__, url_prefix='/system/menu')


@mod.route('/treeselect')
@login_handler()
def treeSelect():
    menus = sysMenu.selectMenuTree()
    return ResHelper.success(data=menus)


@mod.route('/roleMenuTreeselect/<role_id>')
@login_handler()
def roleMenuTreeSelect(role_id):
    data = {"menus": sysMenu.selectMenuTree(), "checkedKeys": sysMenu.selectMenuListByRoleId(role_id)}
    return ResHelper.success(extend=data)
