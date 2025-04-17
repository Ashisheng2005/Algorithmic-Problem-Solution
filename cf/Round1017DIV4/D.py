#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/4/14 上午12:13 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : D.py
# @desc : README.md

n = int(input())

ans = []
for i in range(n):
    p = input()
    p_len = len(p)
    q = input()
    q_len = len(q)

    x, y = 0, 0
    while x < p_len and y < q_len:
        # print(x, y)
        if p[x] == q[y]:

            p_ = 1
            q_ = 1
            x, y = x+1, y+1

            while x < p_len:
                if p[x] == p[x-1]:
                    p_ += 1
                    x += 1
                else:
                    break

            while y < q_len:
                if q[y] == q[y-1]:
                    q_ += 1
                    y += 1

                else:
                    break

            if p_ <= q_ <= 2 * p_:
                pass

            else:
                ans.append("NO")
                break
        else:
            ans.append("NO")
            break

    else:
        if p_len-x == q_len-y==0:
            ans.append("YES")
        else:
            ans.append("NO")

for i in ans:
    print(i)
