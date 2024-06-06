import logging

from flask import Blueprint, request

from wlkc_core import ResHelper
from wlkc_core.modules import Page
from wlkc_admin.modules.sys import SysDict, SysDictData
from wlkc_admin.services import sysDict
from wlkc_core.utils import RedisHelper
from wlkc_core.utils.auth import login_handler

mod = Blueprint('dict', __name__, url_prefix='/system/dict')


@mod.route('/data/type/<type>')
@login_handler()
def query_dict_type(type):
    logging.debug(type)
    dict_data = RedisHelper.get_json(f"sys_dict:{type}")
    return ResHelper.success(data=dict_data)


@mod.route('/type/list')
@login_handler()
def query_dict_type_list():
    params = request.args.to_dict()
    page = Page(page_num=params.get('pageNum', 1), page_size=params.get('pageSize', 10))
    dictType = SysDict(**params)
    data = sysDict.queryList(dictType, page)
    return ResHelper.success(extend=data)


@mod.route("/type", methods=['POST'], strict_slashes=False)
@login_handler()
def dictAdd():
    params = request.json
    sysDict.addDictType(params)
    return ResHelper.success()


@mod.route("/type", methods=['PUT'], strict_slashes=False)
@login_handler()
def dictEdit():
    params = request.json
    sysDict.updateDictType(params)
    return ResHelper.success()


@mod.route("/type/optionselect", methods=['GET'], strict_slashes=False)
@login_handler()
def optionSelect():
    return ResHelper.success(data=[item for item in sysDict.queryAll()])


@mod.route("/type/<type_id>", methods=['GET'], strict_slashes=False)
@login_handler()
def queryByDictTypeId(type_id):
    data = sysDict.queryDictTypeById(type_id)
    return ResHelper.success(data=data.to_json() if data is not None else None)


@mod.route("/type/<type_ids>", methods=['DELETE'], strict_slashes=False)
@login_handler()
def deleteByTypeId(type_ids):
    data = sysDict.deleteDictType(type_ids)
    return ResHelper.success(data=data.to_json() if data is not None else None)


@mod.route("/data/list", methods=['GET'], strict_slashes=False)
@login_handler()
def queryByDictTypeList():
    params = request.args.to_dict()
    page = Page(page_num=params.get('pageNum', 1), page_size=params.get('pageSize', 10))
    dictData = SysDictData(**params)
    data = sysDict.queryDictDataByList(dictData, page)
    return ResHelper.success(extend=data)


@mod.route("/data", methods=['POST'], strict_slashes=False)
@login_handler()
def dataAdd():
    params = request.json
    sysDict.addDictTypeData(params)
    return ResHelper.success()


@mod.route("/data", methods=['PUT'], strict_slashes=False)
@login_handler()
def dataEdit():
    params = request.json
    sysDict.updateDictTypeData(params)
    return ResHelper.success()


@mod.route("/data/<dict_code>", methods=['GET'], strict_slashes=False)
@login_handler()
def queryByDictTypeDataId(dict_code):
    data = sysDict.queryDictTypeDataById(dict_code)
    return ResHelper.success(data=data.to_json() if data is not None else None)


@mod.route("/data/<data_codes>", methods=['DELETE'], strict_slashes=False)
@login_handler()
def deleteDataByTypeId(data_codes):
    sysDict.deleteDictTypeDataByCode(data_codes.split(","))
    return ResHelper.success()
