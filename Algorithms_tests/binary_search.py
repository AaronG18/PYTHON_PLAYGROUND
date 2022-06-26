#coding=utf-8
#@Time:2020/10/4 13:24
#@Author:csdn@hijacklei
#@File:二分查找.py
#@Software:PyCharm
'''二分查找作用于顺序表，而且是有序的顺序表'''
# 1、递归思想的二分查找
def binary_search(alist,item):
    n=len(alist)

    if n>0:
        mid = n // 2 #找到中间值
        if alist[mid]==item:
            return True  #证明中间值就是要找的值
        elif alist[mid]<item:
            return binary_search(alist[mid+1:],item)  #在中间值的右侧是目标值，按照递归的思想进行调用函数
        else:
            return binary_search(alist[:mid],item)    #在中间值的左侧是目标值，按照递归的思想进行调用函数
    return False
'''递归思想是划分后的区域新建立的列表进行调用函数的递归思想
非递归思想是在原有的划分的区域继续进行划分'''
# 2、非递归思想的二分查找
def binary_search_1(alist,item):
    '''非递归思想的二分查找'''
    n=len(alist)
    # 定义初始位置的索引
    first=0
    last=n-1
    while first<=last:
        mid=(first+last)//2
        if alist[mid]==item:
            return True
        elif alist[mid]<item:
            first=mid+1
        else:
            last=mid-1
    return False


if __name__ == '__main__':
    li=[17, 20, 26, 31, 44, 54, 55, 77, 93]
    print(binary_search(li,55))
    print(binary_search(li,100))
    print(binary_search_1(li, 77))
    print(binary_search_1(li, 200))
