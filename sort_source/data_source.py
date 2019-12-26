#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    @Version:  python 2.7.16
    @FileName: data_source.py
    @Author:   
    @Time:     2019-09-19 12:20
    @Desc: 
"""
import sys
import random

if sys.version_info[0] == 2:
    reload(sys)
    sys.setdefaultencoding("utf-8")


def create_int_list(min_num=1,max_num=100,length=20):
    int_list = []
    for i in range(length):
        int_list.append(random.randint(min_num,max_num))
    return int_list

def create_double_list(min_num=1,max_num=100,length=20):
    double_list = []
    for i in range(length):
        double_list.append(random.uniform(min_num,max_num))
    return double_list

def create_ordered_list(min_num=1,max_num=100,swap_times=10):
    tmp = [i for i in range(min_num,max_num)]
    for k in range(0,swap_times):
        i = random.randint(0, len(tmp)-1)
        j = random.randint(0, len(tmp)-1)
        tmp[i], tmp[j] = tmp[j], tmp[i]
    return tmp


if __name__ == "__main__":
    pass






