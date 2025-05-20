#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/5/13 下午9:14 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : P2895.py
# @desc : README.md

m = int(input())

mp = [[None for i in range(302)] for j in range(302)]

for i in range(m):
    a,b,t = map(int, input().split())
    mp[a][b] = min(t, mp[a][b] if (mp[a][b] is not None) else t)
    if a - 1 >= 0:
        mp[a-1][b] = min(t, mp[a-1][b] if (mp[a-1][b] is not None) else t)

    if b - 1 >= 0:
        mp[a][b-1] = min(t, mp[a][b-1] if (mp[a][b-1] is not None) else t)

    mp[a+1][b] = min(t, mp[a+1][b] if (mp[a+1][b] is not None) else t)
    mp[a][b+1] = min(t, mp[a][b+1] if (mp[a][b+1] is not None) else t)

now = [(0, 0, 0)]
eip = 0
while eip < len(now):
    x, y, t = now[eip]
    if mp[x][y] is None:
        print(t)
        break

    elif t < mp[x][y]:
        if x + 1 < 302 and ((x+1, y, t+1) not in now):
            now.append((x+1, y, t+1))

        if y + 1 < 302 and ((x, y+1, t+1) not in now):
            now.append((x, y+1, t+1))

        if x - 1 >= 0 and ((x-1, y, t+1) not in now):
            now.append((x-1, y, t+1))

        if y - 1 >= 0 and ((x, y-1, t+1) not in now):
            now.append((x, y-1, t+1))

    eip += 1

else:
    print(-1)

# for i in mp:
#     print(" ".join(map(str, i)))

# print(now)


