import logging

from flask import Blueprint, request

from wlkc_core import ResHelper
from wlkc_admin.modules.sys import User
from wlkc_admin.services import sysUser, sysRole, sysPost
from wlkc_core.utils.auth import hasPermission, login_handler

mod = Blueprint('user', __name__, url_prefix='/system/user/')


@mod.route('/list')
@hasPermission("system:user:list")
def main():
    params = request.values
    user = sysUser.User(**params)
    page = sysUser.Page(int(params.get("pageNum")), int(params.get("pageSize")))
    users, total = sysUser.queryUserList(user, page)
    return ResHelper.success(extend=dict(rows=users, total=total))


@mod.route('/changeStatus', methods=['PUT'])
@hasPermission("system:user:edit")
def changeStatus():
    data = request.json
    user = User(user_id=data.get("userId"), status=data.get("status"))
    sysUser.checkUserAllowed(user)
    sysUser.checkUserDataScope(user.user_id)
    update_count = sysUser.updateUserStatus(user)

    return ResHelper.success()


@mod.route('/deptTree', methods=['GET'])
@login_handler()
def deptTree():
    return ResHelper.success()


@mod.route('/', methods=['GET'])
@mod.route('/<user_id>', methods=['GET'])
@hasPermission("system:user:query")
def index(user_id=None, **kwargs):
    sysUser.checkUserDataScope(User(user_id=user_id))
    roles = sysRole.selectRoleAll()
    data = dict(roles=[item.to_json() for item in roles], posts=sysPost.queryAllPosts())
    if user_id:
        user = sysUser.selectUserById(user_id)
        data.update(dict(data=user, roleIds=[item.get("roleId") for item in user.get("roles")], postIds=sysPost.queryPostByUserId(user_id)))

    return ResHelper.success(extend=data)


@mod.route("authRole/<user_id>", methods=['GET'])
@hasPermission("system:user:edit")
def authRole(user_id):
    roles = sysRole.selectRoleAll()
    user = sysUser.selectUserById(user_id)

    userRoles = [item.get("roleId") for item in user.get('roles')]
    listRoles = []
    for role in roles:
        jsonRole = role.to_json()
        if role.role_id in userRoles:
            jsonRole.update({"flag": True})
        listRoles.append(jsonRole)
    data = dict(roles=listRoles, user=user)
    return ResHelper.success(extend=data)


@mod.route("authRole", methods=['PUT'])
@hasPermission("system:user:edit")
def saveAuthRole():
    userId = request.args.get("userId")
    roleIds = request.args.get("roleIds")
    sysUser.saveAuthRole(userId, roleIds)
    return ResHelper.success()


@mod.route("", methods=['PUT'], strict_slashes=False)
@hasPermission('system:user:edit')
def userPut():
    logging.debug(request.json)
    sysUser.updateUser(request.json)
    return ResHelper.success()


@mod.route("/<user_ids>", methods=['DELETE'], strict_slashes=False)
@hasPermission('system:user:delete')
def userDel(user_ids=None):
    del_couunt = sysUser.deleteUser(user_ids)
    return ResHelper.success(code=200 if del_couunt > 0 else 500)


@mod.route("", methods=['POST'], strict_slashes=False)
@hasPermission('system:user:add')
def userAdd():
    userData = request.json
    sysUser.addUser(userData)
    return ResHelper.success()


@mod.route("/resetPwd", methods=['PUT'], strict_slashes=False)
@hasPermission('system:user:resetPwd')
def resetPassword():
    passwd = request.json
    sysUser.resetPassword(passwd.get("userId"), passwd.get("password"))
    return ResHelper.success()

#
# class userView(MethodView):
#     @hasPermission('system:user:edit')
#     def put(self, **kwargs):
#         logging.debug(request.json)
#         return ResHelper.success()
#
#     @hasPermission('system:user:add')
#     def post(self):
#         user = User(**request.json)
#         sysUser.addUser(user)
#         return ResHelper.success()
#
#
# mod.add_url_rule("", methods=["GET", "POST", "PUT"], view_func=userView.as_view(''), strict_slashes=False)
