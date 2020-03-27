import numpy as np
import Gaussian_Elimination

""" Expanded_Least_Square_Method
    d : degree, x and y : samples
    拡大最小二乗法
    d : 近似式の次数, x と y : サンプル """
    
def ELSM(d, x, y):
    n = len(x)
    xe = [[1] for i in range(n)]
    for i in range(n):
        tmp = x[i]
        for j in range(2 * d):
            xe[i].append(tmp)
            tmp *= x[i]
    A, ye = [], []
    for t in range(d + 1):
        J = []
        for j in range(d + 1):
            tmp = 0
            for i in range(n):
                tmp += xe[i][t + j]
            J.append(tmp)
        A.append(J)
        tmp = 0
        for i in range(n):
            tmp += y[i] * xe[i][t]
        ye.append(tmp)
    return Gaussian_Elimination.GE(d + 1, np.array(A), np.array(ye))
