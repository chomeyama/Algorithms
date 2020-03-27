""" Power_Method
    return A's eigenvalue, eigenvector
    ep : Convergence judgment error
    べき乗法
    A の 固有値 と 固有ベクトル を返す
    ep : 収束判定誤差 """

import numpy as np
import math

def PM(A, ep):
    n = len(A)
    x = [np.random.randn(n)]
    x.append(np.dot(A, x[0]))
    r = np.dot(x[0].T, x[1]) / np.dot(x[0].T, x[0])
    x[0] = x[1]
    x[1] = np.dot(A, x[0])
    rd = np.dot(x[0].T, x[1]) / np.dot(x[0].T, x[0])
    x[0] = x[1]
    while abs(rd - r) > ep:
        x[1] = np.dot(A, x[0])
        r = rd
        rd = np.dot(x[0].T, x[1]) / np.dot(x[0].T, x[0])
        x[0] = x[1]
    x[1] = x[1] / math.sqrt(np.sum(x[1] ** 2))
    return rd, x[1]
