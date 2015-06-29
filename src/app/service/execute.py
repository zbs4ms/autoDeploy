# -*- coding: utf-8 -*-
import tool
import socket
import threading
import db_service
import os
import commands
import socket
import json

host = 5000

class InitClinet(threading.Thread):
    def __init__(self,task_id):
        super(InitClinet, self).__init__()
        self.task_id = task_id
        self.task = db_service.Task()
        self.process = db_service.Process()
        self.script = db_service.Scripts()

    def run(self):
        taskData= self.task.get_task_by_id(self.task_id).result[0]
        if taskData.has_key('subtask'):
            subtask=taskData['subtask']
        else:
            return None
        for sub in subtask:
            self.clinetIp = sub.get('ip')
            self.parameter = sub.get('params')
            self.init(taskData,sub)

    def init(self,taskData,subtask):
        pwdPath = os.getcwd()
        task_id = taskData.get('id')
        #user = subtask('user')
        #passwd = subtask('password')
        user = "root"
        passwd = "123456"
        filePwd = pwdPath+"/app/service/clinet"
        clinetPwd = "/Users/zbs/code/autoDeploy/src/app/service"
        command = commands.getstatusoutput(pwdPath+"/app/service/addSSH.exp "+self.clinetIp+" "+user+" "+passwd+" "+filePwd+" "+clinetPwd)
        if command and command[1] :
            self.task.update_set({"id":task_id},{"inifLog":command,"message":"初始化成功"})
            self.firstScript(taskData,subtask);
            self.send()
        else:
            self.task.update_set(task_id,{"inifLog":command,"status":"-1","message":"初始化失败"})

    def firstScript(self,data,sub):
        self.processId=data.get("process_id")
        process = self.process.get_process_detail_one_by_id(self.processId).result
        if process.has_key('process') and process.get('process')[0]:
            self.scriptId=process.get('process')[0].get('id')
            scriptDetail = self.script.get_script_by_id(self.scriptId).result
            if scriptDetail and scriptDetail.has_key('script'):
                script = scriptDetail.get('script')
                self.content = script.get('bash_shell')
                self.type = script.get('type')
                self.order = 0
    #构造发送消息
    def send(self):
        myname = socket.getfqdn(socket.gethostname())
        data={}
        data["clinetIp"] =str(self.clinetIp)   #ok
        #data["serviceIp"] = socket.gethostbyname(myname) #ok
        data["serviceIp"] = '127.0.0.1'
        data["serviceHost"] = host  #ok
        data["serviceRoute"] = "/sub_task/call_back" #ok
        data["parameter"] = self.parameter
        data["content"] = self.content   #ok
        data["scriptId"] = self.scriptId  #ok
        data["processId"] = self.processId #ok
        data["type"] = self.type #ok
        data["order"] = self.order
        data["taskId"] = self.task_id
        http = tool.HttpClientByPost(self.clinetIp,9090,"/get/runScript", json.dumps(data))
        http.connect();


