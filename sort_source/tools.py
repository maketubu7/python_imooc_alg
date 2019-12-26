# -*- coding: utf-8 -*-
# @Time    : 2019/9/19 20:09
# @Author  : Deng Wenxing
# @Email   : dengwenxingae86@163.com
# @File    : tools.py
# @Software: PyCharm
import sys
import numpy as np
from math import floor, log, exp
import data_source
import random

if sys.version_info[0] == 2:
    reload(sys)
    sys.setdefaultencoding("utf-8")
    sys.setrecursionlimit(100000)


def swap(arr,j, k):
    arr[j], arr[k] = arr[k], arr[j]

def get_logspace(n):
    mi = int(floor(log(n,2)))
    d = [int(i) for i in np.logspace(0, mi, mi+1, base=2)]
    # if d[-1] < n:
    #     d.append(n)
    return d

def last_sort(arr):
    n = len(arr)
    for i in range(1, n):
        # 每一个元素都和自己的前一个元素比较
        tmp = arr[i]
        minIndex = i
        for j in range(i, 0, -1):
            if tmp < arr[j - 1]:
                arr[j] = arr[j - 1]
                minIndex = j - 1
            if tmp > arr[j - 1]:
                break
        arr[minIndex] = tmp
    return arr


def find_reverse_tuple(arr):
    ''' 找数组中逆序对的个数 '''
    num = 0
    if len(arr) == 1:
        return 0
    sorted_arr = sorted(arr)
    for item in sorted_arr:
        count = arr.index(item)
        num += count
        arr.remove(item)
    return num



def find_nmax_number(arr,n):
    ''' 找到数组中第N大的数值 '''

    def partition(arr, left, right):
        pivot_index = random.randint(left, right)
        pivot = arr[pivot_index]

        # 首先将目标值和最后的一个值互换，不会和自己进行比较进行，先把给定值放在最后
        swap(arr, pivot_index, right)
        store_index = left
        # 从头开始和给定值如果小于给定值，正确位置索引加一
        # 如果大于正确索引位置不变，继续下一个位置直到该位置小于给定值，该位置和正确索引的位置，
        # 正确索引位置加一
        for i in range(left, right):
            if arr[i] < pivot:
                swap(arr, i, store_index)
                store_index += 1
        swap(arr, right, store_index)
        # print arr
        return store_index

    def find_kmax_index(arr, left, right, k):

        if len(arr) == 1:return arr[0]
        index = partition(arr, left, right)
        if index+1 == k:
            return arr[index]
        if index < k:
            #如果第一次排序后的正确index小于K，从右边开始找,返回的永远是arr的索引
            # print 'right'
            # print arr[index:right+1]
            return find_kmax_index(arr, index+1, right, k)
        else:
            #如果第一次排序后的正确index大于K，从左边开始找
            # print 'left'
            # print arr[left:index]
            return find_kmax_index(arr, left, index-1, k)

    return find_kmax_index(arr, 0, len(arr)-1, n)

def max(a,b):
    if a >= b:
        return a
    else:
        return b

def min(a,b):
    if a <= b:
        return a
    else:
        return b

def print_tree(maxheap):
    # 二叉树的层级
    if len(maxheap) < 1:
        print('该最大堆为空，请插入元素')
    else:
        n = int(log(len(maxheap),2)+1)
        for i in range(0,n):
            if i == 0:
                print('  '*(n-i) + str(maxheap[0]))
            else:
                dli = ' '*(n-i)
                pre = '  '*(n-i)
                res = dli.join([str(i) for i in maxheap[2**i-1:2**(i+1)-1]])
                print (pre + res)


if __name__ == "__main__":
    pass
