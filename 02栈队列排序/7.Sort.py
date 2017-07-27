def buddle_sort(alist):
    """冒泡排序"""
    # 排序算法: 先控制下标(i)的变化,再控制比较次数(j)
    n = len(alist)
    # j 是排序的次数  G
    for j in range(n - 1):
        # 在循环遍历之前添加一个标记
        exchange = False
        # 先控制索引的变化  i
        # 从0 开始 每次都会少比较一个
        for i in range(0,n - j - 1):
            # 比较 i 和 i+1 对应的元素的大小
            if alist[i] >= alist[i+1]:
                # 交换两个元素
                alist[i],alist[i+1] = alist[i+1],alist[i]
                exchange = True

        if exchange is False:
            # 没有交换  冒泡排序就可以终止
            break



def select_sort(alist):
    """选择排序"""
    print("选择排序")
    n = len(alist)
    # 2. 需要遍历几次
    for j in range(n - 1):
         # 1. 确定角标 i 的变化
        min_index = j
        for i in range(1+j,n):
            if alist[min_index] > alist[i]:
                min_index = i
        # 退出循环之后 min_index 指向的就一定最小值
        # 交换
        if min_index != j:
            alist[min_index],alist[j] = alist[j],alist[min_index]


def insert_sort(alist):
    """插入排序"""
    print("插入排序")
    n = len(alist)
    # 先确定索引的变化 从1 开始 每次递增
    # 确定比较的次数 n - 1
    for j in range(1,n):
        for i in range(j,0,-1):  # j
            # 比较
            if alist[i] < alist[i-1]:
                #  交换
                alist[i],alist[i-1] = alist[i-1],alist[i]
            else:
                break

def shell_sort(alist):
    n = len(alist)

    # 控制 gap
    gap = n // 2
    while gap >= 1:
        # 比较
        # 控制比较的索引
        for i in range(gap, n):   # gap ~ n 一次循环 就能够将所有的子序列都比较一遍
            # 向后比较多次
            while (i - gap) >= 0:
                if alist[i] < alist[i - gap]:
                    #  交换
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
                    # 元素交换完毕之后 i 的值需要变化吗? 递减 i
                    i = i - gap
                else:
                    break

        gap = gap // 2



def quick_sort(alist,start,end):
    # start 起始索引
    # end 就是结束的索引
    if start >= end:
        # 递归结束的条件
        return
    n = len(alist)
    left = start
    right = end
    base_value = alist[left]

    # 让 alist[right] 和 basevalue
    while left < right:
        #  = 如果基准值一旦重复 就将和基准值相同的元素放在基准值的右边
        while left < right and alist[right] >= base_value:
            # 移动 right 游标
            right -= 1
        # 退出循环之后 交换左右角标对应的值
        alist[left] = alist[right]
        while left < right and alist[left] < base_value:
            left += 1
        # 退出循环之后 交换
        alist[right] = alist[left]
    # 循环退出的时候 left 和 right 相等
    alist[left] = base_value

    # alist[:left] 会得到一个新的列表
    # 对于中间值的左半部分排序
    quick_sort(alist,start,left-1)
    # 对于中间值的右半部分排序
    quick_sort(alist,left+1,end)




if __name__ == '__main__':
    li = [54,26,93,17,77,31,44,55,20]
    # buddle_sort(li)
    # select_sort(li)
    # insert_sort(li)
    # shell_sort(li)
    quick_sort(li,0,len(li)-1)
    print(li)