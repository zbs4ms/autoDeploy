# -*- coding: utf-8 -*-
import tool
import socket
import threading
import db_service
import os
import commands
import socket

class callBack(object):
    def __init__(self,data):
        self.data = data
        self.ip = data.get("clinetIp")
        self.scriptId = data.get("scriptId")
        self.taskId = data.get("")
        self.script = db_service.Scripts;
        self.task = db_service.Task

    #流程执行
    def execute(self):


    #保存返回信息入库
    def save(self):
        #保存
        log = self.data.get("logstr")
        order = self.data.get('order')
        task=self.task.get_task_one_by_id(self.taskId).result
        if task and task.get('subtask'):
            subtask = task.get('subtask')
            sub = subtask[order]
            task.update({"id":self.taskId,"subtask.ip":self.ip},"$inc")

    #判断是否成功
    def isSucced(self):
        log = self.data.get("logstr")
        script = self.script.get_script_by_id(self.scriptId).result
        checkList = script.get('checkList')
        for check in checkList:
            if check.get('type') is "success":
                success = check
            if check.get('type') is "failure":
                failure=check
        if success.get("keyword") in log:
            return True,success
        if failure.get("keyword") in log:
            return False,failure

    #下一个需要执行的脚本
    def next(self):
        order = self.data.get('order')
        task=self.task.get_task_one_by_id(self.taskId).result
        if task and task.get('subtask'):
            subtask = task.get('subtask')
            nextOrder=order+1
            if len(subtask) < nextOrder:
                return subtask[nextOrder]

    #执行脚本
    def send(self):