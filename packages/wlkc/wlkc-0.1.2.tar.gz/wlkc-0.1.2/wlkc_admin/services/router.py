import traceback

from flask import request
from sqlalchemy import and_

from wlkc_core.database import db_session
from wlkc_admin.modules.sys import Menu, RoleMenu, User, UserRole, Role
from wlkc_admin.services import BaseService


class MenuBuilder:

    def __init__(self, menus: list[Menu]):
        self.menus = menus

    @staticmethod
    def firstUpCase(x):
        return x[0].upper() + x[1:]

    @staticmethod
    def keyToSanke(menu: dict):
        try:
            new_dict = {}
            for item in menu.keys():
                new_dict.update({BaseService.to_camel_case(item): menu.get(item)})
                # del menu[item]
            return new_dict
        except Exception as e:
            print(traceback.format_exc())

    def menuToJson(self, menus):
        jsonMenu = []
        for menu in menus:
            jMenu = menu.to_json()
            jMenu.update({"children": self.menuToJson(menu.children)})
            jsonMenu.append(self.keyToSanke(jMenu))
        return jsonMenu

    def buildMenuTree(self, parentId=0):
        level_menu = [item for item in self.menus if item.parent_id == parentId]
        json_menus = []
        for menu in level_menu:
            json_menu = {}
            subMenu = self.buildMenuTree(menu.menu_id)
            json_menu.update(dict(name=menu.menu_name, path=self.getRouterPath(menu), hidden=menu.visible == "1", component=self.getComponent(menu),
                                  meta=menu.meta))
            # menu.setSubMenu(subMenu)
            if len(subMenu) > 0 and menu.menu_type == "M":
                json_menu.update(dict(alwaysShow=True, redirect="noRedirect", children=subMenu))
            elif self.isMenuFrame(menu):
                json_menu.update(dict(name=menu.path, meta=None, children=subMenu))
            elif menu.parent_id == 0 and self.isInnerLink(menu):
                json_menu.update(dict(component=self.getRouterPath(menu), children=subMenu))
            json_menus.append(json_menu)
        return json_menus

    def getComponent(self, menu):
        component = "Layout"
        if menu.component is not None and menu.component != "" and not self.isMenuFrame(menu):
            component = menu.component
        elif (not menu.component or menu.component == "") and menu.parent_id != 0 and self.isInnerLink(menu):
            component = "InnerLink"
        elif (not menu.component or menu.component == "") and self.isParentView(menu):
            component = "ParentView"
        return component

    @staticmethod
    def isMenuFrame(menu):
        return menu.is_frame == "1" and menu.menu_type == "C" and menu.parent_id == 0

    @staticmethod
    def isInnerLink(menu):
        return menu.is_frame == "1" and (menu.path.startswith("http://") or menu.path.startswith("https://"))

    def isParentView(self, menu):
        return menu.parent_id != 0 and menu.menu_type == "M"

    def getRouterPath(self, menu):
        routerPath = menu.path
        if menu.parent_id != 0 and self.isInnerLink(menu):
            routerPath = self.innerLinkReplaceEach(routerPath)
        if menu.parent_id == 0 and menu.menu_type == "M" and menu.is_frame == 1:
            routerPath = "/" + routerPath
        elif self.isMenuFrame(menu):
            routerPath = "/"

        return routerPath

    @staticmethod
    def innerLinkReplaceEach(routerPath):
        return routerPath


def selectUserMenuTree():
    if getattr(request, 'user_id') == 1:
        showMenu = selectAllMenus()
    else:
        showMenu = selectUserMenus()

    return MenuBuilder(showMenu).buildMenuTree()


def selectAllMenus() -> list[Menu]:
    return Menu.query.filter(and_(Menu.status == 0, Menu.menu_type.in_(['M', 'C']))).order_by(Menu.order_num).all()


def selectUserMenus() -> list[Menu]:
    user_id = getattr(request, 'user_id')
    if user_id:
        menus = db_session.query(Menu) \
            .join(RoleMenu, RoleMenu.menu_id == Menu.menu_id, isouter=True) \
            .join(UserRole, UserRole.role_id == RoleMenu.role_id, isouter=True) \
            .join(Role, Role.role_id == UserRole.role_id, isouter=True) \
            .join(User, User.user_id == UserRole.user_id, isouter=True) \
            .filter(and_(User.user_id == user_id, Menu.menu_type.in_(["M", "C"]), Menu.status == 0, Role.status == 0)) \
            .order_by(Menu.parent_id, Menu.order_num).all()
        return menus
    return []
