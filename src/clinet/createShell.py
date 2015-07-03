#-*- coding: utf-8 -*-

import json
#通过 python 生成 shell

class CreateShell(object):

    def __init__(self,data,shellPathName):
        if  not data and not data.get('content'):
            raise ValueError('传入的参数有为空')
        self.parameter = data.get('parameter')
        self.content = data.get('content').encode("utf-8")
        self.scriptType = data.get('scriptType')
        self.shellName= shellPathName

    def creatShell(self):
        if not self.shellName  or not self.content:
            raise ValueError("无效的参数传入")
        file = readFile(self.shellName ,'w')
        if self.scriptType is 'expect':
            file.write("#!/usr/bin/expect -f")
        else:
            file.write("#!/bin/bash"+"\n")
        dictData=mergeKeys(self.parameter)
        if dictData and len(dictData) > 0:
            for (d,x) in dictData.items():
                file.write(d+"="+x+"\n")
        file.write(self.content)

def mergeKeys(dictA=None,dictB=None):
    keys = dictA
    if not dictB:
        return keys
    else:
        if len(keys) > 0:
            for (d,x) in dictB.items():
                keys[d]=x
        else:
            keys = locals
    return keys

#def writeShell(fileName,globals,locals,content):
#    if not fileName  or not content:
#        raise ValueError("无效的参数传入")
#    file = readFile(fileName,'w')
#    file.write("#!/bin/bash"+"\n")
#    dictData=mergeKeys(globals,locals)
#    if len(dictData) > 0:
#        for (d,x) in dictData.items():
#            file.write(d+"="+x+"\n")
#    file.write(content)

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

if __name__ == '__main__':
    data = {"scriptName":"test","content":"cd /usr/local \nyum jdk \necho 'aaaaa'","parameter":{"street":"科技园路.","city":"江苏苏州","country":"中国"}}
    aa = CreateShell(data,'test.sh')
    aa.creatShell();





