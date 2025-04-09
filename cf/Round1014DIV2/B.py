#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/4/7 下午10:01 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : B.py
# @desc : README.md

"""
首先观察替换位置的规律，发现如下：、
第一种：
        0 x 0
        0 y 0
对于这种情况，y可以替换到x左右

第二种：
        0 x 0
        0 y 0
对于这种情况，x可以交换到y的左右两侧位置。

而cnt2 统计的是
x @ x @ ...
@ x @ x ...

cnt1 统计的是

@ y @ y ...
y @ y @ ...

两者分别统计交叉位置上0的个数，分别代表两个二进制中可替换位置，如果位置大于等于/小于等于 m//2 ，则表明替换可完成的
"""

n = int(input())

ans = []
for item in range(n):
    m = int(input())
    a = input()
    b = input()

    if a[0] == b[0] == "1":
        ans.append('no')

    else:
        for i in range(1, m):
            if a[i] == "1" and b[i - 1] == "0":
                pass

            elif b[i] == "1" and a[i - 1] == "0":
                pass

            elif a[i] == b[i] == '0':
                pass

            else:
                ans.append('no')
                break

        else:
            ans.append('yes')


for i in ans:
    print(i)