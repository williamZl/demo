class Node(object):
    def __init__(self,item):
        """节点类"""
        # 存储元素
        self.item = item
        # 指向下一个节点
        self.next = None

class CircleSingleLinkList(object):
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
        if self.is_empty():
            return 0
        # 程序走到这里一定不为空
        count = 0
        cur = self.__head
        while cur.next != self.__head:
            # 一旦不满足调价那就不会执行循环,但是 cur 此时指向的就是尾节点,尾节点不会进入统计
            count +=1
            cur = cur.next
        # 退出循环之后 cur 指向的是尾节点
        return count + 1 # 统计尾节点的个数

    def travel(self):
        """遍历"""
        if self.is_empty():
            return

        cur = self.__head
        while cur.next != self.__head:
            print(cur.item,end=" ")
            cur = cur.next
        # 退出循环之后 cur 指向的就是尾节点
        print(cur.item)
        print("遍历结束")

    def search(self,item):
        """在链表中查找 item 是否存在"""
        if self.is_empty():
            return False

        cur = self.__head
        while cur.next != self.__head:
            if cur.item == item:
                return True
            cur = cur.next
        # 最后一个节点没有判断
        if cur.item == item:
            # 判断最后一个节点的 item 和要查找的元素是否相等
            return True
        # 只要不满足以上所有的判断条件都返回 false
        return False

    def add(self,item):
        """在链表的头部添加元素"""
        # 实例化节点对象
        # 1. 先获取尾节点
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
            return

        # 程序运行至此 链表一定不为空
        rear = self.__head
        while rear.next != self.__head:
            rear = rear.next
        # 退出循环之后此时 rear 指向的就是尾节点

        node.next = self.__head
        self.__head = node
        rear.next = node

    def append(self,item):
        """在链表的尾部添加元素"""
        # 判断链表是否为空
        if self.is_empty():
            self.add(item)
            return

        # 1. 获取尾节点
        rear = self.__head
        while rear.next != self.__head:
            rear = rear.next
        # 退出循环之后 此时 rear 指向的就是尾节点
        node = Node(item)
        rear.next = node
        node.next = self.__head



    def insert(self,pos,item):
        """在指定的位置添加元素"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            # 在中间的某一个位置插入元素
            # 根据 pos 来获取 pos 角标的前一个节点
            count = 0
            cur = self.__head
            while count < (pos - 1):
                count += 1
                cur = cur.next
            # 退出循环之后 cur 指向的就是pos 的前一个角标对应的节点
            # 1.实例化 node 对象
            node = Node(item)
            # 2. 设置 node 的 next属性为 cur.next
            node.next = cur.next
            # 3. 将 cur.next 设置为 node
            cur.next = node

    def remove(self,item):
        """移除链表中的一个 item 元素"""
        if self.is_empty():
            return
        # TODO 1.判断删除首节点 2.判断删除尾节点
        cur = self.__head
        pre = None
        while cur.next != self.__head:
            # 判断 item 是否相等
            if cur.item == item:
                # 判断删除的是否是首节点
                if cur == self.__head:
                    # 先获取尾节点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    # 退出循环之后 rear 就是尾节点
                    self.__head = cur.next
                    # 设置尾节点的下一个节点
                    rear.next = self.__head
                else:
                    # 这个分支在单向链表中就已经包含了尾节点的操作
                    pre.next = cur.next
            # 每次需要设置 cur 等一个 cur 的下一个节点之前就记录 cur
            pre = cur  # 前端节点
            cur = cur.next

        # 退出循环之后 cur 指向的就是尾节点
        if cur.item == item:
            # 删除的元素刚好的就是尾节点
            if pre is not None:
                pre.next = self.__head
            else:
                # 如果只有一个节点
                self.__head = None
            cur.next = None






if __name__ == '__main__':
    single = CircleSingleLinkList()
    print(single.is_empty())    # True
    single.append(4)
    single.remove(4)
    single.travel()
    print("-----------")
    single.add(1)
    single.add(3)
    print(single.is_empty())    # False
    single.travel()             # 3 1 4
    print(single.search(100))   # false
    print(single.search(1))     # ture
    single.append(10)
    single.travel()             # 3 1 4 10
    single.insert(-20,40)       # 40 3 1 4 10
    single.insert(1000,20)      # 40 3 1 4 10 20
    single.insert(2, 50)
    print("--------------")
    single.travel()             # 40 3 50 1 4 10 20
    single.remove(40)
    single.travel()             # 3 50 1 4 10 20
    single.remove(20)
    single.travel()             # 3 50 1 4 10
    single.remove(1)
    single.travel()             # 3 50 4 10


