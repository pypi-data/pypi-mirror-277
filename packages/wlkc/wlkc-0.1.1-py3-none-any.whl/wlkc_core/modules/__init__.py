import datetime

from sqlalchemy import Column, String, DateTime

from wlkc_admin.services import BaseService


def class_keys(classes, exclude=None):
    keys = [item for item in dir(classes) if not str(item).startswith("_") and not callable(getattr(classes, item)) and item != 'is_admin']
    if exclude:
        keys = [item for item in keys if item not in exclude]
    return keys


class BaseModule:

    def __init__(self, **kwargs):
        self.__keys__ = class_keys(self)
        for k, v in kwargs.items():
            key = BaseService.to_snake_case(k)
            if key in self.__keys__:
                setattr(self, key, str(v).strip() if isinstance(v, str) else v)

    def update(self, **kwargs):
        self.__keys__ = class_keys(self)
        for k, v in kwargs.items():
            key = BaseService.to_snake_case(k)
            if key in self.__keys__:
                setattr(self, key, str(v).strip() if isinstance(v, str) else v)
        return self

    # def __eq__(self, other):
    #     return type(self) is type(other) and self.id == other.id
    #
    # def __ne__(self, other):
    #     return not self.__eq__(other)

    def to_json(self, exclude: list[str] = None, camelKey=True):
        dict_data = {}
        base_exclude = ['query', 'metadata', 'registry']
        if exclude:
            base_exclude.extend(exclude)
        keys = [item for item in dir(self) if not str(item).startswith("_") and not callable(getattr(self, item)) and item not in base_exclude]
        for key in keys:
            data = getattr(self, key)
            key = BaseService.to_camel_case(key)
            if type(data) is datetime.datetime:
                dict_data.update({key: data.strftime('%Y-%m-%d %H:%M:%S')})
            else:
                dict_data.update({key: data})
        return dict_data


class BaseColumn:
    status = Column('status', String(1))
    create_by = Column(String(64))
    create_time = Column(DateTime)
    update_by = Column(String(64))
    update_time = Column(DateTime)


class Page:
    def __init__(self, page_num: int = 1, page_size: int = 10):
        self.page_num: int = int(page_num)
        self.page_size: int = int(page_size)

    def set_page(self, page_num: int, page_size: int):
        self.page_num = page_num
        self.page_size = page_size


class PageObject:
    def __init__(self, query, page: Page):
        self.query = query
        self.page = page
        self.__build__()

    def build(self, json: bool = True):
        if json is True:
            return dict(rows=[item.to_json() for item in self.rows], total=self.total)
        return self.rows, self.total

    def __build__(self):
        self.total = self.query.count()
        if self.page:
            self.query = self.query.offset(self.page.page_size * (self.page.page_num - 1)).limit(self.page.page_size)
        self.rows = self.query.all()
