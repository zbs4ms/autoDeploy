#-*- coding: utf-8 -*-
from flask import request
from flask import Flask
import os
import json
import commands
from createShell import CreateShell
from httpClinet import HttpClientByPost

app = Flask(__name__)

#取得正在运行中的任务列表
@app.route('/get/runScript')
def runScript():

    #------传入的内容
    clinetIp = request.json.get('clinetIp')
    serviceIp = request.json.get('serviceIp')
    serviceHost = request.json.get('serviceHost')
    serviceRoute = request.json.get('serviceRoute')
    globals = request.json.get('global')
    locals = request.json.get('local')
    content = request.json.get('content')
    shellName= request.json.get('scriptId')
    processId = request.json.get('processId')

    #------获取当前路径，初始化路径
    pwdPath = os.getcwd()
    initFile(pwdPath,processId)
    shellPathName = pwdPath+"/script/"+processId+"/"+shellName+".sh"
    logPathName = pwdPath+"/script/"+processId+"/"+shellName+".log"
    #------生成脚本
    shell = CreateShell(request.json,shellPathName)
    shell.creatShell()

    #------执行脚本
    os.system('chmod +x '+shellPathName)
    command = commands.getstatusoutput(shellPathName)

    #------返回执行结果
    http = HttpClientByPost(serviceIp,serviceHost,serviceRoute,clinetIp,processId,shellName)
    if not command or len(command) < 2:
        http.error()
        http.connect()
    else:
        log = command[1]
        http.success(log)
        http.connect()


def requestJson(mark,ip,scriptName):
    dictTemp={}
    dictTemp["mark"]=mark
    dictTemp["ip"]=ip
    dictTemp["scriptName"]=scriptName
    return json.dump(dictTemp)

#打开文件
def readFile(fileName,operation=None):
    if not fileName:
        raise ValueError('传入的fileName为空')
    if not operation:
        file = open(fileName)
    else:
        file = open(fileName,operation)
    if not fileName:
        raise  IOError('打开%s文件失败'(fileName))
    return file;


#文件夹初始化
def initFile(pwdPath,processId=None):
    if not os.path.exists(pwdPath+"/script"):
        os.mkdir(pwdPath+"/script")
    if processId and not os.path.exists(pwdPath+"/script/"+processId):
        os.mkdir(pwdPath+"/script/"+processId)


if __name__ == '__main__':
    app.debug = True
    app.run()

#if __name__ == '__main__':
#    data = {"processId":"66666","clinetIp":"192.168.0.263","serviceIp":"192.168.0.133","serviceHost":"50000","serviceRoute":"/clinetRun","scriptName":"test","content":"cd /usr/local \n yum jdk \n echo 'aaaaa'","global":{"street":"科技园路.","city":"江苏苏州","country":"中国"},"local":{"name":"fdafdsa.","password":"123455","country":"美国"}}