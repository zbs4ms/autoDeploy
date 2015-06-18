#-*- coding: utf-8 -*-

import json

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
