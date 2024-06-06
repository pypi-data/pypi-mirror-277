import logging
import traceback
from datetime import datetime

from wlkc_core import OtherException
from wlkc_core.database import db_session
from wlkc_core.modules import PageObject, Page
from wlkc_admin.modules.sys import SysDict, SysDictData
from wlkc_core.utils import SessionHelper, RedisHelper


def queryAll():
    dicts = SysDict.query.all()
    dictList = []
    for item in dicts:
        json_dict = item.to_json()
        json_dict.update(dict(child=queryDictDataByDictId(item.dict_type)))
        dictList.append(json_dict)
    return dictList


def queryDictDataByDictId(dict_type):
    datas = SysDictData.query.filter(SysDictData.dict_type == dict_type).order_by(SysDictData.dict_sort).all()
    return [item.to_json(exclude=['create_by', 'update_by', 'create_time', 'update_time']) for item in datas]


def queryList(dictType: SysDict, page: Page):
    query = SysDict.query

    if dictType.dict_name:
        query = query.filter(SysDict.dict_name.like(f"%{dictType.dict_name}%"))
    if dictType.dict_type:
        query = query.filter(SysDict.dict_type == dictType.dict_type)
    if dictType.status:
        query = query.filter(SysDict.status == dictType.status)

    return PageObject(query, page).build()


def checkDictTypeNameUnique(dictType: SysDict):
    data = SysDict.query.filter(SysDict.dict_name == dictType.dict_name).first()
    if data is not None and data.dict_id != dictType.dict_id:
        raise OtherException("字典名称已存在")


def checkDictTypeUnique(dictType: SysDict):
    data = SysDict.query.filter(SysDict.dict_type == dictType.dict_type).first()
    if data is not None and data.dict_id != dictType.dict_id:
        raise OtherException("字典类型已存在")


def addDictType(json_data):
    try:
        if type(json_data) is not dict:
            raise OtherException("请求数据异常")
        dictType = SysDict(**json_data)
        dictType.update(create_by=SessionHelper.userName(), update_time=datetime.now())
        checkDictTypeNameUnique(dictType)
        checkDictTypeUnique(dictType)
        # 插入角色
        add_count = db_session.add(dictType)
        db_session.commit()
        loadDictToCache()
        return add_count
    except Exception as e:
        db_session.rollback()
        logging.error(traceback.format_exc())
        raise e


def queryDictTypeById(type_id):
    data = SysDict.query.filter(SysDict.dict_id == type_id).first()
    return data


def updateDictTypeDataType(old_dict_type, new_dict_type):
    return db_session.query(SysDictData).filter(SysDictData.dict_type == old_dict_type).update({"dict_type": new_dict_type})


def updateDictType(params):
    if type(params) is not dict:
        raise OtherException("参数异常")
    dictType = SysDict(**params)
    if dictType.dict_id is None:
        raise OtherException("字典ID不能为空")

    checkDictTypeNameUnique(dictType)
    checkDictTypeUnique(dictType)
    try:
        existDict = SysDict.query.filter(SysDict.dict_id == dictType.dict_id).first()
        updateDictData = (False, None) if existDict.dict_type == dictType.dict_type else (True, existDict.dict_type)
        existDict.update(update_by=SessionHelper.userName(), update_time=datetime.now()).update(**params)
        db_session.add(existDict)

        if updateDictData[0]:
            updateDictTypeDataType(updateDictData[1], existDict.dict_type)
        loadDictToCache()
        db_session.commit()
    except Exception as e:
        logging.error(traceback.format_exc())
        db_session.rollback()
        raise e

    return None


def queryDictDataByList(dictData: SysDictData, page: Page):
    query = SysDictData.query.filter(SysDictData.dict_type == dictData.dict_type)
    if dictData.status:
        query = query.filter(SysDictData.status == dictData.status)
    if dictData.dict_label:
        query = query.filter(SysDictData.dict_label == dictData.dict_label)

    return PageObject(query, page).build()


def checkDictTypeDataNameUnique(dictTypeData: SysDictData):
    data = SysDictData.query.filter(SysDictData.dict_label == dictTypeData.dict_label).filter(SysDictData.dict_type == dictTypeData.dict_type).first()
    if data is not None and data.dict_code != dictTypeData.dict_code:
        raise OtherException("数据标签已存在")


def checkDictTypeDataValueUnique(dictTypeData: SysDictData):
    data = SysDictData.query.filter(SysDictData.dict_value == dictTypeData.dict_value).filter(SysDictData.dict_type == dictTypeData.dict_type).first()
    if data is not None and data.dict_code != dictTypeData.dict_code:
        raise OtherException("数据键值已存在")


def addDictTypeData(json_data):
    try:
        if type(json_data) is not dict:
            raise OtherException("请求数据异常")
        dictTypeData = SysDictData(**json_data)

        checkDictTypeDataNameUnique(dictTypeData)
        checkDictTypeDataValueUnique(dictTypeData)
        dictTypeData.update(create_by=SessionHelper.userName(), create_time=datetime.now())

        add_count = db_session.add(dictTypeData)
        db_session.commit()
        loadDictToCache()
        return add_count
    except  Exception as e:
        db_session.rollback()
        logging.error(traceback.format_exc())
        raise e


def updateDictTypeData(json_data):
    try:
        if type(json_data) is not dict:
            raise OtherException("请求数据异常")
        dictTypeData = SysDictData(**json_data)

        checkDictTypeDataNameUnique(dictTypeData)
        checkDictTypeDataValueUnique(dictTypeData)
        typeData = SysDictData.query.filter(SysDictData.dict_code == dictTypeData.dict_code).first()
        typeData.update(update_by=SessionHelper.userName(), update_time=datetime.now()).update(**json_data)
        update_count = db_session.add(typeData)
        db_session.commit()
        loadDictToCache()
        return update_count
    except  Exception as e:
        db_session.rollback()
        logging.error(traceback.format_exc())
        raise e


def queryDictTypeDataById(dict_code):
    return SysDictData.query.filter(SysDictData.dict_code == dict_code).first()


def deleteDictTypeDataByTypes(param):
    delete_count = SysDictData.query.filter(SysDictData.dict_type.in_(param)).delete()
    return delete_count


def deleteDictTypeDataByCode(param):
    delete_count = SysDictData.query.filter(SysDictData.dict_code.in_(param)).delete()
    db_session.commit()
    loadDictToCache()
    return delete_count


def deleteDictType(type_ids):
    try:
        dicts = SysDict.query.filter(SysDict.dict_id.in_(type_ids.split(","))).all()
        deleteDictTypeDataByTypes([item.dict_type for item in dicts])
        for dictType in dicts:
            db_session.delete(dictType)
        db_session.commit()
        loadDictToCache()
    except Exception as e:
        logging.error(traceback.format_exc())
        db_session.rollback()
        raise e


def loadDictToCache():
    keys = RedisHelper.keys("sys_dict:")
    for key in keys:
        RedisHelper.expire(key, 0)
    for item in queryAll():
        import json
        RedisHelper.set(f"sys_dict:{item.get('dictType')}", json.dumps(item.get("child"), ensure_ascii=False), None)
