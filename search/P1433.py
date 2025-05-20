#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/5/16 下午12:33 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : P1433.py
# @desc : README.md

def pack(x1, y1, x2, y2):
    # 两点间距离公式
    return round(pow((x1 - x2) ** 2 + (y1 - y2) ** 2, 0.5), 3)

