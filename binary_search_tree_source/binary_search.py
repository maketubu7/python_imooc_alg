# -*- coding: utf-8 -*-
# @Time    : 2019/10/15 17:01
# @Author  : Deng Wenxing
# @Email   : dengwenxingae86@163.com
# @File    : binary_search.py
# @Software: PyCharm
import sys
from Queue import Queue
from sort_source import data_source
from sort_source import heap_sort

if sys.version_info[0] == 2:
    reload(sys)
    sys.setdefaultencoding("utf-8")

def create_orderd_list(min_num=0, max_num=100,length=20):
    arr = data_source.create_int_list(min_num, max_num, length)
    heap_sort.heap_sort3(arr)
    return arr



def binary_search(arr, target):
    ''' 二分查找法，必须保证数组有序且无重复元素 '''
    n = len(arr)
    l, r= 0, n-1

    while (l <= r):
        mid = (l+r)/2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            #[l,mid-1]
            r = mid - 1
        else:
            #[mid+1,r]
            l = mid + 1
    return -1

def floor(arr, target):
    n = len(arr)
    l, r = 0, n - 1
    while (l <= r):
        mid = (l+r) / 2
        if arr[mid] >= target:
            r = mid - 1
        else:
            l = mid + 1
        if arr[l] == target:
            return l
    return -1

def ceil(arr, target):
    n = len(arr)
    l, r = 0, n - 1
    while (l <= r):
        mid = (l + r) / 2
        if arr[mid] <= target:
            l = mid + 1
        else:
            r = mid - 1
        if arr[r] == target:
            return r
    return -1

class BST(object):
    # todo:实现二分搜索树
    class Node(object):
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.lchild, self.rchild = None, None

        # def __str__(self):
        #     return str(self.key) + ':' + str(self.value)

    def __init__(self):
        self.root = None
        self.count = 0

    def size(self):
        return self.count

    def is_Empty(self):
        return self.count == 0

    def insert(self, key, value):
        self.root = self.__insert(self.root, key, value)

    def contain(self, key):
        return self.__contain(self.root, key)

    def search(self, key):
        return self.__search(self.root, key)

    # 前序遍历(深度优先)
    def preOrder(self):
        self.__preOrder(self.root)

    def preOrder2(self):
        node = self.root
        keys = []
        while node is not None:
            keys.append(node.key)
            if node.lchild:
                keys.append(node.lchild.key)
                node = node.lchild

    # 中序遍历(深度优先)
    def inOrder(self):
        self.__inOrder(self.root)

    # 后序遍历(深度优先)
    def postOrder(self):
        self.__postOrder(self.root)

    # 层级遍历(广度优先)
    def levelOrder(self, ):
        q = Queue()
        q.put(self.root)
        keys = []
        while not q.empty():
            root = q.get()
            keys.append(root.key)
            if root.lchild is not None:
                q.put(root.lchild)
            if root.rchild is not None:
                q.put(root.rchild)
        print(keys)
    def mininum(self):
        if self.count < 1:
            print('该二叉树没有元素')
            raise IndexError
        return self.__mininum(self.root).key

    def maxinum(self):
        if self.count < 1:
            print('该二叉树没有元素')
            raise IndexError
        return self.__maxinum(self.root).key

    def removeMin(self):
        self.root = self.__removeMin(self.root)

    def removeMax(self):
        self.root = self.__removeMax(self.root)

    def remove(self, key):
        self.root = self.__remove(self.root, key)

    def floor(self, key):
        node = self.__floor(self.root, key)
        return node.key

    def ceil(self, key):
        node = self.__ceil(self.root, key)
        return node.key


    def __insert(self, node, key, value):
        if node is None:
            self.count += 1
            return self.Node(key, value)
        if key == node.key:
            node.value = value
        elif key < node.key:
            node.lchild = self.__insert(node.lchild, key, value)
        else :
            node.rchild = self.__insert(node.rchild, key, value)
        return node

    def __contain(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self.__contain(node.lchild, key)
        else:
            return self.__contain(node.rchild, key)

    def __search(self, node, key):

        if node is None:
            return None
        if node.key == key:
            return node.value
        elif key < node.key:
            return self.__search(node.lchild, key)
        else:
            return self.__search(node.rchild, key)

    # 前序遍历(深度优先)
    def __preOrder(self, node):
        if node is not None:
            print(node.key)
            self.__preOrder(node.lchild)
            self.__preOrder(node.rchild)
    # 中序遍历(深度优先)
    def __inOrder(self, node):
        if node is not None:
            self.__inOrder(node.lchild)
            print(node.key)
            self.__inOrder(node.rchild)
    # 后序遍历(深度优先)
    def __postOrder(self, node):
        if node is not None:
            self.__postOrder(node.lchild)
            self.__postOrder(node.rchild)
            print(node.key)
    # 查找最小值
    def __mininum(self, node):
        # 一直寻找左孩纸，直到没有左孩纸
        if node.lchild is None:
            return node
        return self.__mininum(node.lchild)

    # 查找最大值
    def __maxinum(self, node):
        # 一直寻找右孩纸，直到没有右孩纸
        if node.rchild is None:
            return node
        return self.__maxinum(node.rchild)

    # 删除二叉树的最小值
    def __removeMin(self, node):
        if node.lchild is None:
            rnode = node.rchild
            self.count -= 1
            return rnode

        node.lchild = self.__removeMin(node.lchild)
        return node

        # 删除二叉树的最小值
    def __removeMax(self, node):
        if node.rchild is None:
            lnode = node.lchild
            self.count -= 1
            return lnode

        node.rchild = self.__removeMax(node.rchild)
        return node

    def __remove(self, node, key):
        '''删除一个节点，按照最简单的算法，就是寻找这个
        节点的右子树的最小值(左子树的最大值)然后代替当前节点，
        最后删除当前节点'''
        if node == None:
            return None
        if key < node.key:
            # 小于在左子树中找
            node.lchild = self.__remove(node.lchild, key)
            return node
        if key > node.key:
            # 大于在右子树中找
            node.rchild = self.__remove(node.rchild, key)
            return node
        else:
            # 如果等于根节点，判断三种情况，
            # 1、右孩子为空，则直接让左子树代替当前节点的子树
            if node.rchild is None:
                lnode = node.lchild
                self.count -= 1
                return lnode
            # 2、左孩子为空，则直接让右子树代替当前节点的子树
            elif node.lchild is None:
                rnode = node.rchild
                self.count -= 1
                return rnode
            # 3、左右节点都不为空，则让右子树的最小值代替删除节点
            # 这里也可以用左子树的最大值来做，将内部方法变一下就行
            sucessor = self.__mininum(node.rchild) # 找到右子树的最小值的node，为successor

            # 将删除最小值后的右子树，赋值为successor 的右子树
            sucessor.rchild = self.__removeMin(node.rchild) #移除

            # 将删除节点的左子树不变的赋值给successor 的左子树
            sucessor.lchild = node.lchild

            # 最后返回新的子树
            return sucessor

    def __floor(self, node, key):
        if node == None:
            return None

        # 等于key直接返回自身
        if node.key == key:
            return key
        # 大于key，在其左子树中进行查找
        if node.key > key:
            return self.__floor(node.lchild, key)
        # 如果小于key, 则本身可能是结果，也有可能在其右子树中有跟接近的，
        # 尝试在其右子树中继续寻找，没有找到返回空
        # 则代表是自身所在的节点就是floor
        is_right = self.__floor(node.rchild, key)
        if is_right:
            return is_right
        return node

    def __ceil(self, node, key):
        if node == None:
            return None

        # 等于key直接返回自身
        if node.key == key:
            return key
        # 小于key，在其右子树中进行查找
        if node.key < key:
            return self.__ceil(node.rchild, key)
        # 如果大于key, 则本身可能是结果，也有可能在其左子树中有更接近的，
        # 尝试在其左子树中继续寻找，没有找到返回空
        # 则代表是自身所在的节点就是ceil
        is_left = self.__ceil(node.lchild, key)
        if is_left:
            return is_left
        return node


if __name__ == "__main__":
    # arr = create_orderd_list(0,100,100)
    bst = BST()
    bst.insert(2,2)
    bst.insert(1,2)
    bst.insert(-1,2)
    bst.insert(-6,2)
    bst.insert(8,2)
    bst.insert(9,2)
    bst.insert(3,2)
    bst.insert(4,2)
    bst.insert(5,2)

    print bst.floor(7)
    print bst.ceil(7)
