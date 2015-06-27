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
        response = self.find({'status':0},{'_id': 0, 'id': 1, 'status': 1})
        return response.toJson()

    def create_task(self, data):
        response = self.insert(data)
        return response.toJson()

    def get_task_by_id(self, task_id):
        response = self.find({'id': int(task_id)},
                             {'_id': 0, 'id': 1, 'params': 1, 'subtask.ip': 1, 'subtask.params': 1,'subtask.status': 1})
        return response.toJson()

    def get_subtask_by_taskId(self, task_id):
        response = self.find({'id': int(task_id)}, {'_id': 0, 'subtask.ip': 1, 'subtask.status': 1})
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
            response = self.update({'id': int(data['id'])}, data)
        else:
            response = self.insert(data)
        return response.toJson()


# 安装脚本相关的class
@singleton
class Scripts(PyConnect):
    def __init__(self):
        PyConnect.__init__(self, 'script')

    # 删除一个安装脚本
    def del_script_by_id(self, id):
        response = self.remove({'id': id})
        return response.toJson()

    # 获取一个安装脚本信息
    def get_script_by_id(self, id):
        response = self.find(query={'id': id},
                             field={'_id': 0, 'id': 1, 'name': 1, 'version': 1, 'description': 1, 'script': 1,
                                    'checkList': 1})
        return response.toJson()

    # 根据脚本名字取得所有安装脚本,如果查询字为空,则返回所有
    def search_scripts_by_name(self, name=None):
        if (name != None):
            response = self.find({"name": re.compile(name)}, {'_id': 1, 'name': 1, 'ver': 1})
        else:
            response = self.find(field={'_id': 0, 'id': 1, 'name': 1, 'version': 1})
        return response.toJson()

    # 根据脚本名字取得所有安装脚本,如果查询字为空,则返回所有
    def save_script(self, data):
        if (data.has_key('id') and data['id'] != None):
            response = self.update({'id': int(data['id'])}, data)
        else:
            response = self.insert(data)
        return response.toJson()


if __name__ == '__main__':
    db = Task()
    db.remove({"id": 1435307487061927})
    #db.update({'id': 1435307487061927}, {'subtask': [{'ip':'1'},{'ip':'2'}]})
    print db.get_subtask_by_taskId(1435307487061927)
    print db.get_taskList()
