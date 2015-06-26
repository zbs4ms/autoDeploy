#-*- coding: utf-8 -*-
import httplib
import json

class HttpClientByPost(object):
    def __init__(self,ip,host,path,clinetIp,processId,scriptId):
        self.ip = ip
        self.host = host
        self.path = path
        self.data={"clinetIp":clinetIp,"processId":processId,"scriptId":scriptId}

    def error(self,message,log):
        self.reqJson("错误信息缺失",log,-1)
        if(log == None):
            self.reqJson("没有返回日志","",-1)
        if(message != None ):
            self.reqJson(message,log,-1)

    def success(self,log):
        self.reqJson ("执行成功",log,0)

    def reqJson(self,message,logstr,status):
        self.data["message"] = message
        self.data["logstr"] = logstr
        self.data["status"] = status

    def connect(self):
        try:
            content = {"data":json.dumps(self.data)}
            httpClient = httplib.HTTPConnection(self.ip,self.host,timeout=30)
            httpClient.request('POST',self.path,content)
        except Exception, e:
            print e
        finally:
            if httpClient:
                httpClient.close()

if __name__ == '__main__':
    h = HttpClientByGet("0.0.0.0","9090","/fda/fdas","1.1.1.1","2222","3333")
    h.success("fdafsfsafdsafadfda")
    h.connect()
