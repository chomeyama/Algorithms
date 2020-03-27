""" Least Square Method of Exponential Function
    x, y : samples
    指数関数における最小二乗法
    近似式 y = a exp(bx) の 係数 a, b を返す """

from math import *

def Exp_LSM(x, y):
    n = len(x)
    sum_x, sum_y = sum(x), sum(y)
    sum_xx, sum_yy = sum([_x ** 2 for _x in x]), sum([_y ** 2 for _y in y])
    sum_log_y = sum([log(_y) for _y in y])
    sum_x_log_y = sum([_x * log(_y) for _x, _y in zip(x, y)])
    a = exp((sum_xx * sum_log_y - sum_x_log_y * sum_x) / (n * sum_xx - sum_x ** 2))
    b = (n * sum_x_log_y - sum_x * sum_log_y) / (n * sum_xx - sum_x ** 2)
    return a, b
