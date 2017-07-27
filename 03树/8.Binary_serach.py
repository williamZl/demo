
def binary_search(alist,item):
    n = len(alist)
    if n == 0:
       return False
    mid = n // 2
    if alist[mid] == item:
        return True
    elif alist[mid] > item:
        return binary_search(alist[:mid],item)
    else:
        return binary_search(alist[mid+1:],item)


if __name__ == '__main__':
    li = [3,5,9,10,20,60]
    print(binary_search(li,600))