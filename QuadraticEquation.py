""" 二次方程式 a*x^2 + b*x + c = 0の
    解を桁落ち回避で求める関数 """

import math

def Quadratic_Equation(a, b, c):
    a, b, c = float(a), float(b), float(c)
    tmp = math.sqrt(b ** 2 - 4 * a * c)
    x1 = (-b + tmp) / (2 * a)
    x2 = c / (a * x1)
    return x1, x2
