""" Least_Square_Method
    x, y : samples
    最小二乗法
    近似式 y = ax + b の係数
    a, b を返す """

def LSM(x, y):
    n = len(x)
    sum_x, sum_y = sum(x), sum(y)
    sum_xx, sum_yy, sum_xy = 0, 0, 0
    for i in range(n):
        sum_xx += x[i] * x[i]
        sum_yy += y[i] * y[i]
        sum_xy += x[i] * y[i]
    a = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x ** 2)
    b = (sum_xx * sum_y - sum_xy * sum_x) / (n * sum_xx - sum_x ** 2)
    return a, b
