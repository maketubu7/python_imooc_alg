# -*- coding: utf-8 -*-
# @Time    : 2019/10/18 16:11
# @Author  : Deng Wenxing
# @Email   : dengwenxingae86@163.com
# @File    : trie.py
# @Software: PyCharm
class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.Trie = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curr = self.Trie
        for w in word:
            if w not in curr:
                curr[w] = {}
            curr = curr[w]
        curr['end'] = 1

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr = self.Trie
        for w in word:
            if w not in curr:
                return False
            curr = curr[w]
        return "end" in curr

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """

        curr = self.Trie
        for w in prefix:
            if w not in curr:
                return False
            curr = curr[w]
        return True

def test(word):
    """
    Inserts a word into the trie.
    :type word: str
    :rtype: void
    """
    t = {}
    curr = t
    for w in word:
        if w not in curr:
            curr[w] = {}
        curr = curr[w]
        print curr
        print t
    curr['#'] = 1
    print curr == t
    return t



if __name__ == '__main__':
    trie = Trie()
    trie.insert('word')
    print trie.Trie



