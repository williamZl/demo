# stackoverflow (100%会使用)

class Stack(object):
    def __init__(self):
        """用来存储元素的容器"""
        self.__items = []

    def push(self,item):
        """添加一个新的元素item到栈顶"""
        self.__items.append(item)

    def pop(self):
        """弹出栈顶元素"""
        return self.__items.pop()

    def peek(self):
        """返回栈顶元素"""
        # list index out of range 数组的索引越界
        if self.is_empty():
            return
        return self.__items[-1]

    def is_empty(self):
        """判断栈是否为空"""
        return  self.__items == []

    def length(self):
        """获取栈容器中元素的个数"""
        return len(self.__items)


if __name__ == '__main__':
    stack = Stack()
    stack.peek()
    print(stack.is_empty())
    stack.push(1)
    print(stack.is_empty())
    stack.push(3)
    stack.push(5)

    print(stack.pop())
    print(stack.length())