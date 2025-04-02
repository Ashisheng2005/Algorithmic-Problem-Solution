#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/3/29 下午10:33 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : A.py
# @desc : README.md

from math import gcd

n = int(input())

ans = []


def max_happiness(a):
    a.sort(reverse=True)

    return a[0] - a[-1]


for i in range(n):
    sheep = int(input())
    sheep_beauty = list(map(int, input().split()))
    ans.append(max_happiness(sheep_beauty))

for i in ans:
    print(i)

# 1
# 3
# 11 2 3 

"""
# include <iostream>
# include <vector>
# include <algorithm>

using namespace std;

int main(){
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector < int > a(n);
        for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    int max_val = * max_element(a.begin(), a.end());
    int min_val = * min_element(a.begin(), a.end());

    int result = max_val - min_val;
    cout << result << endl;
    }
}
"""