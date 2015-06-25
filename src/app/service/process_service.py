__author__ = 'wang'
#-*- coding: utf-8 -*-
from flask import request
from app import app
import json
import db_service

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

#保存安装流程
@app.route('/post/save_process', methods=['POST'])
def save_process():
    #print(request.json.get('name'))
    #print(request.json.get('process'))
    server = db_service.Process()
    req = server.save_process(request.json.get('name'),request.json.get('process'))
    return json.dumps({"status":req,"message":""});