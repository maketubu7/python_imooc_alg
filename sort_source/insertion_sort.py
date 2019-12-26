# -*- coding: utf-8 -*-
# @Time    : 2019/9/19 19:45
# @Author  : Deng Wenxing
# @Email   : dengwenxingae86@163.com
# @File    : insertion_sort.py
# @Software: PyCharm
import sys
import data_source
import copy
from decoration_source import *
from tools import *
import random
if sys.version_info[0] == 2:
    reload(sys)
    sys.setdefaultencoding("utf-8")
    sys.setrecursionlimit(100000)


def func():
    pass



@execute_time
def insterion_sort_v2(arr):
    n = len(arr)
    for i in range(1,n):
        # 每一个元素都和自己的前一个元素比较
        tmp = arr[i]
        minIndex = i
        for j in range(i,0,-1):
            if tmp < arr[j-1]:
                arr[j] = arr[j-1]
                minIndex = j-1
            if tmp > arr[j-1]:
                break
        arr[minIndex] = tmp
    return arr
@execute_time
def insterion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        # 每一个元素都和自己的前一个元素比较
        for j in range(i,0,-1):
            if arr[j] < arr[j-1]:
                swap(arr, j, j-1)
    return arr
#选择排序法，算法复杂度O(N^2)
@execute_time
def select_arr_sort(arr):
    n = len(arr)
    for i in range(0,n):
        minIndex = i
        #寻找[i,n)中最小的值
        for j in range(i+1,n):
            if arr[j] < arr[minIndex]:
                minIndex = j
        # print str(i) + " " + str(minIndex)
        # arr[i], arr[minIndex] = arr[minIndex], arr[i]
        swap(arr[i], arr[minIndex])
    return arr


@execute_time
def bubbleSort(arr):
    n = len(arr)
    # 遍历所有数组元素
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                swap(arr[j], arr[j+1])
    return arr

@execute_time
def merge_sort(arr):
    '''
    归并排序
    '''
    # 对两个数组进行归并
    def merge(a, b):
        c = []
        while len(a) and len(b):
            if a[0] <= b[0]:
                c.append(a.pop(0))
            elif a[0] > b[0]:
                c.append(b.pop(0))

        if len(a) != 0:
            c += a
        elif len(b) != 0:
            c += b
        return c

    # 对数组进行拆分为两个数组
    def merge_all(arr):
        if len(arr) <= 15:
            return last_sort(arr)
        mid = len(arr) // 2
        left = merge_all(arr[:mid])
        right = merge_all(arr[mid:])
        # 优化一下，因为本身两个数据就是有序的，
        # 如果左边最后一个元素小于右边第一个元素，可以不用交换位置，直接合并
        if left[-1] > right[0]:
            return merge(left, right)
        else:
            return left + right
    res = merge_all(arr)
    # print res
    return res

@execute_time
def quick_sort(arr):
    def quick(arr):
        if len(arr) <= 15:
            return last_sort(arr)
        #这里可以选取随机值和中间的值，可以保证算法复杂度的期望在O(nlogn)
        #不然对于近乎于有序的数组排序会退化为O(n^2)的复杂度

        mid = len(arr) // 2
        # mid = random.randint(0,len(arr)-1)
        piovt = arr[mid]

        left, right = [], []
        #移除找到的第一个匹配的元素
        arr.remove(piovt)
        # 对有大量重复元素的优化，相同的元素，随机添加到左右两端
        # 可消除左右不平衡的问题，使复杂度期望值在O(nlogn)
        for index, key in enumerate(arr):
            if key == piovt:
                if index % 2 == 1:
                    left.append(key)
                else:
                    right.append(key)
            elif key < piovt:
                left.append(key)
            else :
                right.append(key)

        return quick(left) + [piovt] + quick(right)
    res = quick(arr)
    # print res
    return res

@execute_time
def quick_sort_three(arr):
    def quick(arr):
        if len(arr) <= 15:
            return last_sort(arr)
        #这里可以选取随机值和中间的值，可以保证算法复杂度的期望在O(nlogn)
        #不然对于近乎于有序的数组排序会退化为O(n^2)的复杂度
        mid = len(arr) // 2
        # mid = random.randint(0,len(arr)-1)
        piovt = arr[mid]

        left, mid, right = [], [], []
        #移除找到的第一个匹配的元素
        # arr.remove(piovt)
        # 三路排序，对重复元素的排序可以省略，提高速度
        for index, key in enumerate(arr):
            if key == piovt:
                mid.append(key)
            elif key < piovt:
                left.append(key)
            else :
                right.append(key)

        return quick(left) + mid + quick(right)
    res = quick(arr)
    # print res
    return res

if __name__ == "__main__":
    arr = data_source.create_int_list(1,10000,100000)
    order_arr = data_source.create_ordered_list(1,10,20)
    # print arr
    # print order_arr
    order_arr1 = copy.deepcopy(order_arr)
    arr1 = copy.deepcopy(arr)
    arr2 = copy.deepcopy(arr)
    arr3 = copy.deepcopy(arr)
    arr4 = copy.deepcopy(arr)
    arr5 = copy.deepcopy(arr)
    # 一般数据排序
    # bubbleSort(arr3)
    # insterion_sort_v2(arr)
    # insterion_sort(arr1)
    # select_arr_sort(arr2)
    merge_sort(arr4)
    quick_sort(arr5)
    quick_sort_three(arr)
    # 近乎有序数据排序 通过优化后归并排序要快于插入排序
    # insterion_sort_v2(order_arr)
    # merge_sort(order_arr1)
