__author__ = 'wang'
# -*- coding: utf-8 -*-
from flask import request
from app import app
import json, db_service, tool
from data_sender import InitClinet
from callBack import CallBack
from clinet import Clinet

# 取得正在运行中的任务列表
@app.route('/get/taskList')
def get_task_all():
    db = db_service.Task()
    response = db.find(field={'_id': 0, 'id': 1, 'status': 1})
    return response.toJson()


# 取得正在运行中的任务列表
@app.route('/get/running/task')
def get_running_task():
    db = db_service.Task()
    response = db.find({'status': {"$gt": -1}}, {'_id': 0, 'id': 1, 'status': 1})
    return response.toJson()


# 创建任务
@app.route('/post/create_task', methods=['POST'])
def create_task():
    data = request.json
    if data.get('process_id') is None:
        tool.commonError("id 为空")
    db = db_service.Task()
    return db.create_task(data).toJson()


# 更新任务信息
@app.route('/post/execute_task', methods=['POST'])
def save_params_and_execute_task():
    data = request.json
    db = db_service.Task()
    data['status'] = 1
    res = db.update_set({'id': data.get('id')}, data)
    if res.status != -1:
        init = InitClinet(data.get('id'), 0)
        init.start()
    return res.toJson()


# 根据ID取得执行中的任务信息  status  0=等待命令 1=命令执行中 100=全部完成 -1=执行失败
@app.route('/get/subtask/status/<task_id>')
def get_taskList_info(task_id):
    db = db_service.Task()
    try:
        id = int(task_id)
    except:
        return tool.commonError("id错误")
    return db.get_subtask_by_taskId(id).toJson()


# 根据 taskId 和 subtask ip 取得对应的执行日志
@app.route('/post/subtask/log')
def get_task_log():
    #TODO
    task_id = int(request.json.get('task_id'))
    subtask_ip = int(request.json.get('ip'))
    print(task_id)
    return "123123"


# 测试目标机连接
@app.route('/post/test/connection', methods=['POST'])
def test_connection():
    # TODO
    target = (request.json.get('target'))
    data = {"clinetIp": target.get("ip")}
    clinet = Clinet(data)
    if clinet.isConnect():
        return json.dumps({"status": 0, "message": ""})
    else:
        return tool.commonError("目标机无法连接")


# 取得任务信息
@app.route('/get/task/<task_id>')
def get_target_list(task_id):
    if (task_id == None):
        tool.commonError("id 为空")
    db = db_service.Task()
    return db.get_task_by_id(task_id).toJson()


# 目标机回调接口
@app.route('/sub_task/call_back', methods=['POST'])
def target_call_back():
    # 保存本次的执行结果到数据库
    data = json.loads(request.data)
    callBack = CallBack(data)
    callBack.execute()


# 删除task
@app.route('/post/remove_task', methods=['POST'])
def remove_task_by_id():
    try:
        id = int(request.json.get('id'))
    except:
        return tool.commonError("id 为空")
    db = db_service.Task()
    return db.remove({'id': id}).toJson()
