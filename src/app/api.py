# -*- coding: utf-8 -*-
import os
import sys
sys.path.append(os.getcwd()+"/service")
from flask import request,Flask
import search_catalog

app = Flask(__name__)

@app.route('/select')
def select_catalog():
    req=search_catalog.findAll();
    return req 

if __name__ == '__main__':
    #调试模式，正式环境请关闭
    app.debug=True
    app.run()
