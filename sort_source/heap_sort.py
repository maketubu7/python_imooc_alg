#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    @Version:  python 2.7.16
    @FileName: heap_sort.py
    @Author:   
    @Time:     2019-09-26 18:09
    @Desc: 
"""
import sys
import heapq
from tools import *
from insertion_sort import *

if sys.version_info[0] == 2:
    reload(sys)
    sys.setdefaultencoding("utf-8")


class MaxHeap(object):

    def __init__(self):
        self.maxheap = []
        self.count = 0

    def size(self):
        return self.size

    def isEmpty(self):
        return self.count == 0

    def __shiftup(self):
        # 最大堆的排序,插入的时候维护为一个完全最大堆
        index = self.count-1
        while (index > 0 and self.maxheap[index] > self.maxheap[(index-1) / 2]):
            swap(self.maxheap, index, (index-1) / 2)
            index = (index-1) / 2

    def __shiftdown(self):
        # 取出的时候，取出根节点， 并且维护为一个完全最大堆
        index = 0
        if self.count == 2:
            if self.maxheap[0] < self.maxheap[1]:
                swap(self.maxheap, 0, 1)
            else:
                return
        while (index < self.count and 2*index+2 < self.count):
            j = 2*index + 1
            if self.maxheap[j+1] > self.maxheap[j]:
                j += 1
            if self.maxheap[index] > self.maxheap[j]:
                break
            swap(self.maxheap,index, j)
            index = j
            # if (self.maxheap[index] >= self.maxheap[2*index+1] and self.maxheap[index] >= self.maxheap[2*index+2]):
            #     break
            # elif (self.maxheap[2*index+1] >= self.maxheap[2*index+2]):
            #     swap(self.maxheap, index, 2*index+1)
            #     index = 2*index + 1
            # else:
            #     swap(self.maxheap, index, 2 * index + 2)
            #     index = 2*index + 2

    def insert(self, item):
        self.maxheap.append(item)
        self.count += 1
        # print self.count, item
        self.__shiftup()
        # print self.maxheap

    def pop_max(self):
        max = self.maxheap[0]
        self.maxheap[0] = self.maxheap[-1]
        del self.maxheap[-1]
        self.count -= 1
        self.__shiftdown()
        # print_tree(self.maxheap)
        return max


    def __str__(self):
        res = [str(i) for i in self.maxheap]
        return ' '.join(res)

class IndexMaxHeap(object):
    #最大索引堆
    def __init__(self):
        self.maxheap = []
        self.indeces = []
        self.count = 0

    def isEmpty(self):
        return self.count == 0

    def __shiftup(self):
        # 最大堆的排序,插入的时候维护为一个完全最大堆
        index = self.count-1
        while (index > 0 and self.maxheap[self.indeces[index]] > self.maxheap[self.indeces[(index-1) / 2]]):
            swap(self.indeces, index, (index-1) / 2)
            index = (index-1) / 2

    def __shiftdown(self):
        # 取出的时候，取出根节点， 并且维护为一个完全最大堆
        index = 0
        if self.count == 2:
            if self.maxheap[self.indeces[0]] < self.maxheap[self.indeces[1]]:
                swap(self.indeces, 0, 1)
            else:
                return
        while (index < self.count and 2*index+2 < self.count):
            j = 2*index + 1
            if self.maxheap[self.indeces[j+1]] > self.maxheap[self.indeces[j]]:
                j += 1
            if self.maxheap[self.indeces[index]] > self.maxheap[self.indeces[j]]:
                break
            swap(self.indeces,index, j)
            index = j

    def insert(self, item):
        self.maxheap.append(item)
        self.indeces.append(self.count)
        self.count += 1
        # print self.count, item
        self.__shiftup()
        # print self.maxheap

    def pop_max(self):
        max = self.maxheap[self.indeces[0]]
        swap(self.indeces, 0, 1)
        # del self.maxheap[self.indeces[-1]]
        self.count -= 1
        self.__shiftdown()
        # print_tree(self.maxheap)
        return max
    def pop_max_index(self):
        max_index =  self.indeces[0]
        swap(self.indeces, 0, 1)
        # del self.maxheap[self.indeces[-1]]
        self.count -= 1
        self.__shiftdown()
        return max_index

    def __rebuild(self):
        def shiftdown(arr, n, i):
            while (2 * i + 1 < n):
                j = 2 * i + 1
                if j + 1 < n and arr[j + 1] > arr[j]:
                    j += 1
                if arr[i] > arr[j]:
                    break
                swap(arr, i, j)
                i = j
        n = self.count
        # 先对原数组整理为一个最大堆
        for i in range(int(n / 2 - 1), -1, -1):
            shiftdown(self.maxheap, n, i)

    def change(self, i, new_item):
        self.maxheap[i] = new_item
        self.__rebuild()

    def __str__(self):
        res_data = [str(i) for i in self.maxheap]
        res_index = [str(i) for i in self.indeces]
        return ' '.join(res_data) + '\n' + ' '.join(res_index)



@execute_time
def heap_sort1(arr):
    ''' 基础堆排序算法, 先插入所有元素，在抓取最大值 返回所有结果'''
    mah = MaxHeap()
    res = []
    for key in arr:
        mah.insert(key)
    while not mah.isEmpty():
        res.append(mah.pop_max())
    res.reverse()
    return res

@execute_time
def heap_sort2(arr):
    ''' 直接把数组变为最大堆，在抓取最大值  '''
    n = len(arr)
    last_root = n/2 -1
    print last_root

    for i in range(last_root,-1,-1):
        print i
        left = min(n-1,2*i+1)
        right = min(n-1,2*i+2)
        if arr[i] >= arr[left] and arr[i] >= arr[right]:
            return
        elif arr[left] >= arr[right]:
            swap(arr, i, left)
        else:
            swap(arr, i, right)
@execute_time
def heap_sort3(arr):
    #在原数组上直接进行shiftdown操作，不用额外开辟存储空间，没有相关的赋值操作，
    # 速度优于1，2
    n = len(arr)
    def __shiftdown(arr, n, i):
        while (2*i+1 < n):
            j = 2*i+1
            if j+1 < n and arr[j+1] > arr[j]:
                j += 1
            if arr[i] > arr[j]:
                break
            swap(arr, i, j)
            i = j
    #先对原数组整理为一个最大堆
    for i in range(n/2-1,-1,-1):
        __shiftdown(arr, n, i)
    # print_tree(arr)

    #1、把根节点和最后一个元素交换位置
    #2、对除去最后一个元素的前面的二叉树重新整理为一个最大堆，直到堆中只剩最后一个元素
    #3、那么该数组就完全有序了
    for i in range(n-1,0,-1):
        swap(arr,i,0)
        __shiftdown(arr,i,0)


if __name__ == "__main__":
    mah = IndexMaxHeap()

    arr = data_source.create_int_list(1,100,10)
    arr1 = copy.deepcopy(arr)

    for key in arr:
        mah.insert(key)
    print mah
    mah.change(7,199)
    print mah






