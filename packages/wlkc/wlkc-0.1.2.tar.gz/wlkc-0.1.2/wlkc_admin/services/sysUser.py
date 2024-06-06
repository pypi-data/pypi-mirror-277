import logging
import traceback
from datetime import datetime

import bcrypt
from sqlalchemy import or_, and_

from wlkc_core import UserException
from wlkc_core.database import db_session
from wlkc_core.modules import Page
from wlkc_admin.modules.sys import User, UserRole, UserPost, Dept, Role
from wlkc_admin.services import sysRole, sysDept, sysPost
from wlkc_core.utils import SessionHelper


def build_passwd(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


def queryUserList(user: User, page: Page):
    query = User.query.filter(User.del_flag == 0)

    if user:
        if user.user_name:
            query = query.filter(User.user_name.like(f"%{user.user_name}%"))
        if user.phonenumber:
            query = query.filter(User.phonenumber == user.phonenumber)
        if user.user_type:
            query = query.filter(User.user_type == user.user_type)
        if user.status:
            query = query.filter(User.status == user.status)
        if user.user_id:
            query = query.filter(User.user_id == user.user_id)
    total = query.count()
    if page:
        query = query.offset(page.page_size * (page.page_num - 1)).limit(page.page_size)

    users = [item.to_json() for item in query.all()]
    return users, total


def checkUserAllowed(user: User):
    """校验用户是否允许操作"""
    if user and user.user_id and user.is_admin:
        raise UserException(100, "不允许操作超级管理员用户")


def checkUserDataScope(user_id):
    """校验用户是否有数据权限"""
    user = User(user_id=SessionHelper.userId())
    if not user.is_admin:
        users = User.query.filter(User.user_id == user.user_id).all()
        if len(users) == 0:
            raise UserException(101, "没有权限访问用户数据")


def updateUserStatus(user):
    try:
        update_count = User.query.filter(User.user_id == user.user_id).update({"status": user.status})
        db_session.commit()
        return update_count
    except:
        logging.error(traceback.format_exc())
        db_session.rollback()
        raise UserException(102, "更新用户状态异常")


def selectUserById(user_id):
    exclude = ["create_by", "create_time", "update_time", "update_by", "password"]
    datas = db_session.query(User).filter(User.user_id == user_id).first()
    if datas:
        user = datas.to_json(exclude=exclude)
        user.update(dict(roles=sysRole.loadUserRoles(datas.user_id), depts=sysDept.queryDeptByDeptId(datas.dept_id)))
        # .join(UserRole, UserRole.user_id == User.user_id, isouter=True)
        # if len(user) > 0:
        #     return user[0]
        return user
    return None


class UserRolePost:
    @staticmethod
    def insertUserPost(user, postIds):
        """插入用户岗位列表"""
        return db_session.add_all([UserPost(user_id=user.user_id, post_id=item) for item in postIds])
        # db_session.flush()

    @staticmethod
    def insertUserRole(user, roleIds):
        """插入角色列表"""
        return db_session.add_all([UserRole(user_id=user.user_id, role_id=item) for item in roleIds])
        # db_session.flush()

    @classmethod
    def removeUserPost(cls, user):
        """删除岗位列表"""
        db_session.query(UserPost).filter(UserPost.user_id == user.user_id).delete()
        db_session.flush()
        # userPosts = UserPost.query.filter(UserPost.user_id == user.user_id).all()
        # for item in userPosts:
        #     db_session.delete(item)

    @classmethod
    def removeUserRole(cls, userId):
        # """删除角色列表"""
        db_session.query(UserRole).filter(UserRole.user_id == userId).delete()
        db_session.flush()
        # userRoles = UserRole.query.filter(UserRole.user_id == user.user_id).all()
        # for item in userRoles:
        #     db_session.delete(item)


def addUser(userData):
    """新增用户"""
    try:
        user = User(**userData)
        userList, _ = queryUserList(None, None)
        userList = [item for item in userList if (user.phonenumber and user.phonenumber == item.get("phonenumber")) or user.user_name == item.get('userName') or
                    (user.email and user.email == item.get("email"))]
        if len(userList) > 0:
            raise UserException(30, "请检查电话号码，用户名以及邮箱是否已存在！")

        user.update(create_time=datetime.now(), create_by=SessionHelper.userName(), password=build_passwd(user.password))
        db_session.add(user)
        # 刷新获得新增用户ID
        db_session.flush()
        # 新增用户岗位关联
        UserRolePost.insertUserPost(user, userData.get("postIds"))
        # 新增用户与角色管理
        UserRolePost.insertUserRole(user, userData.get("roleIds"))
        db_session.commit()
        pass
    except Exception as e:
        logging.error(traceback.format_exc())
        db_session.rollback()
        raise e
    finally:
        db_session.expire_all()


def updateUser(userData):
    """更新用户信息"""
    try:
        user = User(**userData)
        userList, _ = queryUserList(None, None)
        userList = [item for item in userList if
                    (user.phonenumber == item.get("phonenumber") or user.user_name == item.get('userName') or user.email == item.get("email")) and user.user_id != item.get(
                        "userId")]
        if len(userList) > 0:
            raise UserException(30, "修改的的电话号码、用户名或邮箱是否已存在！")

        userData.update(dict(update_time=datetime.now(), update_by=SessionHelper.userName()))

        user = User().query.filter(User.user_id == user.user_id).first()
        del userData['password']
        user.update(**userData)
        db_session.add(user)
        # db_session.flush()
        UserRolePost.removeUserPost(user)
        UserRolePost.removeUserRole(user.user_id)
        # 新增用户岗位关联
        UserRolePost.insertUserPost(user, userData.get("postIds"))
        # 新增用户与角色管理
        UserRolePost.insertUserRole(user, userData.get("roleIds"))
        db_session.commit()
        pass
    except:
        logging.error(traceback.format_exc())
        db_session.rollback()
        raise UserException(30, "更新用户异常")

    finally:
        db_session.expire_all()


def deleteUser(user_ids):
    """删除用户"""
    try:
        if user_ids:
            userIds = user_ids.split(',')
            if SessionHelper.userId() in userIds:
                raise UserException(3090, "当前用户不能删除")
            for user_id in userIds:
                checkUserAllowed(User(user_id=user_id))
                checkUserDataScope(user_id)
            # 删除用户与角色关联
            sysRole.deleteUserRoles(userIds)
            # 删除用户与岗位关联
            sysPost.deleteUserPost(userIds)
            del_count = db_session.query(User).filter(User.user_id.in_(userIds)).update({"del_flag": 2})
            db_session.commit()
            return del_count
    except Exception as e:
        db_session.rollback()
        raise e
    return 0


def resetPassword(userId, password):
    if userId and password:
        checkUserAllowed(User(user_id=userId))
        checkUserDataScope(userId)
        update_count = db_session.query(User).filter(User.user_id == userId).update({"password": build_passwd(password)})
        db_session.commit()
        return update_count

    raise UserException(33, "用户ID或者密码为空")


def saveAuthRole(userId, roleIds):
    try:
        checkUserDataScope(userId)
        UserRolePost.removeUserRole(userId)
        UserRolePost.insertUserRole(User(user_id=userId), roleIds.split(","))
        db_session.commit()
    except Exception as e:
        logging.error(traceback.format_exc())
        db_session.rollback()
        raise UserException(33, "修改用户角色异常")


def userSelect(user: User):
    query = db_session.query(User).join(Dept, Dept.dept_id == User.dept_id, isouter=True).join(UserRole, UserRole.user_id == User.user_id, isouter=True) \
        .join(Role, Role.role_id == UserRole.role_id, isouter=True).filter(User.del_flag == 0)
    if user.phonenumber:
        query = query.filter(User.phonenumber == user.phonenumber)
    if user.user_name:
        query = query.filter(User.user_name == user.user_name)
    return query


def selectUnallocatedList(params: dict, page: Page):
    query = userSelect(User(**params))
    query = query.filter(or_(Role.role_id != params.get("roleId"), Role.role_id.__eq__(None)))
    userIds = [item[0] for item in db_session.query(User.user_id).join(UserRole, and_(UserRole.user_id == User.user_id, UserRole.role_id == params.get("roleId")))]
    query = query.filter(User.user_id.notin_(userIds))
    total = query.count()
    if page:
        query = query.limit(page.page_size).offset(page.page_size * (page.page_num - 1))
    users = query.all()
    return users, total


def selectAllocatedList(params, page):
    query = userSelect(User(**params)).filter(Role.role_id == params.get("roleId"))
    total = query.count()
    if page:
        query = query.limit(page.page_size).offset(page.page_size * (page.page_num - 1))
    users = query.all()
    return users, total
