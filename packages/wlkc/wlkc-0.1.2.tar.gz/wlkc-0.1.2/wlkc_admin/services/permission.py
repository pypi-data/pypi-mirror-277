from wlkc_admin.services import menu


def getMenuPermission(user: dict):
    if user.get("isAdmin"):
        return {"*:*:*"}
    permission = []
    for role in user.get("roles"):
        pers = menu.selectMenuPermsByRoleId(role.get("roleId"))
        permission.extend(pers)
    return set(permission)
