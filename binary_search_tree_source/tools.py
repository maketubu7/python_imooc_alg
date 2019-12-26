# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 10:52
# @Author  : Deng Wenxing
# @Email   : dengwenxingae86@163.com
# @File    : tools.py
# @Software: PyCharm
import sys
from collections import Iterator

if sys.version_info[0] == 2:
    reload(sys)
    sys.setdefaultencoding("utf-8")

def format_str(data):
    # return data.replace(',','').replace(':','').replace('"','').lower()
    return filter(str.isalpha, data.lower())

def readfile2iter(filename):
    list = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            words = line.split(' ')
            for word in words:
                list.append(format_str(word))

    return iter(list)

if __name__ == "__main__":
    pass