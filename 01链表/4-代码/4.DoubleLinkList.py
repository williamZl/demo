class Node(object):
    def __init__(self,item):
        """节点类"""
        # 存储元素
        self.item = item
        # 指向下一个节点
        self.next = None
        # 指向前端节点
        self.pre = None

class DoubleLinkList(object):
    def __init__(self):
        # 链表的头结点,用来保存链表的第一个元素
        self.__head = None

    def is_empty(self):
        """判断是否为空链表"""
        # if self.__head is None:
        #     return True
        # return False
        return  self.__head is None

    def length(self):
        """长度"""
        count = 0
        cur = self.__head
        while cur is not None:
            count +=1
            cur = cur.next
        return count

    def travel(self):
        """遍历"""
        cur = self.__head
        while cur is not None:
            print(cur.item,end=" ")
            cur = cur.next
        print("遍历结束")

    def search(self,item):
        """在链表中查找 item 是否存在"""
        cur = self.__head
        while cur is not None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

    def add(self,item):
        """在链表的头部添加元素"""
        # 实例化节点对象
        node = Node(item)
        node.next = self.__head
        if self.__head is not None:
            self.__head.pre = node
        self.__head = node

    def append(self,item):
        """在链表的尾部添加元素"""
        # 判断链表是否为空
        if self.is_empty():
            self.add(item)
            return

        # 1. 获取尾节点
        cur = self.__head
        while cur.next is not None:
            cur = cur.next
        # 退出循环之后 此时 cur 指向的就是尾节点
        node = Node(item)
        node.pre = cur
        cur.next = node

    def insert(self,pos,item):
        """在指定的位置添加元素"""
        if pos <= 0:
            self.add(item)
        elif pos > self.length():
            self.append(item)
        else:
            # 在中间的某一个位置插入元素
            # 根据 pos 来获取 pos 角标的前一个节点
            count = 0
            cur = self.__head
            while count < pos:
                count += 1
                cur = cur.next
            # 退出循环之后 cur 指向的就是pos 的前一个角标对应的节点
            # 1.实例化 node 对象
            node = Node(item)
            node.next = cur
            node.pre = cur.pre
            cur.pre.next = node
            cur.pre = node

    def remove(self,item):
        """移除链表中的一个 item 元素"""
        cur = self.__head
        while cur is not None:
            # 判断 item 是否相等
            if cur.item == item:
                # 判断删除的是否是首节点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    # 尾几点的删除也同样在此分支中完成
                    cur.pre.next = cur.next
                    if cur.next is not None:
                        # 为了解决删除尾节点导致崩溃的问题
                        cur.next.pre = cur.pre
            # 每次需要设置 cur 等一个 cur 的下一个节点之前就记录 cur
            # pre = cur  # 前端节点
            cur = cur.next



if __name__ == '__main__':
    single = DoubleLinkList()
    print(single.is_empty())    # True
    single.append(4)
    single.add(1)
    single.add(3)
    print(single.is_empty())    # False
    single.travel()             # 3 1 4
    print(single.search(100))   # False
    print(single.search(1))     # True
    single.append(10)
    single.travel()             # 3 1 4 10
    single.insert(-20,40)
    single.travel()             # 40 3 1 4 10
    single.insert(1000,20)
    single.travel()             # 40 3 1 4 10 20
    single.insert(2, 50)
    print("---------------")
    single.travel()             # 40 3 50 1 4 10 20
    single.remove(40)
    single.travel()             # 3 50 1 4 10 20
    single.remove(20)
    single.travel()             # 3 50 1 4 10
    single.remove(1)
    single.travel()             # 3 50 4 10


