from sqlalchemy import and_

from wlkc_admin.modules.sys import Menu, RoleMenu
from wlkc_core.database import db_session


def selectMenuPermsByRoleId(roleId) -> list:
    roles = db_session.query(Menu.perms).join(RoleMenu, RoleMenu.menu_id == Menu.menu_id).filter(and_(RoleMenu.role_id == roleId, Menu.status == "0")).all()
    return [item[0] for item in roles if item != ("",)]
