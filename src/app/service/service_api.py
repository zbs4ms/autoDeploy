#-*- coding: utf-8 -*-
from flask import request
from app import app
import json

#取得正在运行中的任务列表
@app.route('/get/taskList')
def get_taskList():
    #TODO
    tasklist = [{"name":"云平台安装"},{"name":"云平台控制"}];
    return json.dumps(tasklist);

#取得部署流程列表
@app.route('/get/processList')
def get_processList():
    #TODO
    processList = [{"name":"云平台安装","id":"123"},{"name":"云平台控制","id":"321"}];
    return json.dumps(processList);

#取得安装步骤列表
@app.route('/get/processDetail/<id>')
def get_process_detail(id=None):
    #TODO
    list = ["JDK","MySql","检查点"];
    return json.dumps(list);

#删除部署流程,status=0 表示成功 -1表示失败
@app.route('/post/deleteProcess', methods=['POST'])
def del_process():
    #TODO
    print(request.json.get('id'))
    return json.dumps({"status":0,"message":""});

#取得所有安装脚本列表
@app.route('/post/scripts/', methods=['POST'])
def get_scripts(keyword=None):
    #TODO 实现查找功能，如果keyword=null 则表示全部查找
    print(request.json.get('keyword'))
    return json.dumps([{"id":"123","name":"JDK","ver":"1.7"},{"id":"223","name":"JDK","ver":"1.5"}]);