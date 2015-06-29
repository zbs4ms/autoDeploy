# -*- coding: utf-8 -*-
import tool
import socket
import threading
import db_service
import os
import commands
import socket


class callBack(object):
    def __init__(self, data):
        self.data = data
        self.scriptId = data.get("scriptId")
        self.taskId = data.get("")
        self.script = db_service.Scripts;
        self.task = db_service.Task

    # 流程执行
    def execute(self):
        return

    # 保存返回信息入库
    def save(self):
        # 保存
        return False

    # 判断是否成功
    def isSucced(self):
        log = self.data.get("logstr")
        script = self.script.get_script_by_id(self.scriptId).result
        he_kList = script.get('checkList')
        for check in he_kList:
            if check.get('type') is "success":
                success = check
            if check.get('type') is "failure":
                failure = check
        if success.get("keyword") in log:
            return True, success
        if failure.get("keyword") in log:
            return False, failure

    # 下一个需要执行的脚本
    def next(self):
        order = self.data.get('order')
        # task.get_task_one_by_id(self.taskId)

    # 执行脚本
    def send(self):
        return
