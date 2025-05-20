#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/5/11 下午5:24 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : P1443.py
# @desc : README.md

# 深搜
def ri(x, y, num):
    if 1 <= x <= n and 1 <= y <= m:
        if mp[x][y] == -1:
            mp[x][y] = num

        else:
            if mp[x][y] > num:
                mp[x][y] = num

            else:
                return

    else:
        return

    ri(x+2, y-1, num+1)
    ri(x+1, y-2, num+1)

    ri(x-1, y-2, num+1)
    ri(x-2, y-1, num+1)

    ri(x+2, y+1, num+1)
    ri(x+1, y+2, num+1)

    ri(x-2, y+1, num+1)
    ri(x-1, y+2, num+1)



# 广搜
def bfs():
    i = 0
    while i < len(dl):
        x, y, num = dl[i]
        if 1 <= x <= n and 1 <= y <= m :
            if mp[x][y] == -1 or num < mp[x][y]:
                mp[x][y] = num
                dl.append((x+2, y-1, num+1))
                dl.append((x+1, y-2, num+1))
                dl.append((x-1, y-2, num+1))
                dl.append((x-2, y-1, num+1))
                dl.append((x+2, y+1, num+1))
                dl.append((x+1, y+2, num+1))
                dl.append((x-2, y+1, num+1))
                dl.append((x-1, y+2, num+1))
        i += 1


n, m, x, y = map(int, input().split())
mp = [[-1 for i in range(m+1)]for j in range(n+1)]
dl = [(x, y, 0)]
ri(x, y, 0)
# bfs()
for i in range(1, n+1):
    print(" ".join(map(str, mp[i][1:])))
