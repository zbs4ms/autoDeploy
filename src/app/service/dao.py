# -*- coding: utf-8 -*-

from pymongo import MongoClient

class A(object):
    c = 1

class PyConnect(object):

    def __init__(self):
        try:
            self.conn = MongoClient('localhost', 27017)
            self.db = self.conn.autoDeploy
        except:
            print "连接失败"
            exit(0)

    def __del__(self):
        if not self.conn:
            self.conn.close()

    def set_collection(self, collection):
        if not self.db:
            print ("没有连接");
            exit(0)
        else:
            self.coll = self.db[collection]

    def find(self, query={}, field=None):
        try:
            if not field:
                result = self.coll.find(query)
            else:
                result = self.coll.find(query, field)
            return result
        except:
            print "查找出现异常"
            return -1

    def insert(self, data):
        try:
            self.coll.insert(data)
            return 0
        except:
            print "插入出现异常"
            return -1

    def update(self, data, setdata):
        try:
            self.coll.update(data, {'$set': setdata})
            return 0
        except:
            print "更新出现异常"
            return -1

    def remove(self, data):
        try:
            self.coll.remove(data)
            return 0
        except:
            print "删除出现异常"
            return -1


1
if __name__ == "__main__":
    conn = PyConnect()
    conn2= PyConnect()

    print (conn.a)

    print(conn2.a)