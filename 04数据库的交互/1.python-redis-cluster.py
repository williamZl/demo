from rediscluster import *

if __name__ == '__main__':

    startup_nodes = [{'host':'192.168.64.186','port':'7000'},
                     {'host': '192.168.64.186', 'port': '7001'},
                     {'host': '192.168.64.96', 'port': '7003'}]
    cluster = StrictRedisCluster(startup_nodes=startup_nodes,
                                 decode_responses=True)
    cluster.set('name','canjin')
    res = cluster.get('name')
    print(res)