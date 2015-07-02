__author__ = 'wang'
# -*- coding: utf-8 -*-
from flask import request
from app import app
import json, db_service, tool


# 取得部署流程列表
@app.route('/get/processList')
def get_processList():
    db = db_service.Process()
    return db.get_process_list().toJson()


# 取得指定流程的安装步骤列表
@app.route('/get/processDetail/<id>')
def get_process_detail(id=None):
    try:
        id = int(id)
    except:
        return tool.commonError("id错误")
    db = db_service.Process()
    res = db.get_process_detail_by_id(id);
    process_checke(res)
    return res.toJson()


def process_checke(res):
    if res.status != -1:
        for script in res.result['process']:
            db = db_service.Scripts()
            list = []
            if not script.get('id'):
                continue
            if db.get_script_by_id(script['id']).result is None:
                res.status = -1
                list.append(script['name'])
            if len(list) > 0:
                res.message = "脚本" + json.dumps(list) + "已经删除,当前流程不可用。"


# 删除部署流程,status=0 表示成功 -1表示失败
@app.route('/post/deleteProcess', methods=['POST'])
def del_process():
    try:
        id = int(request.json.get('id'))
    except:
        return tool.commonError("id错误")
    db = db_service.Process()
    return db.del_process_by_id(id).toJson()


# 保存安装流程
@app.route('/post/save_process', methods=['POST'])
def save_process():
    db = db_service.Process()
    data = request.json
    if data.get('name').strip() == '':
        return tool.commonError();
    return db.save_process(data).toJson()


# 取得安装流程所需的变量列表
@app.route('/get/process/params/<process_id>')
def get_process_params(process_id):
    try:
        id = int(process_id)
    except:
        return tool.commonError("id错误")
    db = db_service.Process()
    res = db.get_process_detail_by_id(id)
    if res.result is None:
        return tool.commonError("未查找到对应的安装流程信息")
    list = []
    for script in res.result['process']:
        db = db_service.Scripts()
        if script.get('id'):
            script = db.get_script_by_id(script.get('id')).result
            if script is not None:
                if script.get('params'):
                    for p in script.get('params'):
                        list.append({'desc': str(script['name'])+" "+str(script['version']), 'name': p})
            else:
                return tool.commonError("安装脚本数据异常")

    return json.dumps(list)
