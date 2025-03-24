#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/3/22 下午10:31 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : A.py
# @desc : README.md

# 2爆了，我是傻逼

def fun(s_x, s_y):
    if ord(s_x) <= ord(s_y):
        return True
    return False

n = int(input())
ans = []

for i in range(n):
    n, k = map(int, input().split())
    s = list(input())
    if len(set(s)) == 1:
        ans.append('NO')
        continue

    if s == s[::-1] and k == 0:
        ans.append("NO")
        continue

    # 反转
    x = 0
    y = len(s) - 1
    while x < y:
        if not fun(s[x], s[y]):
            max_ = x
            for j in range(x + 1, len(s)):
                if fun(s[x], s[j]):
                    if not fun(s[j], s[max_]):
                        max_ = j

            if max_ == x:
                ans.append("NO")
                break

            s[x], s[max_] = s[max_], s[x]
            k -= 1
            if k < 0:
                ans.append("NO")
                break

        x += 1
        y -= 1
    else:
        ans.append("YES")

for i in ans:
    print(i)







