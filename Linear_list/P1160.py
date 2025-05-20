#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/5/19 下午11:08 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : P1160.py
# @desc : README.md


# 在双向链表中集成哈希表实现空间换时间 时间复杂度为O(N + M)



class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.end = self.head
        self.size = 0
        self.mp = {}

    def append(self, data):
        node = Node(data)
        self.mp[data] = node

        if self.head is None:
            self.head = node
            self.end = self.head

        else:
            node.left = self.end
            self.end.right = node
            self.end = self.end.right

        self.size += 1

    def find(self, data):
        return self.mp.get(data, None)

        # if self.size == 0:
        #     return None
        #
        # if self.head.data == data:
        #     return self.head
        #
        # elif self.end.data == data:
        #     return self.end
        #
        # else:
        #     result = self.mp.get(data, None)
        #     if result:
        #         return result
        #
        #     temp = self.head.right
        #
        #     while temp:
        #         if temp.data == data:
        #             return temp
        #
        #         temp = temp.right
        #
        #     return None

    def delete(self, data):
        node = self.find(data)

        if node is None:
            return False

        del self.mp[data]

        if node == self.head:
            self.head.right.left = None
            self.head = self.head.right
            self.size -= 1
            return True

        if node == self.end:
            self.end = self.end.left
            self.end.right = None
            self.size -= 1
            return True

        node.left.right = node.right
        node.right.left = node.left
        self.size -= 1
        return True

    def left_insert(self, data1, data2):
        node = Node(data1)
        self.mp[data1] = node
        node2 = self.find(data2)

        if node2 is None:
            return False

        node.right = node2

        if node2 == self.head:
            self.head.left = node
            self.head = self.head.left

        else:
            node.left = node2.left
            node2.left.right = node
            node2.left = node

        self.size += 1

    def right_insert(self, data1, data2):

        node2 = self.find(data2)

        if node2 is None:
            return False

        if node2 == self.end:
            self.append(data1)
            return True

        node = Node(data1)
        self.mp[data1] = node

        node.right = node2.right
        node2.right.left = node
        node.left = node2
        node2.right = node

        self.size += 1

    def item(self):
        temp = self.head
        result = []
        while temp:
            result.append(str(temp.data))
            temp = temp.right

        return result


n = int(input())
ls = DoubleLinkedList()
ls.append(1)
for i in range(2, n+1):
    k, p = map(int, input().split())
    if p == 0:
        ls.left_insert(i, k)

    else:
        ls.right_insert(i, k)

# deleted = set()
n = int(input())
for i in range(n):
    m = int(input())
    ls.delete(m)
    # if m not in deleted:
    #     ls.delete(m)
    #     deleted.add(m)

# lss = [i for i in ls.item()]
print(" ".join(ls.item()))

