#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/3/23 下午10:26 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : A.py
# @desc : README.md

n = int(input())

ans = []

for i in range(n):
    x, k = map(int, input().split())

    b_x = list(str(bin(x))[2:])
    print(b_x)
    c = b_x.count('1') - k

    if c > 0:
        for j in range(len(b_x)-1, -1, -1):
            if b_x[j:].count("1") == c:
                b_x[j:] = [0 for _ in range(len(b_x[j:]))]
                break
    elif c < 0:
        for j in range(len(b_x)-1, -1, -1):
            if b_x[j] == "0":
                b_x[j] = "1"
                c += 1
                if c == 0:
                    break
        else:
            for j in range(abs(c)):
                b_x.append("1")

    print(b_x)

    ans.append(abs(x - int("".join(b_x), 2)))


for i in ans:
    print(i)
    # no AC

