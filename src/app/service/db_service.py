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

    def create_task(self, data):
        response = self.insert(data)
        return response

    def get_task_by_id(self, task_id):
        response = self.find_one({'id': int(task_id)},
                             {'_id': 0, 'id': 1, 'process_id': 1, 'params': 1, 'subtask': 1})
        return response

    def get_task_by_id(self, task_id):
        response = self.find_one({'id': int(task_id)}, {'_id': 0, 'id': 1, 'process_id': 1, 'params': 1, 'subtask': 1})
        return response

    def get_subtask_by_taskId(self, task_id):
        response = self.find_one({'id': int(task_id)}, {'_id': 0, 'subtask.ip': 1, 'subtask.status': 1})
        return response

    def update_task_by_taskId(self, task_id, data):
        response = self.update_set({'id': int(task_id)}, data)
        return response


# 部署目录的class
@singleton
class Process(PyConnect):
    def __init__(self):
        PyConnect.__init__(self, 'process')

    # 取得部署流程列表
    def get_process_list(self):
        response = self.find(field={'_id': 0, 'id': 1, 'name': 1})
        return response

    # 根据id取得安装步骤列表，每次取得1个
    def get_process_detail_by_id(self, id):
        response = self.find_one({'id': int(id)}, {'_id': 0, 'id': 1, 'name': 1, 'process': 1})
        return response

    # 删除部署流程,status=0 表示成功 -1表示失败
    def del_process_by_id(self, id):
        response = self.remove({'id': int(id)})
        return response

    def save_process(self, data):
        if data.get('id'):
            response = self.update_set({'id': int(data.get('id'))}, data)
        else:
            response = self.insert(data)
        return response


# 安装脚本相关的class
@singleton
class Scripts(PyConnect):
    def __init__(self):
        PyConnect.__init__(self, 'script')

    # 删除一个安装脚本
    def del_script_by_id(self, id):
        response = self.remove({'id': id})
        return response

    # 获取一个安装脚本信息
    def get_script_by_id(self, id):
        response = self.find_one(query={'id': id},
                                 field={'_id': 0, 'id': 1, 'name': 1, 'version': 1, 'description': 1, 'script': 1,
                                        'params': 1,'checkList': 1})
        return response

    # 根据脚本名字取得所有安装脚本,如果查询字为空,则返回所有
    def search_scripts_by_name(self, name=None):
        if (name != None):
            response = self.find({"name": re.compile(name)}, {'_id': 1, 'name': 1, 'ver': 1})
        else:
            response = self.find(field={'_id': 0, 'id': 1, 'name': 1, 'version': 1})
        return response

    # 根据脚本名字取得所有安装脚本,如果查询字为空,则返回所有
    def save_script(self, data):
        if (data.has_key('id') and data['id'] != None):
            response = self.update_set({'id': int(data['id'])}, data)
        else:
            response = self.insert(data)
        return response


if __name__ == '__main__':
    # db = Task()
    # db.remove({"id": 1435307487061927})
    # db.update({'id': 1435307487061927}, {'subtask': [{'ip':'1'},{'ip':'2'}]})
    # print db.get_subtask_by_taskId(1435307487061927)
    # print db.get_taskList()
    # analysis_param("@QES @1233 &ANS =abcc &CHE =yyzz")

    #data = "jjk; $aaa jkjkj jjjk kjkjl $bbbbb jkjkl; ioqi3nnknjk;\njkklj\t\n  $aaaa"
    #matchObj = re.findall(r'\$(\w+)', data)
    #if matchObj:
    #    print matchObj
    data = Task()
    data.update_set()("{'subtask.ip':'192.168.0.236'}","{'subtask.log':['aaa','bbb','ccc']}")