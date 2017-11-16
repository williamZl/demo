from pymongo import *


def insert():
    """插入数据"""
    try:
        # 1. 创建连接对象
        client = MongoClient(host='localhost',
                             port=27017)
        # 2.　获取数据库对象
        db = client.py_mongo
        # 3.　获取集合对象
        col = db.infos
        # 　插入多条数据
        col.insert([{'name': 'zhangsan', 'age': 18},
                    {'book': '北冥神功', 'star': 5},
                    {'name': '如来神掌', 'price': 9.9}])
    except Exception as e:
        print(e)


def select():
    """查询数据"""
    try:
        # 1. 创建连接对象
        client = MongoClient(host='localhost',
                             port=27017)
        # 2.　获取数据库对象
        db = client.py_mongo
        # 3.　获取集合对象
        col = db.infos
        # 　查询
        # find_one() 返回的结果类型是字典
        res = col.find()  # 返回的是ｃｕｒｓｏｒ对象
        # res = col.find_one()
        # print(res)
        for item in res:
            print(item)
            print(item['name'])
            print(item['age'])
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # insert()
    select()