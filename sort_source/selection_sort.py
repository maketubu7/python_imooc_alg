#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    @Version:  python 2.7.16
    @FileName: selection_sort.py
    @Author:   马克图布
    @Time:     2019-09-19 11:33
    @Desc:     排序算法
"""
import data_source
from decoration_source import *
from tools import *

if sys.version_info[0] == 2:
    reload(sys)
    sys.setdefaultencoding("utf-8")

def func():
    pass
# 重写类的比较方法
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __lt__(self, other):
        if self.score == other.score:
            return self.name < other.name
        return self.score < other.score
    def __gt__(self, other):
        return self.score > other.score
    def __eq__(self, other):
        return self.score == other.score
    def __str__(self):
        return self.name + ':' + str(self.score)

students = [Student('1',1),Student('5',5),Student('4',4),Student('3',4),Student('2',2),]

class Select_sort(object):
    #选择排序法，算法复杂度O(N^2)
    @execute_time
    def select_arr_sort(self, arr):
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

if __name__ == "__main__":
    arr = data_source.create_int_list(1,200,10000)
    tmp = arr
    Select_sort().select_arr_sort(tmp)
    # print tmp
    # Select_sort().arr_sort(students)
    # for i in range(0,len(students)):
    #     print students[i]







