#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/4/5 下午2:55 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : D.py
# @desc : README.md

# 需要第三方库
# import numpy as np
# from scipy.special import roots_legendre
#
# # 高效计算多项式 P(x) 的值（使用秦九韶算法）
# def evaluate_polynomial(coefficients, x):
#     result = 0
#     for coef in coefficients[::-1]:  # 从高次到低次
#         result = result * x + coef
#     return result
#
# # 计算积分的主函数
# def compute_integral(n, coefficients):
#     # 选择高斯点数量 k
#     # 为了满足 10^-6 的精度，k 需要足够大
#     # 这里 n = 2，k 取一个稍大的值，例如 10，确保精度
#     k = 10  # 至少 10 个点，确保精度
#
#     # 获取高斯-勒让德公式的点和权重（区间 [-1, 1]）
#     gauss_points, weights = roots_legendre(k)
#
#     # 计算被积函数在高斯点上的值
#     integral_sum = 0.0
#     for i in range(k):
#         t = gauss_points[i]  # 高斯点 t_i
#         w = weights[i]       # 对应的权重 w_i
#
#         # 变换：x = (t + 1) / 2
#         x = (t + 1) / 2
#
#         # 计算 P(x)
#         p_x = evaluate_polynomial(coefficients, x)
#
#         # 变换后的分母：t^2 + 2t + 5
#         denominator_t = t**2 + 2*t + 5
#
#         # 被积函数：P((t+1)/2) / (t^2 + 2t + 5)
#         f_t = p_x / denominator_t
#
#         # 累加 w_i * f(t_i)
#         integral_sum += w * f_t
#
#     # 积分结果：乘以系数 2（由区间变换 dx = dt/2 得到）
#     result = 2 * integral_sum
#     return result
#
# # 测试用例
# n = int(input())
# coefficients = list(map(int, input().split()))
#
# # 计算积分
# result = compute_integral(n, coefficients)
#
# # 输出结果，保留 10 位小数
# print(f"{result:.10f}")

# # 预定义 10 点高斯-勒让德公式的点和权重
# GAUSS_POINTS_10 = [
#     -0.9739065285171717, -0.8650633666889845, -0.6794095682990244, -0.4333953941292472, -0.1488743389816312,
#     0.1488743389816312, 0.4333953941292472, 0.6794095682990244, 0.8650633666889845, 0.9739065285171717
# ]
#
# GAUSS_WEIGHTS_10 = [
#     0.0666713443086881, 0.1494513491505806, 0.2190863625159820, 0.2692667193099965, 0.2955242247147529,
#     0.2955242247147529, 0.2692667193099965, 0.2190863625159820, 0.1494513491505806, 0.0666713443086881
# ]
#
# # 预定义 20 点高斯-勒让德公式的点和权重
# GAUSS_POINTS_20 = [
#     -0.9931285991850949, -0.9639719272779138, -0.9122344282513259, -0.8391169718222188, -0.7463319064601508,
#     -0.6360536807265150, -0.5108670019508271, -0.37370608871541955, -0.22778585114164507, -0.07652652113349734,
#     0.07652652113349734, 0.22778585114164507, 0.37370608871541955, 0.5108670019508271, 0.6360536807265150,
#     0.7463319064601508, 0.8391169718222188, 0.9122344282513259, 0.9639719272779138, 0.9931285991850949
# ]
#
# GAUSS_WEIGHTS_20 = [
#     0.017614007139152118, 0.04060142980038694, 0.06267204833410906, 0.08327674157670475, 0.10193011981724044,
#     0.11819453196151842, 0.13168863844917664, 0.14209610931838205, 0.14917298647260374, 0.15275338713072584,
#     0.15275338713072584, 0.14917298647260374, 0.14209610931838205, 0.13168863844917664, 0.11819453196151842,
#     0.10193011981724044, 0.08327674157670475, 0.06267204833410906, 0.04060142980038694, 0.017614007139152118
# ]
#
# # 高效计算多项式 P(x) 的值（使用秦九韶算法）
# def evaluate_polynomial(coefficients, x):
#     result = 0
#     for coef in coefficients[::-1]:  # 从高次到低次
#         result = result * x + coef
#     return result
#
# # 计算积分的主函数
# def compute_integral(n, coefficients):
#     # 根据 n 选择高斯点数量
#     if n <= 10:
#         k = 10
#         gauss_points = GAUSS_POINTS_10
#         weights = GAUSS_WEIGHTS_10
#     else:
#         k = 20
#         gauss_points = GAUSS_POINTS_20
#         weights = GAUSS_WEIGHTS_20
#
#     # 计算被积函数在高斯点上的值
#     integral_sum = 0.0
#     for i in range(k):
#         t = gauss_points[i]  # 高斯点 t_i
#         w = weights[i]       # 对应的权重 w_i
#
#         # 变换：x = (t + 1) / 2
#         x = (t + 1) / 2
#
#         # 计算 P(x)
#         p_x = evaluate_polynomial(coefficients, x)
#
#         # 变换后的分母：t^2 + 2t + 5
#         denominator_t = t * t + 2 * t + 5
#
#         # 被积函数：P((t+1)/2) / (t^2 + 2t + 5)
#         f_t = p_x / denominator_t
#
#         # 累加 w_i * f(t_i)
#         integral_sum += w * f_t
#
#     # 积分结果：乘以系数 2（由区间变换 dx = dt/2 得到）
#     result = 2 * integral_sum
#     return result
#
# # 主程序
# # 输入处理
# n = int(input())  # 读取多项式次数
# coefficients = list(map(int, input().split()))  # 读取系数 a_0, a_1, ..., a_n
#
# # 计算积分
# result = compute_integral(n, coefficients)
#
# # 输出结果，保留 10 位小数
# print(result)

import math

# 预定义数学常数
# AC
PI = 3.141592653589793
LN2 = 0.6931471805599453


# 高效计算多项式除法，得到 Q(x) 和余数 bx + c
def polynomial_division(coefficients, n):
    # x^2 + 1 的系数：1, 0, 1（对应 x^2, x, 常数项）
    divisor = [1, 0, 1]

    # 初始化商 Q(x) 的系数
    if n < 2:
        q_coeffs = [0]  # 如果 n < 2，Q(x) = 0
    else:
        q_coeffs = [0] * (n - 1)  # Q(x) 是 n-2 次多项式

    # 复制 P(x) 的系数
    remainder = coefficients[:]

    # 多项式除法
    for i in range(n, 1, -1):  # 从最高次 x^n 除到 x^2
        # 商的当前项系数
        q = remainder[i] / divisor[2]  # divisor[2] = 1
        q_coeffs[i - 2] = q

        # 更新余数
        for j in range(3):
            remainder[i - 2 + j] -= q * divisor[j]

    # 余数是 bx + c 的形式
    b = remainder[1] if n >= 1 else 0
    c = remainder[0]

    return q_coeffs, b, c


# 计算积分
def compute_integral(n, coefficients):
    # 进行多项式除法
    q_coeffs, b, c = polynomial_division(coefficients, n)

    # 计算第一部分：∫ Q(x) dx
    q_integral = 0
    for i in range(len(q_coeffs)):
        q_integral += q_coeffs[i] / (i + 1)  # ∫ x^i dx = x^(i+1)/(i+1)

    # 计算第二部分：∫ (bx + c)/(x^2 + 1) dx
    second_part = b * (LN2 / 2) + c * (PI / 4)

    # 总积分
    result = q_integral + second_part
    return result


# 主程序
# 输入处理
n = int(input())  # 读取多项式次数
coefficients = list(map(int, input().split()))  # 读取系数 a_0, a_1, ..., a_n

# 如果 n < 2，手动补齐系数
while len(coefficients) <= n:
    coefficients.append(0)

# 计算积分
result = compute_integral(n, coefficients)

# 输出结果，保留 10 位小数
print("{:.10f}".format(result))

