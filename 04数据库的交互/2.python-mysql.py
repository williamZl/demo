from pymysql import *


def update():
    # 1.创建连接对象
    # host = None, user = None, password = "",
    # database = None, port = 0, unix_socket = None,
    # charset = '',
    try:
        conn = connect(host='localhost',
                       user='root',
                       password='mysql',
                       database='python_info',
                       port=3306,
                       charset='utf8')
        # 2.获取数据库操作对象
        cur = conn.cursor()
        # 3.编写ｓｑｌ　执行ｓｑｌ语句
        # insert_sql = "insert into classes (name) values ('python11')"
        # delete_sql = "delete from classes where id = 6"
        update_sql = "update classes set name = 'python2222' where id = 10"
        cur.execute(update_sql)
        # 4.python中调用调用ｍｙｓｑｌ默认是开启事务的，如果做数据的更新操作，需要程序员手动提交
        conn.commit()
    except Exception as e:
        print(e)

    finally:
        # 关闭连接
        cur.close()
        conn.close()


def select():
    # 1.创建连接对象
    # host = None, user = None, password = "",
    # database = None, port = 0, unix_socket = None,
    # charset = '',
    try:
        conn = connect(host='localhost',
                       user='root',
                       password='mysql',
                       database='python_info',
                       port=3306,
                       charset='utf8')
        # 2.获取数据库操作对象
        cur = conn.cursor()
        # 3.编写ｓｑｌ　执行ｓｑｌ语句
        select_sql = "select * from classes where id >= 10"
        cur.execute(select_sql)
        # 获取查询的结果
        # fetchon 获取的结构是元祖类型
        # res = cur.fetchall() 嵌套的元祖
        res = cur.fetchall()
        for item in res:
            print(item[0])
            print(item[1])
            print(item[2])
        # print(res)
        # fetchall
        # 4.python中调用调用ｍｙｓｑｌ默认是开启事务的,查询操作不许要提交事务
        # conn.commit()
    except Exception as e:
        print(e)

    finally:
        # 关闭连接
        cur.close()
        conn.close()


def update_params():
    # 1.创建连接对象
    # host = None, user = None, password = "",
    # database = None, port = 0, unix_socket = None,
    # charset = '',
    try:
        conn = connect(host='localhost',
                       user='root',
                       password='mysql',
                       database='python_info',
                       port=3306,
                       charset='utf8')
        # 2.获取数据库操作对象
        cur = conn.cursor()
        # 3.编写ｓｑｌ　执行ｓｑｌ语句
        params = ['python3333']
        insert_sql = "insert into classes (name) values (%s)"
        # delete_sql = "delete from classes where id = 6"
        cur.execute(insert_sql,params)
        # 4.python中调用调用ｍｙｓｑｌ默认是开启事务的，如果做数据的更新操作，需要程序员手动提交
        conn.commit()
    except Exception as e:
        print(e)

    finally:
        # 关闭连接
        cur.close()
        conn.close()
if __name__ == '__main__':
    # update()
    # select()
    update_params()