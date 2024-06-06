import logging
import traceback
from datetime import datetime
from typing import Union

from sqlalchemy import select, and_

from wlkc_core import UserException, OtherException
from wlkc_core.database import db_session
from wlkc_core.modules import Page
from wlkc_admin.modules.sys import Role, UserRole, User, Dept, RoleMenu
from wlkc_core.utils import SessionHelper


def selectQuery():
    return db_session.query(Role).join(UserRole, UserRole.role_id == Role.role_id, isouter=True) \
        .join(User, User.user_id == UserRole.user_id, isouter=True) \
        .join(Dept, Dept.dept_id == User.dept_id, isouter=True).filter(Role.del_flag == 0)


def checkRoleDataScope(role_id):
    """校验用户是否有数据权限"""
    user = User(user_id=SessionHelper.userId())
    if not user.is_admin:
        roles = selectQuery().filter(Role.role_id == role_id).all()
        if len(roles) == 0:
            raise UserException(101, "没有权限访问角色数据")


def checkRoleAllowed(role: Role):
    if role.role_id is not None and role.is_admin:
        raise UserException(150, "不允许操作超级管理员角色")


def selectRoleAll():
    roles, _ = selectRoleList(Role(), None)
    # isAdmin = BaseService.isAdmin(SessionHelper.userId())
    if not SessionHelper.isAdminUser():
        roles = [item for item in roles if not item.is_admin]
    return roles


def selectRoleList(role: Role, page: Union[Page, None]):
    query = selectQuery().order_by(Role.role_sort, Role.role_id)
    if role:
        if role.role_id:
            query = query.filter(Role.role_id == role.role_id)
        if role.role_name:
            query = query.filter(Role.role_name.like(f"%{role.role_name}%"))
        if role.role_key:
            query = query.filter(Role.role_key == role.role_key)
        if role.status:
            query = query.filter(Role.status == role.status)
    total = query.count()
    if page:
        query = query.offset(page.page_size * (page.page_num - 1)).limit(page.page_size)
    return query.all(), total


def loadUserRoles(user_id) -> list[dict]:
    exclude = ["create_by", "create_time", "update_time", "update_by", "password"]
    userRole = db_session.execute(select(UserRole.user_id, UserRole.role_id).filter(UserRole.user_id == user_id)).all()
    if userRole:
        role_ids = [item.role_id for item in userRole]
        roles = Role.query.filter(Role.role_id.in_(role_ids)).all()
        roles = [item.to_json(exclude=exclude) for item in roles]
        return roles
    return []


def selectRoleByRoleId(roleId):
    return selectQuery().filter(Role.role_id == roleId).first()


def countUserRoleByRoleId(roleId):
    user_count = UserRole.query.filter(UserRole.role_id == roleId).count()
    role = Role.query.filter(Role.role_id == roleId).first()
    if user_count > 0:
        raise OtherException(f"角色【{role.role_name}】已分配,不能删除")


def deleteRoleMenu(roleIds):
    """删除角色与菜单关联"""
    db_session.query(RoleMenu).filter(RoleMenu.role_id.in_(roleIds)).delete()


def deleteRoleDept(roleIds):
    """删除角色与部门关联"""
    # db_session.query(RoleDept).filter(Dept.dept_id.in_(roleIds)).delete()
    pass


def deleteUserRoles(userIds):
    db_session.query(UserRole).filter(UserRole.user_id.in_(userIds)).delete()


def deleteRoles(role_ids):
    try:
        if role_ids:
            role_ids = role_ids
        for role_id in role_ids:
            checkRoleAllowed(Role(role_id=role_id))
            checkRoleDataScope(role_id)
            countUserRoleByRoleId(role_id)
        del_count = db_session.query(Role).filter(Role.role_id.in_(role_ids)) \
            .update({"del_flag": 2, "update_by": SessionHelper.userName(), "create_time": datetime.now()})

        # 删除角色与菜单关联
        deleteRoleMenu(role_ids)
        # 删除角色与部门关联
        deleteRoleDept(role_ids)
        db_session.commit()
        return del_count
    except Exception as e:
        db_session.rollback()
        logging.error(traceback.format_exc())
        raise e


def updateStatus(role: Role):
    try:
        checkRoleAllowed(role)
        checkRoleDataScope(role.role_id)
        update_count = db_session.query(Role).filter(Role.role_id == role.role_id) \
            .update({"status": role.status, "update_by": SessionHelper.userName(), "update_time": datetime.now()})
        db_session.commit()
        return update_count
    except Exception as e:
        logging.error(traceback.format_exc())
        raise e


def checkRoleNameUnique(role):
    role_id = -1 if role.role_id is None or role.role_id == "" else role.role_id
    role = selectQuery().filter(Role.role_name == role.role_name).first()
    if role is not None and role.role_id != role_id:
        raise OtherException("角色名称已存在")


def checkRoleKeyUnique(role):
    role_id = -1 if role.role_id is None or role.role_id == "" else role.role_id
    role = selectQuery().filter(Role.role_key == role.role_key).first()
    if role is not None and role.role_id != role_id:
        raise OtherException("权限字符已存在")


def addRoles(json_data):
    try:
        if type(json_data) is not dict:
            raise OtherException("请求数据异常")
        role = Role(**json_data)
        role.update(create_by=SessionHelper.userId(), update_time=datetime.now())
        checkRoleNameUnique(role)
        checkRoleKeyUnique(role)
        # 插入角色
        add_count = db_session.add(role)
        db_session.flush()
        insertRoleMenu(role, json_data.get("menuIds"))
        db_session.commit()
        return add_count
    except Exception as e:
        db_session.rollback()
        logging.error(traceback.format_exc())
        raise e


def insertRoleMenu(role: Role, menus):
    if menus and len(menus) > 0:
        roleMenus = [RoleMenu(menu_id=menu, role_id=role.role_id) for menu in menus if menu]
        db_session.add_all(roleMenus)


def updateRole(json_data):
    try:
        if type(json_data) is not dict:
            raise OtherException("请求数据异常")
        role = Role(**json_data)
        if role.role_id is None or role.role_id == "":
            raise OtherException("角色ID不能为空")
        checkRoleAllowed(role)
        checkRoleDataScope(role.role_id)
        checkRoleNameUnique(role)
        checkRoleKeyUnique(role)

        role = selectRoleByRoleId(role.role_id)
        role.update(**json_data).update(**{"update_by": SessionHelper.userName(), "update_time": datetime.now()})
        update_count = db_session.add(role)
        # 删除角色菜单
        deleteRoleMenu([role.role_id])
        # 插入角色菜单
        insertRoleMenu(role, json_data.get("menuIds"))
        db_session.commit()
        return update_count
    except Exception as e:
        db_session.rollback()
        raise e


def insertRoleUser(params):
    try:
        role_id = params.get("roleId")
        user_ids = params.get("userIds").split(",")
        checkRoleDataScope(role_id)
        role_users = []
        for user_id in user_ids:
            role_users.append(UserRole(role_id=role_id, user_id=user_id))
        if len(role_users) > 0:
            insert_count = db_session.add_all(role_users)
            db_session.commit()
            return insert_count
        return 0
    except Exception as e:
        logging.error(traceback.format_exc())
        db_session.rollback()
        raise e


def cancelRoleUsers(params):
    try:
        role_id = params.get("roleId")
        if params.get("userIds"):
            user_ids = params.get("userIds").split(",")
        else:
            user_ids = [params.get("userId")]
        if len(user_ids) > 0:
            del_count = db_session.query(UserRole).filter(and_(UserRole.role_id == role_id, UserRole.user_id.in_(user_ids))).delete(synchronize_session=False)
            db_session.commit()
            return del_count
    except:
        logging.error(traceback.format_exc())
        db_session.rollback()
    return 0
