from wlkc_admin.modules.sys import Dept


def queryDeptByUserId(userId):
    pass


def queryDeptByDeptId(deptId):
    if deptId:
        dept = Dept.query.filter(Dept.dept_id == deptId).first()
        return dept.to_json()
    return None
