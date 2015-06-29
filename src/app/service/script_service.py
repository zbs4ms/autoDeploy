__author__ = 'wang'
# -*- coding: utf-8 -*-
from flask import request
from app import app
import json, db_service, tool, re



# 根据关键字查找安装脚本列表，如果keyword=null 则表示全部查找
@app.route('/post/search_scripts', methods=['POST'])
def search_scripts():
    db = db_service.Scripts()
    keyword = request.json.get('keyword')
    if (keyword != None and keyword.strip() == ''):
        keyword = None
    return db.search_scripts_by_name(keyword)
    # return json.dumps([{"id":"123","name":"JDK","ver":"1.7"},{"id":"223","name":"JDK","ver":"1.5"}]);


# 通过ID删除脚本
@app.route('/post/del_script', methods=['POST'])
def del_script_by_id():
    try:
        id = int(request.json.get('id'))
    except:
        return tool.commonError("id 错误")
    db = db_service.Scripts();
    return db.del_script_by_id(id)


# 通过Id取得安装脚本的信息
@app.route('/get/script_detail/<script_id>')
def get_script_by_id(script_id):
    try:
        id = int(script_id)
    except:
        return tool.commonError("id 错误")
    db = db_service.Scripts()
    return db.get_script_by_id(id).toJson()


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
    if (data.get('name').strip() == '' or data.get('version').strip() == ''):
        return tool.commonError();
    params = analysis_param(data.get('script').get('bash_shell'));
    if (params != None):
        data['params'] = params
    return script.save_script(data)


def analysis_param(src):
    if (src == None):
        return None
    p = re.findall(r'\$(\w+)', src)
    if p:
        return p
    return None
