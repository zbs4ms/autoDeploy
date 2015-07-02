# -*- coding: utf-8 -*-
import httplib,json,tool,os,commands,socket,subprocess


clinetHost= 9090

class Clinet(object):
    def __init__(self,data):
        #传递过来的值
        self.data = data

    def execute(self,addSSH=False,init=False,copyFile=False,runClinet=False,send=False):
        log=[]
        try:
            if addSSH:
                log.append(self.addSSH())
            if init:
                log.append(self.initInstall())
            if copyFile:
                log.append(self.copyFileToClinet())
            if runClinet:
                log.append(self.runClinet())
            if send:
                self.send()
            return True,log
        except Exception,e:
            return False,tool.commonError(e.message)

    #发送消息到cline端 no return
    def send(self):
        #-----1.对参数进行校验-----
        #  设置不能为空的值的key的名字
        isNotEmptyKey=["clinetIp","serviceIp","serviceHost","serviceRoute","content","scriptId","processId","type","taskId"]
        #  设置可以为空的key的名字
        isEmptyKey=["parameter","order"]
        self.checkParameter(isNotEmptyKey)
        #-----2.发送http请求-----
        clinetPath="/get/runScript"
        http = HttpClientByPost(self.data.get("clinetIp"),clinetHost,clinetPath, json.dumps(self.data))
        http.connect();

    #安装ssh信任
    def addSSH(self):
        command = commands.getstatusoutput(os.getcwd()+"/shell/addSSH.sh")
        return command[1]

    #在clinet端安装软件
    def initInstall(self):
        #1.检验传递过来的参数
        #  设置不能为空的值的key的名字
        isNotEmptyKey=["clinetIp","user","passwd"]
        #  设置可以为空的key的名字
        self.isEmptyKey=[]
        self.checkParameter(isNotEmptyKey)
        command = commands.getstatusoutput(os.getcwd()+"/shell/initClinet.sh "+self.data.get("clinetIp")+" "+self.data.get("user")+" "+self.data.get("passwd"))
        return command[1]

    #拷贝文件到clinet端
    def copyFileToClinet(self):
        #1.检验传递过来的参数
        #  设置不能为空的值的key的名字
        isNotEmptyKey=["clinetIp","user","passwd","clinetPath","servicePath"]
        #  设置可以为空的key的名字
        self.isEmptyKey=[]
        self.checkParameter(isNotEmptyKey)
        #2.拷贝文件到clinet
        command = commands.getstatusoutput(os.getcwd()+"/shell/copyFile.sh "+self.data.get("clinetIp")+" "+self.data.get("user")+" "+self.data.get("passwd")+" "+self.data.get("clinetPath")+" "+self.data.get("servicePath"))
        return command[1]

    #启动Clinet客户端
    def runClinet(self):
        #1.检验传递过来的参数
        #  设置不能为空的值的key的名字
        isNotEmptyKey=["clinetIp","user","passwd","clinetPath"]
        #  设置可以为空的key的名字
        self.isEmptyKey=[]
        self.checkParameter(isNotEmptyKey)
        if not self.isHostOpen(self.data.get("clinetIp"),5000):
        #运行脚本
            command = commands.getstatusoutput(os.getcwd()+"/shell/runClinet.sh "+self.data.get("clinetIp")+" "+self.data.get("user")+" "+self.data.get("passwd")+" "+self.data.get("clinetPath"))
            return command[1]
        else:
            return "已经启动"

    #校验服务器是否能拼的通
    def isConnect(self):
        #1.检验传递过来的参数
        #  设置不能为空的值的key的名字
        isNotEmptyKey=["clinetIp"]
        #  设置可以为空的key的名字
        self.isEmptyKey=[]
        self.checkParameter(isNotEmptyKey)
        command = commands.getstatusoutput(os.getcwd()+"/shell/isConnect.sh "+self.data.get("clinetIp"))
        print command[1]
        if command and len(command)==2 and command[1] is "0":
            return True
        else:
            return False

    #判断端口是否打开
    def isHostOpen(self,ip,port):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            s.connect((ip,int(port)))
            s.shutdown(2)
            return True
        except:
            return False

    #校验需要传递的参数
    def checkParameter(self,isNotEmptyKey):
        #1、校验不为空
        if not self.data:
            raise ValueError("传入的参数为空")
        #2、校验类型是否为dict
        if not type(self.data) is dict:
            raise ValueError("传入的参数不是dict类型")
        for key in isNotEmptyKey:
            self.isEmpty(key)

    #校验传递的参数是否为空，为0
    def isEmpty(self,key):
        if not self.data.get(key):
            raise ValueError("无效的参数传入["+key+"]")

#发送http请求
class HttpClientByPost(object):
        def __init__(self,ip,host,path,data):
            self.data = data
            self.ip = ip
            self.path = path
            self.host = host

        def connect(self):
            try:
                httpClient = httplib.HTTPConnection(self.ip,self.host,timeout=30)
                httpClient.request('POST',self.path,self.data)
            finally:
                if httpClient:
                    httpClient.close()

