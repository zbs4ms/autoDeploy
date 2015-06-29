__author__ = 'wang'
# -*- coding: utf-8 -*-
from flask import request
from app import app
import json, db_service, tool, execute
from execute import InitClinet

# 取得正在运行中的任务列表
@app.route('/get/taskList')
def get_taskList():
    db = db_service.Task()
    return db.get_taskList().toJson()


# 创建任务
@app.route('/post/create_task', methods=['POST'])
def create_task():
    data = request.json
    if (data.get('process_id') == None):
        tool.commonError("id 为空")
    db = db_service.Task()
    return db.create_task(data).toJson()


# 更新任务信息
@app.route('/post/execute_task', methods=['POST'])
def update_task():
    data = request.json
    db = db_service.Task()
    res = db.update_pushAll({'id': data.get('id')}, data)
    if (res.status != -1):
        init = InitClinet(data.get('id'))
        init.start()
    return res.toJson()


# 根据ID取得执行中的任务信息  status 0=连接成功  0=等待命令 1=命令执行中 100=全部完成 -1=执行失败
@app.route('/get/task_list/detail/<task_id>')
def get_taskList_info(task_id):
    db = db_service.Task()
    try:
        id = int(task_id)
    except:
        return tool.commonError("id错误")
    return db.get_subtask_by_taskId(id).toJson()


# 根据ID取得执行中的任务信息  status 0=安装中  1=成功 -1=失败
@app.route('/get/task/log/<task_id>')
def get_task_log(task_id):
    # TODO
    print(task_id)
    return "123123"


# 测试目标机连接
@app.route('/post/test/connection', methods=['POST'])
def test_connection():
    # TODO
    print(request.json.get('target'))
    return json.dumps({"status": 0, "message": ""})


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
    # 保存本次的执行结果

    # 查询下一步需要执行的


# 发送到目标机执行
@app.route('/post/execute', methods=['POST'])
def execute():
    execute.run(request.json.get('task_id'))


# 删除task
@app.route('/post/remove_task', methods=['POST'])
def remove_task_by_id():
    try:
        id=int(request.json.get('id'))
    except:
        return tool.commonError("id 为空")
    db = db_service.Task()
    return db.remove({'id':id}).toJson()
