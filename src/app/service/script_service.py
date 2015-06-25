__author__ = 'wang'
#-*- coding: utf-8 -*-
from flask import request
from app import app
import json
import db_service


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