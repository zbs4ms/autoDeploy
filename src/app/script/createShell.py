#-*- coding: utf-8 -*-

#通过 python 生成 shell

class CreateShell(object):

    def __init__(self,globalFileName,localFileName,shellFileName,contentFileName):
        if not shellFileName:
            raise ValueError('传入的shell文件名为空')
        self.globalFile = globalFileName
        self.localFile = localFileName
        self.shellFile = shellFileName
        self.contentFile = contentFileName

    def creatShell(self):
        dictData= mergeKeys(self.globalFile,self.localFile)
        writeShell(self.shellFile,dictData,self.contentFile)

def writeShell(fileName,dictData,contentName):
    if not fileName  or not contentName:
        raise ValueError("无效的参数传入")
    file = readFile(fileName,'w')
    file.write("#!/bin/bash"+"\n")
    if len(dictData) > 0:
        for (d,x) in dictData.items():
            file.write(d+"="+x+"\n")
    content = readFile(contentName)
    while True:
        line = content.readline().strip()
        if not line:
            break
        else:
            file.write(line+"\n")

#合并公共参数+私有参数
def mergeKeys(globalFile,localFile):
    if not globalFile and not localFile:
        raise ValueError("无效的参数传入")
    keys = None
    if globalFile:
        keys = get_dict_by_file(globalFile)
    if localFile:
        keys = get_dict_by_file(localFile,dictData=keys)
    return keys

#value字符串要加"" 或者 '' ,数字不用加
def get_dict_by_file(fileName,dictData={}):
    file = readFile(fileName)
    while True:
        line = file.readline().strip()
        if not line:
            break
        else:
            temp = line.split('=')
            if len(temp) == 2:
                dictData[temp[0]]=temp[1]
            else:
                raise  ValueError('传入的keys文件有误')
    if len(dictData) > 0:
        return dictData

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
    aa = CreateShell("global_keys.txt","local_keys.txt","shell.sh","message.txt")
    aa.creatShell();





