#-*- coding: utf-8 -*-

import json
import time
import random

#数据转json
def getJsonByDict(data):
    return json.dumps(data);

#数据转dict
def getDictByJson(data):
    return json.loads(data)

#mongo find 的类型转dict
def getDictByCursor(data):
    if data.count() <= 0:
        return None;
    array=[];
    for i in data:
        array.append(i)
    return array;

#对象转json
def getJsonByObject(obj):
    d = {}
    d.update(obj.__dict__)
    return json.dumps(d)

#生成唯一ID
def createId():
    t = str(time.time()).replace('.','');
    c = str(random.randint(0, 9999))
    return int(t+c)


class response:
    def __init__(self):
        self.status=0
        self.message=""
        self.result=[]

    def error(self,mesg=None):
        self.status=-1
        self.message=mesg
        return self

    def success(self,result=[]):
        self.status=0
        self.result=result
        return self

    def toJson(self):
        self.result=getDictByCursor(self.result)
        return getJsonByObject(self)