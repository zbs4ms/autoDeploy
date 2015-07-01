#-*- coding: utf-8 -*-
import os,commands,json
from flask import request
from flask import Flask
from createShell import CreateShell
from httpClinet import HttpClientByPost


app = Flask(__name__)

@app.route('/')
def test():
    return 'OK'


#取得正在运行中的任务列表
@app.route('/get/runScript',methods=['POST'])
def runScript():
    try:
        req = json.loads(request.data)
        clinetIp = checkKey(req,'clinetIp')
        serviceIp = checkKey(req,'serviceIp')
        serviceHost = checkKey(req,'serviceHost')
        serviceRoute = checkKey(req,'serviceRoute')
        parameter = req.get('parameter')
        content = checkKey(req,'content')
        shellName= str(checkKey(req,'scriptId'))
        processId = checkKey(req,'processId')
        scriptType = checkKey(req,'type')
        order = req.get('order')
        taskId = checkKey(req,'taskId')

        #------初始化路径
        (shellPathName,logPathName)=initFile(processId,shellName,scriptType)

        #------生成脚本
        shell = CreateShell(req,shellPathName)
        shell.creatShell()

        #------执行脚本
        os.system('chmod +x '+shellPathName)
        command = commands.getstatusoutput(shellPathName)

        #------返回执行结果
        http = HttpClientByPost(serviceIp,serviceHost,serviceRoute,clinetIp,processId,shellName,order,taskId)
        if not command or len(command) < 2:
            http.error()
            http.connect()
        else:
            log = command[1]
            http.success(log)
            http.connect()
    except Exception,e:
        http = HttpClientByPost(serviceIp,serviceHost,serviceRoute,clinetIp,processId,shellName,order,taskId)
        http.error("执行出现异常",e.message)
        http.connect()

#检查传入的值是否为空
def checkKey(data,key):
    if not data.get(key):
        raise ValueError("无效的参数传入["+key+"]")
    else:
        return data.get(key)

#文件夹初始化
def initFile(processId,shellName,scriptType):
    if not processId:
        raise ValueError("无效的参数传入[processId]")
    pwdPath = os.getcwd()
    if not os.path.exists(pwdPath+"/script"):
        os.mkdir(pwdPath+"/script")
    if processId and not os.path.exists(pwdPath+"/script/"+processId):
        os.mkdir(pwdPath+"/script/"+processId)
    #不同的脚本类型创建不同的脚本
    if scriptType is 'expect':
        shellPathName = pwdPath+"/script/"+processId+"/"+shellName+".exp"
    else:
        shellPathName = pwdPath+"/script/"+processId+"/"+shellName+".sh"
    logPathName = pwdPath+"/script/"+processId+"/"+shellName+".log"
    return shellPathName,logPathName

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000)