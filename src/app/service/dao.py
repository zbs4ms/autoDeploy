# -*- coding: utf-8 -*-

from pymongo import MongoClient
from tool import response
from tool import createId


class PyConnect(object):
    def __init__(self,collection):
        try:
            self.conn = MongoClient('localhost', 27017)
            self.db = self.conn.autoDeploy
            self.coll = self.db[collection]
        except:
            print "连接失败"
            exit(0)

    def __del__(self):
        print "exit dao"
        if not self.conn:
            self.conn.close()

    def find(self, query={}, field=None):
        try:
            if not field:
                result = self.coll.find(query)
            else:
                result = self.coll.find(query, field)
            return response().success(result)
        except:
            return response().error("查找出现异常")

    def insert(self, data):
        try:
            data[id] = createId()
            self.coll.insert(data)
            return response().success()
        except:
            return response().error("插入出现异常")

    def update(self, data, setdata):
        try:
            self.coll.update(data, {'$set': setdata})
            return response().success()
        except:
            return response().error("更新出现异常")

    def remove(self, data):
        try:
            self.coll.remove(data)
            return response().success()
        except:
            return response().error("删除出现异常")
