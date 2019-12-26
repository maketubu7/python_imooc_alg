#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    @Version:  python 2.7.16
    @FileName: test.py
    @Author:   
    @Time:     2019-09-24 17:06
    @Desc: 
"""
import sys
import numpy as np
import random
import math

if sys.version_info[0] == 2:
    reload(sys)
    sys.setdefaultencoding("utf-8")


def func(n):
    d = np.logspace(start=1, stop=n, endpoint=True, base=2)
    print d


class Demo(object):
    def __init__(self):
        pass


if __name__ == "__main__":
    # func(10)
    # print random.randint(0,1)
    arr = [6,7,8,6,7,89]
    arr.remove(6)
    print arr





