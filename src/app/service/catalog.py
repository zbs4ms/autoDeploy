#-*- coding: utf-8 -*-

import connection
import json

#查找全部
def findAll():
    try:
        catalog=connection.db.catalog;
        list=catalog.find()
        if not list:
            return nil
        else:
            array=[]
            for i in list:
                i.pop("_id")
                array.append(i);
            return json.dumps({"catalog":array});                    
    except Exception,e:
        print "异常",e;
        return -1;

#查找一个根据ID
def findOneById(id):
    try:
        catalog=connection.db.catalog;
        data=catalog.find_one({"id":id})
        if not data:
            return nil
        else:
            data.pop("_id")
            return json.dumps(data)
    except Exception,e:
        print "异常",e
        return -1    

#新增
def addOne(dictData):
    try:
        id=dictData["id"]
        name=dictData["name"]
        process=dictData["process"]
        if not id or not name or not process:
            raise Exception("信息不完整");
        else:
            catalog=connection.db.catalog;
            data={"id":id,"name":name,"process":process}
            catalog.save(data);
            return 1;            
    except Exception,e:
        print "异常",e
        return -1

#删除
def remove(id):
    try:
        if not id:
            return nil
        else:
            catalog=connection.db.catalog;
            catalog.remove({"id":id})
            return 1;
    except Exception,e:
        print "异常",e
        return -1

#修改
def update(dictData):
    try:
        id=dictData["id"]
        name=dictData["name"]
        process=dictData["process"]
        if not id or not name or not process:
            raise Exception("信息不完整");
        else:
            catalog=connection.db.catalog;
            data={"id":id,"name":name,"process":process}
            catalog.update({"id":id},{'$set':data},upsert=False,multi=True);
            return 1;            
    except Exception,e:
        print "异常",e
        return -1

if __name__=='__main__':
    aa={};
    aa['id']=44
    aa["name"]="zzzzz"
    aa["process"]="{fsfds}"
    #print addOne(aa);
    print findAll();
    print remove(44)
    aa["name"]="ddddd"
    aa["id"]=55
    print update(aa)
    print findAll();
