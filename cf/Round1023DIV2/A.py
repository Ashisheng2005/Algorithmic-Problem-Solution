#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/5/5 下午10:31 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : A.py
# @desc : README.md

from math import gcd

num = int(input())

ans = []

for _ in range(num):
    n = int(input())
    mp = list(map(int, input().split()))
    # mp.sort()
    left = []
    right = []
    flag = False

    for i in mp:
        if i == 1:
            flag = True
        else:
            if i % 2 == 0:
                left.append(i)
            else:
                right.append(i)

    if len(left) == 0:
        if flag:
            left.append(1)
            flag = False
        else:
            ans.append(("NO", ))
            continue

    elif len(right) == 0:
        if flag:
            right.append(1)
            flag = False
        else:
            ans.append(("NO", ))
            continue

    left_ = left[0]
    for j in range(len(left)):
        left_ = gcd(left_, left[j])
        if left_ == 1:
            break

    right_ = right[0]
    for j in range(len(right)):
        right_ = gcd(right_, right[j])
        if right_ == 1:
            break

    if left_ == right_:
        if flag and left_ != 1:
            left.append(1)
            flag = False
        else:
            ans.append(("NO", ))

    else:
        if flag:
            if right_ == 1:
                right.append(1)
            else:
                left.append(1)

        ans.append(("YES", [2 if i in left else 1 for i in mp]))


for i in ans:
    # print(i)
    print(i[0])
    if len(i) > 1:
        print(' '.join(map(str, i[1])))

