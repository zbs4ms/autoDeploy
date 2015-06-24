#-*- coding: utf-8 -*-
from flask import request
from app import app
import json
import db_service

#取得正在运行中的任务列表
@app.route('/get/taskList')
def get_taskList():
    server = db_service.Task()
    tasklist = server.get_taskList()
    #tasklist = [{"name":"云平台安装"},{"name":"云平台控制"}];
    return json.dumps(tasklist)

#取得部署流程列表
@app.route('/get/processList')
def get_processList():
    #processList = [{"name":"云平台安装","id":"123"},{"name":"云平台控制","id":"321"}];
    server = db_service.Process()
    processList = server.get_processList()
    return json.dumps(processList)

#取得指定流程的安装步骤列表
@app.route('/get/processDetail/<id>')
def get_process_detail(id):
    #list = ["JDK","MySql","检查点"];
    server = db_service.Process()
    list = server.get_process_detail()
    return json.dumps(list)

#删除部署流程,status=0 表示成功 -1表示失败
@app.route('/post/deleteProcess', methods=['POST'])
def del_process():
    #print(request.json.get('id'))
    server = db_service.Process()
    req = server.del_process(request.json.get('id'))
    return json.dumps({"status":req,"message":""});

#根据关键字查找安装脚本列表，如果keyword=null 则表示全部查找
@app.route('/post/search_scripts', methods=['POST'])
def search_scripts():
    #print("keyword="+request.json.get('keyword'))
    server = db_service.Scripts()
    list = server.search_scripts()
    if(list==None):
        return json.dumps([])
    return json.dumps(list)
    #return json.dumps([{"id":"123","name":"JDK","ver":"1.7"},{"id":"223","name":"JDK","ver":"1.5"}]);

#保存安装流程
@app.route('/post/save_process', methods=['POST'])
def save_process():
    #print(request.json.get('name'))
    #print(request.json.get('process'))
    server = db_service.Process()
    req = server.save_process(request.json.get('name'),request.json.get('process'))
    return json.dumps({"status":req,"message":""});

#通过ID删除脚本
@app.route('/post/del_script', methods=['POST'])
def del_script_by_id():
    #print(request.json.get('id'))
    server = db_service.Scripts();
    req = server.del_script(request.json.get('id'))
    return json.dumps({"status":0,"message":""})

#通过Id取得安装脚本的信息
@app.route('/get/script_detail/<id>')
def get_script_by_id(id):
    #print(id)
    #return json.dumps({"name":"JDK","ver":"1.7","description":"xxx","dependents":[{"id":"1","name":"JDK","ver":"1.7"}]});
    server = db_service.Scripts()
    req = server.get_script_by_id(request.json.get('id'))
    return json.dumps({"status":req,"message":""})

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
    return json.dumps([{"name":"user","value":"","scope":"all","description":"用户名称"},{"name":"HOST","value":"","scope":"192.0.0.1"}])

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

#取得测试环境的执行结果
@app.route('/post/test/script', methods=['POST'])
def test_script():
    print(request.json.get('params'))
    return json.dumps(["install","安装成功"])

#保存脚本
@app.route('/post/save/script', methods=['POST'])
def save_script():
    print(request.json.get('name'))
    print(request.json.get('version'))
    print(request.json.get('description'))
    print(request.json.get('script'))
    return json.dumps({"status":0,"message":""})