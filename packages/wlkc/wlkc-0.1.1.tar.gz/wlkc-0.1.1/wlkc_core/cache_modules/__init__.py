from datetime import datetime


class LoginUser:
    # 登录时间
    loginTime = None
    # 过期时间
    expireTime = None
    # 登录IP地址
    ipaddr: str = None
    # 登录地点
    loginLocation: str = None
    # 浏览器类型
    browser: str = None
    # 操作系统
    os = None

    def __init__(self, user: dict, permissions: set):
        self.userId = user.get("user_id")
        self.deptId = user.get("dept_id")
        self.user = user
        self.permissions: set = permissions
        self.loginTime = datetime.now()
        self.roles = [item.get("roleKey") for item in user.get("roles")]

    @property
    def isAccountNonExpired(self) -> bool:
        return True

    @property
    def isAccountNonLocked(self) -> bool:
        return True

    @property
    def isCredentialsNonExpired(self) -> bool:
        return True

    @property
    def isEnabled(self) -> bool:
        return True

    def setToken(self, token):
        self.token = token

    def setLoginInfo(self, loginTime, expireTime, ipaddr, loginLocation, browser, os):
        self.loginTime = loginTime
        self.expireTime = expireTime
        self.ipaddr = ipaddr
        self.loginLocation = loginLocation
        self.browser = browser
        self.os = os

    def to_json(self, exclude=None):
        if exclude is None:
            exclude = []
        dict_data = {}
        base_exclude = ['query', 'metadata', 'registry']
        base_exclude.extend(exclude)
        keys = [item for item in dir(self) if not str(item).startswith("_") and not callable(getattr(self, item)) and item not in base_exclude]
        for key in keys:
            data = getattr(self, key)
            if type(data) is datetime:
                dict_data.update({key: data.strftime('%Y-%m-%d %H:%M:%S')})
            elif type(data) is set:
                dict_data.update({key: list(data)})
            else:
                dict_data.update({key: getattr(self, key)})
        return dict_data
