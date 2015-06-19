#-*- coding: utf-8 -*-
from flask import request
from app import app
import json
import db_service

#取得正在运行中的任务列表
@app.route('/get/taskList')
def get_taskList():
    #tasklist = [{"name":"云平台安装"},{"name":"云平台控制"}];
    server = db_service.Task()
    tasklist = server.get_taskList()
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
    return json.dump(list)
    #return json.dumps([{"id":"123","name":"JDK","ver":"1.7"},{"id":"223","name":"JDK","ver":"1.5"}]);

#取得所有安装脚本列表
@app.route('/post/save_process', methods=['POST'])
def save_process():
    #TODO
    #print(request.json.get('name'))
    #print(request.json.get('process'))
    server = db_service.Process()
    req = server.save_process(request.json.get('name'),request.json.get('process'))
    return json.dumps({"status":req,"message":""});

#取得所有安装脚本列表
@app.route('/post/del_script', methods=['POST'])
def del_script():
    #TODO
    #print(request.json.get('id'))
    server = db_service.Scripts();
    req = server.del_script(request.json.get('id'))
    return json.dumps({"status":0,"message":""})

#取得所有安装脚本列表
@app.route('/get/script_detail/<id>')
def get_script_by_id(id):
    #TODO
    #print(id)
    #return json.dumps({"name":"JDK","ver":"1.7","description":"xxx","dependents":[{"id":"1","name":"JDK","ver":"1.7"}]});
    server = db_service.Scripts()
    req = server.get_script_by_id(request.json.get('id'))
    return json.dumps({"status":req,"message":""})