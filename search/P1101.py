#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/5/17 上午10:13 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : P1101.py
# @desc : README.md


def bfs(x, y, num, direction):
    if mp[x][y] == str1[num] or mp[x][y] == num:
        if num == 6:
            mp[x][y] = num
            return True

        right, left, up, down = False, False, False, False
        left_up, left_down, right_up, right_down = False, False, False, False
        flag = False
        if direction == 0:
            flag = True

        direction = 1 if flag else direction
        if x + 1 < n and direction == 1:
            right = bfs(x + 1, y, num + 1, direction)

        direction = 2 if flag else direction
        if x - 1 >= 0 and direction == 2:
            left = bfs(x - 1, y, num + 1, direction)

        direction = 3 if flag else direction
        if y + 1 < n and direction == 3:
            down = bfs(x, y + 1, num + 1, direction)

        direction = 4 if flag else direction
        if y - 1 >= 0 and direction == 4:
            up = bfs(x, y - 1, num + 1, direction)

        direction = 5 if flag else direction
        if x - 1 >= 0 and y - 1 >= 0 and direction == 5:
            left_up = bfs(x-1, y-1, num+1, direction)

        direction = 6 if flag else direction
        if x + 1 < n and y + 1 < n and direction == 6:
            left_down = bfs(x+1, y+1, num+1, direction)

        direction = 7 if flag else direction
        if x - 1 >= 0 and y + 1 < n and direction == 7:
            right_up = bfs(x-1, y+1, num+1, direction)

        direction = 8 if flag else direction
        if x + 1 < n and y + 1 < n and direction == 8:
            right_down = bfs(x+1, y+1, num+1, direction)

        if (right or left or up or down or left_up or left_down or right_up or right_down):
            mp[x][y] = num
            return True

    else:
        return False


str1 = "yizhong"

n = int(input())
mp = []
start_index = []
for i in range(n):
    str2 = input()
    mp2 = []
    for j in range(n):
        if str2[j] not in str1:
            mp2.append("*")
        else:
            if str2[j] == "y":
                start_index.append((i, j))

            mp2.append(str2[j])

    mp.append(mp2)


for i in start_index:
    bfs(i[0], i[1], 0, 0)

for i in mp:
    # print(''.join(i))
    for j in i:
        # print(j, end="")
        if type(j) == int:
            print(str1[j], end="")


        else:
            # print(j, end="")
            print("*", end="")
    print()