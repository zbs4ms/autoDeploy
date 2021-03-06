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

    def test(self,data,setdata):
        self.coll.find_one_and_update(data,{'$push':setdata})


if __name__ == "__main__":
    task = PyConnect("task")
    data={'id':143574146422672}
    setdata={'subtask.log':"aaaa"}
    #setdata={'status':"aaaa"}
    #findData = {"subtask.ip":"192.168.0.236"}
    #task.test(data,setdata)
    # aa = task.find_one(findData)

    #add ={'subtask':[{"ip":"1.1.1.1","log":["aa","bb","cc"],"name":"zzzbbbsss"},{'subtask':{"ip":"2.2.2.2","log":["aa","bb","cc"],"name":"zzzbbbsss"}}]}

    #task.update_set(data,add)

    #find = {"subtask":"1.1.1.1"}

    find = task.find_one(data).result
    sub = find.get("subtask")
    print sub

    updata={'subtask':sub}
    bbb = task.update_set({'id':143574146422672},{"subtask":["nimabi"]})
    #aa =task.find_one(find)
   # print aa


