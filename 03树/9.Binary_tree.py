class Node(object):
    def __init__(self,item):
        # 保存元素
        self.item = item
        # 保存左子树
        self.lchild = None
        # 保存右子树
        self.rchild = None


class BinaryTree(object):
    def __init__(self):
        self.root = None

    def add(self,item):
        n = Node(item)
        if self.root is None:
            self.root = n
            return
        # 队列
        # 根节点入列
        queue = [self.root]
        # 遍历队列 依次处理队列中每个节点
        while len(queue) > 0:
            # 出列
            node = queue.pop(0)
            if node.lchild is None:
                node.lchild = n
                # 退出循环
                return
            else:
                # 让 lchild 入列
                queue.append(node.lchild)

            if node.rchild is None:
                node.rchild = n
                return
            else:
                queue.append(node.rchild)

    def breadth_travel(self):
        """广度优先遍历(从左到右遍历)"""
        if self.root is None:
            return
        queue = [self.root]
        while len(queue) > 0:
            node = queue.pop(0)
            print(node.item,end=" ")
            if node.lchild is not None:
                queue.append(node.lchild)
            if node.rchild is not None:
                queue.append(node.rchild)

    def preorder_travel(self,root):
        """先序遍历 根 左 右"""
        if root is not None:
            print(root.item,end=" ")
            self.preorder_travel(root.lchild)
            self.preorder_travel(root.rchild)


    def inorder_travel(self,root):
        """中序遍历 左 根 右"""
        if root is not None:
            self.inorder_travel(root.lchild)
            print(root.item, end=" ")
            self.inorder_travel(root.rchild)


    def postorder_travel(self,root):
        """后序遍历 左 右 根"""
        if root is not None:
            self.postorder_travel(root.lchild)
            self.postorder_travel(root.rchild)
            print(root.item, end=" ")


if __name__ == '__main__':
    tree = BinaryTree()

    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)

    tree.breadth_travel()

    print("")
    tree.preorder_travel(tree.root)
    print("")
    tree.inorder_travel(tree.root)
    print("")
    tree.postorder_travel(tree.root)
