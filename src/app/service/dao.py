# -*- coding: utf-8 -*-

from pymongo import MongoClient
from tool import response
from tool import createId


class PyConnect(object):
    def __init__(self, collection):
        try:
            self.conn = MongoClient('localhost', 27017)
            self.db = self.conn.autoDeploy
            self.coll = self.db[collection]
        except Exception as e:
            print e
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
        except Exception as e:
            print e
            return response().error("查找出现异常")

    def find_one(self, query={}, field=None):
        try:
            if not field:
                result = self.coll.find_one(query)
            else:
                result = self.coll.find_one(query, field)
            return response().success(result)
        except Exception as e:
            print e
            return response().error("查找出现异常")

    def insert(self, data):
        try:
            id = createId()
            data['id'] = id
            self.coll.insert(data)
            return response().success({'id': id})
        except Exception as e:
            print e
            return response().error("插入出现异常")

    def update_set(self, data, setdata):
        try:
            self.coll.update(data, {'$set': setdata},False,True)
            return response().success()
        except Exception as e:
            print e
            return response().error("更新出现异常")

    def remove(self, data):
        try:
            self.coll.remove(data)
            return response().success()
        except Exception as e:
            print e
            return response().error("删除出现异常")
