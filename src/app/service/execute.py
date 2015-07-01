# -*- coding: utf-8 -*-
import tool
import socket
import threading
import db_service
import os
import commands
import socket
import json
from clinet import Clinet

class InitClinet(threading.Thread):
    def __init__(self,task_id,order):
        super(InitClinet, self).__init__()
        if not task_id:
            raise  "无效的参数传递"
        self.task_id = task_id
        myname = socket.getfqdn(socket.gethostname())
        self.serviceIp = socket.gethostbyname(myname);
        self.serviceHost = 5000
        self.serviceRoute = "/sub_task/call_back"
        self.order=order
        #初始化些数据库
        self.task = db_service.Task()
        self.process = db_service.Process()
        self.script = db_service.Scripts()

    def execute(self):
        (taskData,process,script) = self.findDataByDatabase(self.order)
        data={}
        data["serviceIp"]=self.serviceIp
        data["serviceHost"]=self.serviceHost
        data["serviceRoute"]=self.serviceRoute
        data["order"]=self.order
        data["taskId"]=self.task_id
        data["content"]=script.get("bash_shell")
        data["scriptId"]=script.get("id")
        data["processId"]=taskData.get("process_id")
        data["type"]=script.get("type")
        for sub in taskData.get('subtask'):
            data["clinetIp"]=sub.get('ip')
            data["parameter"]=sub.get('params')
            data["user"]=sub.get("user")
            data["passwd"]=sub.get("password")
            data["clinetPath"]="/usr/local"
            data["servicePath"]=os.getcwd()+"/clinet"
            clinet = Clinet(data)
            log = clinet.execute(copyFile=True,runClinet=True,send=True)
            for l in log:
                print l

    def findDataByDatabase(self,order):
        taskData = self.task.get_task_by_id(self.task_id).result
        if taskData.get("process_id") and taskData.get("subtask"):
            process = self.process.get_process_detail_by_id(taskData.get("process_id")).result
            if process.get('process') and process.get('process')[order]:
                scriptId=process.get('process')[order].get('id')
                script = self.script.get_script_by_id(scriptId).result
                return taskData,process,script
            else:
                raise ValueError("process 数据库数据不完整")
        else:
            raise ValueError("task 数据库数据不完整")


if __name__ == '__main__':
    aa = InitClinet('1435514343626092',0)
    aa.execute();
