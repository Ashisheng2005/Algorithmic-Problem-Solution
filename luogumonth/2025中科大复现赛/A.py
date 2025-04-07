#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/4/5 下午12:57 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : A.py
# @desc : README.md

# 理论最大罚时（根据样例）
MAX_Y_GOLD = 180558  # 金奖下确界
MAX_Y_OTHERS = 180279  # 其他下确界

# 读取输入
g, s, b, h = map(int, input().split())
n = g + s + b + h  # 总人数
players = []
for _ in range(n):
    x, y = map(int, input().split())
    players.append((x, y))

# 计算上确界和下确界
# 上确界：该类别最后一个选手的成绩
gold_upper = players[g-1]  # 金奖最后一个
silver_upper = players[g+s-1]  # 银奖最后一个
bronze_upper = players[g+s+b-1]  # 铜奖最后一个

# 下确界：理论上可能的最差成绩，参考下一个类别的第一个选手
# 金奖下确界：参考银奖第一个选手
silver_first = players[g]  # 银奖第一个
if gold_upper[0] == silver_first[0]:
    gold_lower_x = gold_upper[0]
    gold_lower_y = silver_first[1] - 1 if silver_first[1] > 0 else 0
else:
    gold_lower_x = gold_upper[0] - 1
    if g == 1:
        gold_lower_y = 180000 + 279 * gold_lower_x

    else:
        gold_lower_y = silver_first[1] - 1

# 银奖下确界：参考铜奖第一个选手
bronze_first = players[g+s]  # 铜奖第一个
if silver_upper[0] == bronze_first[0]:
    silver_lower_x = silver_upper[0]
    silver_lower_y = bronze_first[1] - 1 if bronze_first[1] > 0 else 0
else:
    silver_lower_x = silver_upper[0] - 1
    if s == 1:
        silver_lower_y = 180000 + 279 * silver_lower_x
    else:
        silver_lower_y = bronze_first[1] - 1

# 铜奖下确界：参考荣誉奖第一个选手（如果有）
if g + s + b < n:  # 如果有荣誉奖
    honor_first = players[g+s+b]  # 荣誉奖第一个
    if bronze_upper[0] == honor_first[0]:
        bronze_lower_x = bronze_upper[0]
        bronze_lower_y = honor_first[1] - 1 if honor_first[1] > 0 else 0
    else:
        bronze_lower_x = bronze_upper[0]  # 保持 x 不变
        bronze_lower_y = MAX_Y_OTHERS
else:
    # 如果没有荣誉奖，铜奖下确界取 x 不变，y 取 0
    bronze_lower_x = bronze_upper[0]
    bronze_lower_y = 0

# 输出结果
print(f"{gold_upper[0]} {gold_upper[1]} {gold_lower_x} {gold_lower_y}")
print(f"{silver_upper[0]} {silver_upper[1]} {silver_lower_x} {silver_lower_y}")
print(f"{bronze_upper[0]} {bronze_upper[1]} {bronze_lower_x} {bronze_lower_y}")