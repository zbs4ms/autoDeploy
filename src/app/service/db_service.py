# -*- coding: utf-8 -*-

import tool
from dao import PyConnect
import re


def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return _singleton


# 任务相关的class
@singleton
class Task(PyConnect):
    def __init__(self):
        PyConnect.__init__(self, 'task')

    # 取得正在运行中的任务列表
    def get_taskList(self):
        response = self.find(field={'_id': 0, 'name': 1})
        return response.toJson()


# 部署目录的class
@singleton
class Process(PyConnect):
    def __init__(self):
        PyConnect.__init__(self, 'process')

    # 取得部署流程列表
    def get_processList(self):
        response = self.find(field={'_id': 0, 'id': 1, 'name': 1})
        return response.toJson()

    # 根据id取得安装步骤列表
    def get_process_detail_by_id(self, id):
        response = self.find({'id': int(id)}, {'_id': 0, 'id': 1, 'name': 1, 'process': 1})
        return response.toJson()

    # 删除部署流程,status=0 表示成功 -1表示失败
    def del_process_by_id(self, id):
        response = self.remove({'id': int(id)})
        return response.toJson()

    def save_process(self, data):
        if (data['id'] != None):
            response = self.update({'id': data['id']}, data)
        else:
            response = self.insert(data)
        return response.toJson()

    def get_parameter(self,id):
        response = self.find({'id':int(id)},{'_id':0,'parameter':1})
        return response.toJson()


# 安装脚本相关的class
@singleton
class Scripts(PyConnect):
    def __init__(self):
        PyConnect.__init__(self, 'script')

    # 删除一个安装脚本
    def del_script_by_id(self, id):
        response = self.remove({'_id': id})
        return response.toJson()

    # 获取一个安装脚本信息
    def get_script_by_id(self, id):
        response = self.find(query={'id': id}, field={'_id': 0, 'name': 1, 'ver': 1, 'description': 1})
        return response.toJson()

    # 根据脚本名字取得所有安装脚本,如果查询字为空,则返回所有
    def search_scripts_by_name(self, name=None):
        if (name != None):
            response = self.find({"name": re.compile(name)}, {'_id': 1, 'name': 1, 'ver': 1})
        else:
            response = self.find(field={'_id': 0, 'name': 1, 'ver': 1})
        return response.toJson()

    def get_parameter(self,id):
        response = self.find({'id':int(id)},{'_id':0,'parameter':1})
        return response.toJson()


if __name__ == '__main__':
    d1 = Scripts()
    # d1.remove({"name":"123"})
    list = d1.search_scripts_by_name()

    print list
