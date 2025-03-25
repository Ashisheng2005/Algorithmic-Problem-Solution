#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/3/24 下午9:11 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : P3156.py
# @desc : README.md

n, m = map(int, input().split())

ls = {}
j = 1
for i in input().split():
    ls[j] = i
    j += 1

for i in input().split():
    print(ls[int(i)])

# 真就是淫贱，python超空间，还跌用c++写
#include <bits/stdc++.h>
# using namespace std;
# long long a[2000001];
#
# int main()
# {
#     long long n, m, x;
#     cin >> n >> m;
#     for (int i=1; i<=n; ++i) cin >> a[i];
#     for (int i=1; i<=m; ++i) {
#     cin >> x;
#     cout << a[x] << endl;
#     }
#     return 0;
# }


