__author__ = 'wang'
# -*- coding: utf-8 -*-
from flask import request
from app import app
import json, db_service, tool


# 取得部署流程列表
@app.route('/get/processList')
def get_processList():
    db = db_service.Process()
    return db.get_processList()


# 取得指定流程的安装步骤列表
@app.route('/get/processDetail/<id>')
def get_process_detail(id=None):
    try:
        id = int(id)
    except:
        return tool.commonError("id错误")
    db = db_service.Process()
    return db.get_process_detail_by_id(id).toJson()


# 删除部署流程,status=0 表示成功 -1表示失败
@app.route('/post/deleteProcess', methods=['POST'])
def del_process():
    try:
        id = int(request.json.get('id'))
    except:
        return tool.commonError("id错误")
    db = db_service.Process()
    return db.del_process_by_id(id)


# 保存安装流程
@app.route('/post/save_process', methods=['POST'])
def save_process():
    db = db_service.Process()
    data = request.json
    if (data.get('name').strip() == ''):
        return tool.commonError();
    print(data)
    return db.save_process(data)


# 取得安装流程所需的变量列表
@app.route('/get/process/params/<process_id>')
def get_process_params(process_id):
    try:
        id = int(process_id)
    except:
        return tool.commonError("id错误")
    db = db_service.Process()
    #return db.get_process_params(id)
    return json.dumps([{"name": "user", "value": "", "description": "用户名称"}, {"name": "HOST", "value": ""}])

