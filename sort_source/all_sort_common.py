# -*- coding: utf-8 -*-
# @Time    : 2019/9/19 19:45
# @Author  : Deng Wenxing
# @Email   : dengwenxingae86@163.com
# @File    : all_sort_common.py
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
        swap(arr, i, minIndex)
    return arr


@execute_time
def bubbleSort(arr):
    n = len(arr)
    # 遍历所有数组元素
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j+1)
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
        # 可消除左右分区不平衡的问题，使复杂度期望值在O(nlogn)
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

@execute_time
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

@execute_time
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
            # 对于正确位置，永远都是索引位置加一等于k的位置
            # print 'right'
            # print arr[index:right+1]
            return find_kmax_index(arr, index+1, right, k)
        else:
            #如果第一次排序后的正确index大于K，从左边开始找,,返回的永远是arr的索引
            # print 'left'
            # print arr[left:index]
            return find_kmax_index(arr, left, index-1, k)
    res = find_kmax_index(arr, 0, len(arr)-1, n)
    print res
    return res

@execute_time
def sorted_namax_number(arr,n):
    arr = sorted(arr)
    res = arr[n-1]
    print res
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
    # merge_sort(arr4)
    # quick_sort(arr5)
    # quick_sort_three(arr)
    # 近乎有序数据排序 通过优化后归并排序要快于插入排序
    # insterion_sort_v2(order_arr)
    # merge_sort(order_arr1)
    # 拓展算法1-求数组逆序对的个数， 2-求数组中第N大的数
    # find_reverse_tuple(arr)
    find_nmax_number(arr,678)
    sorted_namax_number(arr2,678)
