# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 11:02
# @Author  : Deng Wenxing
# @Email   : dengwenxingae86@163.com
# @File    : binary_tree_test.py
# @Software: PyCharm
import sys
import binary_search
import tools
from sort_source.decoration_source import *

if sys.version_info[0] == 2:
    reload(sys)
    sys.setdefaultencoding("utf-8")

@execute_time
def binary_search_wordCount(target):
    while True:
        try:
            if target.lower() == next(iter):
                is_exist = bst.search(target)
                if is_exist is None:
                    bst.insert(target, 1)
                else:
                    bst.insert(target,is_exist+1)
        except StopIteration:
            break

    return target.lower() + ": " + str(bst.search(target))



if __name__ == "__main__":
    bst = binary_search.BST()
    iter = tools.readfile2iter('bible.txt')
    print(binary_search_wordCount('MAKETUBU'))