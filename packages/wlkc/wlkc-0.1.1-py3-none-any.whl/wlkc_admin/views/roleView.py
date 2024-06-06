from flask import Blueprint, request

from wlkc_core import ResHelper
from wlkc_core.modules import Page
from wlkc_admin.modules.sys import Role
from wlkc_admin.services import sysRole, sysUser
from wlkc_core.utils.auth import hasPermission

mod = Blueprint('roleView', __name__, url_prefix='/system/role')


@mod.route('/list')
@hasPermission("system:role:list")
def list():
    params = request.values
    role = sysRole.Role(**params)
    page = sysRole.Page(int(params.get("pageNum")), int(params.get("pageSize")))

    data, total = sysRole.selectRoleList(role, page)
    return ResHelper.success(extend=dict(rows=[item.to_json() for item in data], total=total))


@mod.route('/changeStatus', methods=['PUT'])
@hasPermission("system:role:edit")
def changeStatus():
    data = request.json
    role = Role(role_id=data.get("roleId"), status=data.get("status"))
    update_count = sysRole.updateStatus(role)
    return ResHelper.success() if update_count > 0 else ResHelper.failed("更新异常")


@mod.route('/<role_ids>', methods=['DELETE'])
@hasPermission("system:role:remove")
def deleteRole(role_ids):
    sysRole.deleteRoles(role_ids.split(","))
    return ResHelper.success()


@mod.route("/<role_id>", methods=["GET"])
@hasPermission("system:role:list")
def getRole(role_id):
    sysRole.checkRoleDataScope(role_id)
    role = sysRole.selectRoleByRoleId(role_id)
    if role is not None:
        role = role.to_json()
    return ResHelper.success(data=role)


@mod.route('', methods=['POST'], strict_slashes=False)
@hasPermission("system:role:add")
def addRole():
    sysRole.addRoles(request.json)
    return ResHelper.success()


@mod.route('', methods=['PUT'], strict_slashes=False)
@hasPermission("system:role:edit")
def updateRole():
    sysRole.updateRole(request.json)
    return ResHelper.success()


@mod.route('/authUser/allocatedList', methods=['GET'])
@hasPermission("system:role:list")
def allocatedList():
    params = request.values
    page = Page(page_num=int(params.get("pageNum")), page_size=int(params.get("pageSize")))
    users, total = sysUser.selectAllocatedList(params, page)
    return ResHelper.success(extend={"total": total, "rows": [item.to_json() for item in users]})


@mod.route('/authUser/unallocatedList', methods=['GET'])
@hasPermission("system:role:list")
def unAllocatedList():
    params = request.values
    page = Page(page_num=int(params.get("pageNum")), page_size=int(params.get("pageSize")))
    users, total = sysUser.selectUnallocatedList(params, page)
    return ResHelper.success(extend={"total": total, "rows": [item.to_json() for item in users]})


@mod.route('/authUser/selectAll', methods=['PUT'])
@hasPermission("system:role:list")
def selectAll():
    params = request.values
    sysRole.insertRoleUser(params)
    return ResHelper.success()


@mod.route('/authUser/cancel', methods=['PUT'])
@hasPermission("system:role:list")
def userRoleCancel():
    params = request.json
    sysRole.cancelRoleUsers(params)
    return ResHelper.success()


@mod.route('/authUser/cancelAll', methods=['PUT'])
@hasPermission("system:role:list")
def userRoleCancelAll():
    params = request.values
    sysRole.cancelRoleUsers(params)
    return ResHelper.success()
