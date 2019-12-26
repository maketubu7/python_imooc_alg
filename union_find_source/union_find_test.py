# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 15:52
# @Author  : Deng Wenxing
# @Email   : dengwenxingae86@163.com
# @File    : union_find_test.py
# @Software: PyCharm
import sys
import random
from sort_source.decoration_source import *
import psycopg2 as pg
if sys.version_info[0] == 2:
    reload(sys)
    sys.setdefaultencoding("utf-8")
    sys.setrecursionlimit(100000)

''' 连接问题和路径问题 '''
def test():
    pg.connect()

@execute_time
def uftest(uf, n):
    uf = uf(n)

    for i in range(n):
        a = random.randint(0,n-1)
        b = random.randint(0,n-1)
        uf.union(a, b)

    for i in range(n):
        a = random.randint(0,n-1)
        b = random.randint(0,n-1)
        uf.isConnected(a, b)

    return uf

class UnionFind(object):

    def __init__(self, n):
        self.count = n
        self.id = [i for i in range(n)]

    def find(self, p):
        if p >=0 and p < self.count:
            return self.id[p]
        else:
            raise IndexError

    def isConnected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        pID = self.find(p)
        qID = self.find(q)
        if pID == qID:
            return
        else:
            for i in range(self.count):
                if self.id[i] == pID:
                    self.id[i] = qID

class UnionFind2(object):
    ''' 改为树形结构 '''
    def __init__(self, n):
        self.count = n
        self.parents = [i for i in range(n)]

    def find(self, p):
        if p >= 0 and p < self.count:
            while p != self.parents[p]:
                p = self.parents[p]
            return p

    def isConnected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        proot = self.find(p)
        qroot = self.find(q)
        if proot == qroot:
            return
        self.parents[proot] = qroot

class UnionFind3(object):
    ''' 考虑union时的树形高度 '''
    def __init__(self, n):
        self.count = n
        self.parents = [i for i in range(n)]
        self.sz = [1 for i in range(n)]  # 某个根的节点的个数

    def find(self, p):
        if p >= 0 and p < self.count:
            while p != self.parents[p]:
                p = self.parents[p]
            return p

    def isConnected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        proot = self.find(p)
        qroot = self.find(q)
        if proot == qroot:
            return
        if self.sz[proot] < self.sz[qroot]:
            self.parents[proot] = qroot
            self.sz[qroot] += self.sz[proot]
        else:
            self.parents[qroot] = proot
            self.sz[proot] += self.sz[qroot]

class UnionFind4(object):
    ''' 考虑union时的树形高度 '''
    def __init__(self, n):
        self.count = n
        self.parents = [i for i in range(n)]
        self.rank = [1 for i in range(n)] # 以p为某个根对应树形节点的层数

    def find(self, p):
        if p >= 0 and p < self.count:
            while p != self.parents[p]:
                p = self.parents[p]
            return p

    def isConnected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        proot = self.find(p)
        qroot = self.find(q)
        if proot == qroot:
            return
        if self.rank[proot] < self.rank[qroot]:
            self.parents[proot] = qroot
        elif self.rank[qroot] < self.rank[proot]:
            self.parents[qroot] = proot
        else:
            self.parents[proot] = qroot
            self.rank[qroot] += 1

class UnionFind5(object):
    ''' 路径压缩优化'''
    def __init__(self, n):
        self.count = n
        self.parents = [i for i in range(n)]
        self.rank = [1 for i in range(n)] # 以p为某个根对应树形节点的层数

    def find(self, p):
        if p >= 0 and p < self.count:
            while p != self.parents[p]:
                # 如果本身不是根节点，将其指向父亲节点的父亲节点
                self.parents[p] = self.parents[self.parents[p]]
                p = self.parents[p]
            return p

    def isConnected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        proot = self.find(p)
        qroot = self.find(q)
        if proot == qroot:
            return
        if self.rank[proot] < self.rank[qroot]:
            self.parents[proot] = qroot
        elif self.rank[qroot] < self.rank[proot]:
            self.parents[qroot] = proot
        else:
            self.parents[proot] = qroot
            self.rank[qroot] += 1

class UnionFind6(object):
    ''' 路径压缩优化,最后的层级都压缩为2层的树形结构 '''
    def __init__(self, n):
        self.count = n
        self.parents = [i for i in range(n)]
        self.rank = [1 for i in range(n)] # 以p为某个根对应树形节点的层数

    def find(self, p):
        if p >= 0 and p < self.count:
            # while p != self.parents[p]:
            #     # 如果本身不是根节点，将其指向父亲节点的父亲节点
            #     self.parents[p] = self.parents[self.parents[p]]
            #     p = self.parents[p]
            # return p
            if p != self.parents[p]:
                self.parents[p] = self.find(self.parents[p])
            return self.parents[p]

    def isConnected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        proot = self.find(p)
        qroot = self.find(q)
        if proot == qroot:
            return
        if self.rank[proot] < self.rank[qroot]:
            self.parents[proot] = qroot
        elif self.rank[qroot] < self.rank[proot]:
            self.parents[qroot] = proot
        else:
            self.parents[proot] = qroot
            self.rank[qroot] += 1

if __name__ == "__main__":
    n = 100000
    # uf = uftest(UnionFind, n)
    # uf2 = uftest(UnionFind2, n)
    # uf3 = uftest(UnionFind3, n)
    uf5 = uftest(UnionFind5, n)
    uf6 = uftest(UnionFind6, n)

    # uf4 = UnionFind4(10)
    # uf4.union(1,9)
    # uf4.union(2,8)
    # uf4.union(1,3)
    # uf4.union(1,5)
    # uf4.union(1,7)
    # uf4.union(2,4)
    # uf4.union(2,6)
    #
    # print(uf4.parents)
    # print(uf4.rank)

    # print uf.id
    # print uf2.id
