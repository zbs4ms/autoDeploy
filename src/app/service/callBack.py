# -*- coding: utf-8 -*-
from clinet import Clinet
import socket
import db_service
import os, tool


class CallBack(object):
    def __init__(self, data):
        self.data = data
        myname = socket.getfqdn(socket.gethostname())
        self.serviceIp = socket.gethostbyname(myname);
        self.serviceHost = 5000
        self.serviceRoute = "/sub_task/call_back"
        # 初始化些数据库
        self.task = db_service.Task()
        self.process = db_service.Process()
        self.script = db_service.Scripts()

    # 流程执行
    def execute(self):
        try:
            print "保存返回的数据"
            self.saveLog()
            print "判断是否能继续执行"
            (isSucced, check) = self.isSucced()
            if isSucced:
                self.nextScript()
            else:
                print "执行完毕"
        except Exception, e:
            return tool.commonError(e.message)

    def finished(self):
        print ""

    # 保存返回信息入库
    def saveLog(self):
        # 1.检查参数
        isNotEmptyKey = ["logstr", "taskId"]
        isEmptyKey = ["order"]
        self.checkParameter(isNotEmptyKey)
        # 2.从数据库中查出task
        task = self.task.get_task_by_id(self.data.get("taskId")).result
        if task and task.get('subtask'):
            subTaskList = task.get("subtask")
            for s in subTaskList:
                if s.get("ip") in self.data.get("clinetIp"):
                    subtask = s
            if not subtask:
                raise ValueError("数据库task中的值有异常")
            # subtask = subTaskList[self.data.get("order")]
            if not isinstance(subtask.get("log"), list):
                subtask["log"] = []
            subtask["log"].append(self.data.get("logstr"))
            self.task.update_set({"id": int(self.data.get("taskId"))}, {"subtask": subTaskList})
        else:
            raise ValueError("task数据库中的值不完善")

    # 判断是否成功，只支持success和failure
    def isSucced(self):
        # 1.检查参数
        isNotEmptyKey = ["logstr"]
        isEmptyKey = []
        self.checkParameter(isNotEmptyKey)
        # 2.从数据库中拿值做对比
        script = self.script.get_script_by_id(int(self.data.get("scriptId"))).result
        if not script:
            raise ValueError("没有从数据库中找到scriptId 为" + self.data.get("scriptId") + "的值")
        checkList = script.get('checkList')
        for check in checkList:
            if check.get('type') in "success":
                success = check
            if check.get('type') in "failure":
                failure = check
        if success and success.get("keyword") in self.data.get("logstr"):
            return True, success
        if failure and failure.get("keyword") in self.data.get("logstr"):
            return False, failure
        return False, "没有找到相关判断信息"

    def nextScript(self):
        # 1.检查参数
        isNotEmptyKey = ["taskId", "clinetIp"]
        isEmptyKey = ["order"]
        self.checkParameter(isNotEmptyKey)
        (taskData, process, script) = self.findDataByDatabase(int(self.data.get('taskId')),
                                                              int(self.data.get("order")) + 1)
        if not taskData and not process and not script:
            return None;
        if not taskData or not process or not script:
            raise ValueError("无效的参数传递")
        scriptCommand = script.get("script")
        sub = taskData.get('subtask')
        for s in sub:
            if s.get("ip") in self.data.get("clinetIp"):
                sub = s;
        if not sub:
            raise ValueError("没有找到ip为" + self.data.get("clinetIp") + "的数据")
        data = {}
        data["serviceIp"] = self.serviceIp
        data["serviceHost"] = self.serviceHost
        data["serviceRoute"] = self.serviceRoute
        data["order"] = int(self.data.get("order")) + 1
        data["taskId"] = self.data.get("taskId")
        data["content"] = scriptCommand.get("bash_shell")
        data["scriptId"] = script.get("id")
        data["processId"] = taskData.get("process_id")
        data["type"] = scriptCommand.get("type")
        data["clinetIp"] = self.data.get('clinetIp')
        data["parameter"] = sub.get('params')
        data["user"] = sub.get("user")
        data["passwd"] = sub.get("password")
        #data["clinetPath"]="/usr/local"
        data["clinetPath"] = os.getcwd()
        data["servicePath"] = os.getcwd() + "/clinet"
        clinet = Clinet(data)
        (mark, log) = clinet.execute(send=True)
        if not mark:
            print log

    def findDataByDatabase(self, task_id, order):
        taskData = self.task.get_task_by_id(task_id).result
        if taskData.get("process_id") and taskData.get("subtask"):
            processDetail = self.process.get_process_detail_by_id(taskData.get("process_id")).result
            if processDetail.get('process'):
                if order < len(processDetail.get('process')):
                    scriptId = processDetail.get('process')[order].get('id')
                    script = self.script.get_script_by_id(scriptId).result
                    return taskData, processDetail, script
                else:
                    return None, None, None
            else:
                raise ValueError("process 数据库数据不完整")
        else:
            raise ValueError("task 数据库数据不完整")

    # 检查点的校验
    def checkContent(self):
        print ""

    # 校验需要传递的参数
    def checkParameter(self, isNotEmptyKey):
        # 1、校验不为空
        if not self.data:
            raise ValueError("传入的参数为空")
        # 2、校验类型是否为dict
        if not type(self.data) is dict:
            raise ValueError("传入的参数不是dict类型")
        for key in isNotEmptyKey:
            self.isEmpty(key)

    # 校验传递的参数是否为空，为0
    def isEmpty(self, key):
        if not self.data.get(key):
            raise ValueError("无效的参数传入[" + key + "]")
