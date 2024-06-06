from wlkc_core.database import db_session
from wlkc_admin.modules.sys import Menu, RoleMenu, UserRole, Role
from wlkc_admin.services import BaseService
from wlkc_core.utils import SessionHelper


def __menuList__(menu: Menu):
    query = Menu.query
    if menu is not None:
        if menu.menu_name:
            query = query.filter(Menu.menu_name.like(f"%{menu.menu_name}%"))
        if menu.visible:
            query = query.filter(Menu.visible == menu.visible)
        if menu.status:
            query = query.filter(Menu.status.like(f"%{menu.status}%"))
    return query.order_by(Menu.parent_id, Menu.order_num).all()


def __userMenuList__(menu: Menu):
    user_id = SessionHelper.userId()
    query = Menu.query.join(RoleMenu, RoleMenu.menu_id == Menu.menu_id) \
        .join(UserRole, UserRole.role_id == RoleMenu.role_id) \
        .join(Role, Role.role_id == UserRole.role_id).filter(UserRole.user_id == user_id)

    if menu is not None:
        if menu.menu_name:
            query = query.filter(Menu.menu_name.like(f"%{menu.menu_name}%"))
        if menu.visible:
            query = query.filter(Menu.visible == menu.visible)
        if menu.status:
            query = query.filter(Menu.status.like(f"%{menu.status}%"))
    return query.order_by(Menu.parent_id, Menu.order_num).all()


def selectMenuList(menu: Menu = None):
    if BaseService.isAdmin(SessionHelper.userId()):
        a = __menuList__(menu)
    else:
        a = __userMenuList__(menu)
    return a


def __build_child__(menus, menuId):
    children = [item for item in menus if item.parent_id == menuId]
    json_children = []
    for child in children:
        json_child = {"id": child.menu_id, "label": child.menu_name}
        childs = __build_child__(menus, child.menu_id)
        if childs:
            json_child.update({"children": childs})
        json_children.append(json_child)
    return json_children


def __build_tree__(menus):
    menu_ids = [item.menu_id for item in menus]
    json_menus = []
    for menu in menus:
        # 判断为跟节点
        if menu.parent_id not in menu_ids:
            json_menu = {"id": menu.menu_id, "label": menu.menu_name}
            json_menu.update({'children': __build_child__(menus, menu.menu_id)})
            json_menus.append(json_menu)

    return json_menus if len(json_menu) > 0 else [{"id": item.menu_id, "label": item.menu_name} for item in menus]


def selectMenuTree():
    menus = selectMenuList()
    return __build_tree__(menus)


def selectMenuIdsByRoleId(role: Role):
    query = db_session.query(Menu).join(RoleMenu, RoleMenu.menu_id == Menu.menu_id, isouter=True).filter(RoleMenu.role_id == role.role_id)
    if role.menu_check_strictly == 1:
        pids = [item[0] for item in db_session.query(Menu.parent_id).join(RoleMenu, RoleMenu.menu_id == Menu.menu_id).filter(RoleMenu.role_id == role.role_id).all()]
        query = query.filter(Menu.menu_id.notin_(pids))
    return query.order_by(Menu.parent_id, Menu.order_num).all()


def selectMenuListByRoleId(role_id):
    from wlkc_admin.services import sysRole
    role = sysRole.selectRoleByRoleId(role_id)
    if role is not None:
        return [item.menu_id for item in selectMenuIdsByRoleId(role)]
    return []
