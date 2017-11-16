from pymysql import *
from hashlib import *
from pymongo import *
from redis import *


def register():
    """注册"""
    try:
        conn = mysql_conn()
        cur = conn.cursor()
        # 先执行　ｓｅｌｅｃｔ
        select_params = [username]
        select_sql = 'select upwd from py_users where uname=%s'
        cur.execute(select_sql, select_params)
        res = cur.fetchone()
        if res is not None:
            print('注册失败，用户名已经存在')
            return
            # 程序运行至此　用户名字一定不存在　注册
        insert_params = [username, sha_pwd]
        insert_sql = 'insert into py_users (uname,upwd) values (%s,%s)'
        count = cur.execute(insert_sql, insert_params)
        if count == 1:
            print('注成功')
            # 插入数据更新数据的操作　　应该手动提交数据
            conn.commit()
        else:
            print('注册失败')

    except Exception as e:
        print(e)

    finally:
        close(conn)

def mysql_login():
    """登录"""
    try:
        # 根据用户名查找密码　
        conn = mysql_conn()
        cur = conn.cursor()
        params = [username]
        select_sql = 'select upwd from py_users where uname=%s'
        cur.execute(select_sql,params)
        res = cur.fetchone()
        # 没有查找到密码　用户错误
        if res is None:
            print('登录失败，用户名错误,数据来自于ｍｓｑｌ')
            return
        # 查找到密码　用户名正确　但是需要校验密码
        # 比较密文密码　如果相同登录成功　否则就登陆失败　
        pwd = res[0]
        if pwd == sha_pwd:
            print('密码正确，登录成功，ｍｙｓｑｌ')
            # 将用户的数据按照之前约定的格式写入到ｍｏｎｇｏ
            # col.insert_one({'name':username,'password':sha_pwd})
            # 将用户数据写入到ｒｅｄｉｓ　ｕｓｅｒｎａｍｅ：ｓｈａ_ｐｗｄ
            redis_client.set(username,sha_pwd)
        else:
            print('密码错误，登陆失败，ｍｙｓｑｌ')

    except Exception as e:
        print(e)

    finally:
        close(conn)




def mysql_conn():
    """获取连接对象"""
    # host = None, user = None, password = "",
    # database = None, port = 0, unix_socket = None,
    # charset = ''
    return connect(host='localhost',
                   user='root',
                   password='mysql',
                   database='python_info',
                   port=3306,
                   charset='utf8')

def mongo_login():
    # 在ｍｏｎｇｏｄｂ中查找数据 {name:xxx,password:xxxx}
    # find_one 只需要对结果判断是否为Ｎｏｎｅ
    # 返回的数据是一个ｃｕｒｓｏｒ类型的对象　不能判断是否为空
    cur = col.find({'name': username})
    # 获取ｃｕｒｓｏｒ类型的对象结果的数量
    count = cur.count()
    if count == 0:
        # 没有找到数据　调用ｍｙｓｑｌ的登陆
        mysql_login()
    else:
        # 找到数据
        item = cur[0]
        # ｉｔｅｍ就是字典对象
        print(item)
        if item['password'] == sha_pwd:
            print('登陆成功，数据来源于ｍｏｎｇｏ')
        else:
            print('登陆失败，数据来源与ｍｏｎｇｏ')

def close(con):
    """关闭连接和数据库操作对象"""
    con.cursor().close()
    con.close()



if __name__ == '__main__':

    # 获取用户名和密码
    username = input('请输入用户名：')
    password = input('请输入密码：')
    # m = hashlib.md5()
    # >> > m.update(b"Nobody inspects")
    # >> > m.update(b" the spammish repetition")
    # >> > m.digest()
    s1 = sha1()
    s1.update(password.encode())
    sha_pwd = s1.hexdigest()
    print(sha_pwd)
    # 先去ｍｏｎｇｏｄｂ中根据用户名查找密码
    mongoclient = MongoClient(host='localhost',
                              port=27017)
    db = mongoclient.flowerfiled
    col = db.f_users


    # redis缓存的使用
    redis_client = StrictRedis(host='192.168.64.186')
    # 预先定义ｒｅｄｉｓ中用户名和密码如何存储　ｓｔｒｉｎｇ：　username：sha_pwd
    r_pwd = redis_client.get(username).decode()
    # 先判断密码是否为空
    # 密码为空　在ｒｅｄｉｓ就没有数据　需要从ｍｙｓｑｌ中登陆
    if r_pwd is None:
        mysql_login()
    else:
        print(r_pwd)
        if r_pwd == sha_pwd:
            print('登陆成功，ｒｅｉｄｓ')
        else:
            print('登陆失败，ｒｅｄｉｓ')
    #register()
    # login()


