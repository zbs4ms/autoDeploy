__author__ = 'wang'
#-*- coding: utf-8 -*-
from flask import request
from app import app
import json,db_service,tool

#取得正在运行中的任务列表
@app.route('/get/taskList')
def get_taskList():
    db = db_service.Task()
    #tasklist = [{"name":"云平台安装"},{"name":"云平台控制"}];
    return db.get_taskList()

#创建任务
@app.route('/post/create_task', methods=['POST'])
def create_task():
    #TODO
    print(request.json.get('targetList'))
    return json.dumps({"status":0,"message":""})

#根据ID取得执行中的任务信息  status 0=安装中  1=成功 -1=失败
@app.route('/get/task_list/detail/<task_id>')
def get_taskList_info(task_id):
    #TODO
    print(task_id)
    return json.dumps([{"id":"222","ip":"192.0.0.1","status":"0","message":"安装JDK..."},{"id":"123","ip":"192.0.0.2","status":"-1","message":"安装失败"}])

#根据ID取得执行中的任务信息  status 0=安装中  1=成功 -1=失败
@app.route('/get/task/log/<task_id>')
def get_task_log(task_id):
    #TODO
    print(task_id)
    return "123123";

#根据ID取得当前任务需要的变量列表
@app.route('/get/task/params/<task_id>')
def get_task_params(task_id):
    #TODO
    print(task_id)
    return json.dumps([{"name":"user","value":"","description":"用户名称"},{"name":"HOST","value":""}])

#保存任务变量
@app.route('/post/save/taskParams', methods=['POST'])
def save_param():
    #TODO
    print(request.json.get('params'))
    return json.dumps({"status":0,"message":""})

#测试目标机连接
@app.route('/post/test/connection', methods=['POST'])
def test_connection():
    #TODO
    print(request.json.get('target'))
    return json.dumps({"status":0,"message":""})


#取得任务目标机器列表
@app.route('/get/target_list/<task_id>')
def get_target_list(task_id):
    print(task_id)
    return json.dumps(["192.0.0.1","192.0.0.2","192.0.0.3"])

#目标机回调接口
@app.route('/sub_task/call_back', methods=['POST'])
def target_call_back():
    print(request.json.get('data'))
