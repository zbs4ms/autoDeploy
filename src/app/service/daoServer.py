# -*- coding: utf-8 -*-

import tool
import dao


#任务相关的class
class Task(object):
    def __init__(self):
        self.conn = dao.PyConnect()
     #取得正在运行中的任务列表
    def get_taskList(self):
        self.conn.setCollection('task')
        list = self.conn.find(field={'_id': 0, 'name': 1})
        return tool.getDictByCursor(list)

#部署目录的class
class Process(object):
    def __init__(self):
        self.conn = dao.PyConnect()

    #取得部署流程列表
    def get_processList(self):
        self.conn.setCollection('process')
        list = self.conn.find(field={'_id': 0, 'name': 1, 'id': 1})
        return tool.getDictByCursor(list)

    #根据取得安装步骤列表
    def get_process_detail(self,id):
        self.conn.setCollection('process')
        list = self.conn.find(query={'id': id}, field={'_id': 0, 'scriptList': 1})
        return tool.getDictByCursor(list)

    #删除部署流程,status=0 表示成功 -1表示失败
    def del_process(self,id):
        self.conn.setCollection('process')
        req = self.conn.remove({'id':id})
        return req

    #新建安装部署
    def save_process(self,data):
        self.conn.setCollection('process')
        return "未完"

#安装脚本相关的class
class Scripts(object):
    def __init__(self):
        self.conn = dao.PyConnect()

    #删除一个安装脚本
    def del_script(self,id):
        self.conn.setCollection('script')
        req = self.conn.remove({'id':id})
        return req

    #获取一个安装脚本信息
    def get_script_by_id(self,id):
        self.conn.setCollection('script')
        list = self.conn.find(query={'id':id},field={'_id':0,'name':1,'ver':1,'description':1})
        return tool.getDictByCursor(list)

    #取得所有安装脚本列表
    def search_scripts(self):
        self.conn.setCollection('script')
        list = self.conn.find(field={'_id':0,'id':1,'name':1,'ver':1})
        return tool.getDictByCursor(list)

#目标机相关class
class Target(object):
    def __init__(self):
        self.conn = dao.PyConnect()



