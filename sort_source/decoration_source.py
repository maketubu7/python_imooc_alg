#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    @Version:  python 2.7.16
    @FileName: selection_sort.py
    @Author:   马克图布
    @Time:     2019-09-19 11:33
    @Desc:     排序算法
"""
import sys
import time

if sys.version_info[0] == 2:
    reload(sys)
    sys.setdefaultencoding("utf-8")


def execute_time(func):
    def func_time(self, *args, **kwargs):
        start_time = time.time()
        res = func(self, *args, **kwargs)
        end_time = time.time()
        print func.__name__ + u' 执行时间：'+ str(end_time-start_time)
        return res
    return func_time