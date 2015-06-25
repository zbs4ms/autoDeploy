__author__ = 'wang'
# -*- coding: utf-8 -*-
from flask import request
from app import app
import json
import db_service



# 根据关键字查找安装脚本列表，如果keyword=null 则表示全部查找
@app.route('/post/search_scripts', methods=['POST'])
def search_scripts():
    db = db_service.Scripts()
    keyword = request.json.get('keyword')
    if(keyword!=None and keyword.strip()==''):
            keyword = None
    return db.search_scripts_by_name(keyword)
    # return json.dumps([{"id":"123","name":"JDK","ver":"1.7"},{"id":"223","name":"JDK","ver":"1.5"}]);


# 通过ID删除脚本
@app.route('/post/del_script', methods=['POST'])
def del_script_by_id():
    # print(request.json.get('id'))
    db = db_service.Scripts();
    return db.del_script_by_id(request.json.get('id'))


# 通过Id取得安装脚本的信息
@app.route('/get/script_detail/<id>')
def get_script_by_id(id):
    # print(id)
    # return json.dumps({"name":"JDK","ver":"1.7","description":"xxx","dependents":[{"id":"1","name":"JDK","ver":"1.7"}]});
    server = db_service.Scripts()
    req = server.get_script_by_id(request.json.get('id'))
    return json.dumps({"status": req, "message": ""})


# 取得测试环境的执行结果
@app.route('/post/test/script', methods=['POST'])
def test_script():
    print(request.json.get('params'))
    return json.dumps(["install", "安装成功"])


# 保存脚本
@app.route('/post/save/script', methods=['POST'])
def save_script():
    print(request.json)
    script = db_service.Scripts()
    data = request.json
    if(data.get('name').strip()=='' or data.get('version').strip()==''):
        return json.dumps({"status": -1, "message": "关键数据缺失,不能保存"})
    return script.insert(data)
