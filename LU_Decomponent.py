""" LU_Decomponent
    A = LU, Ax = y -> return L, U, x
    LU 分解を行う関数 """

import numpy as np

def LUD(A, y):
    n = len(y)
    a, b, c = np.empty(n), np.empty(n), np.empty(n)
    for i in range(n):
        a[i] = A[i][i]
    for i in range(1, n):
        b[i] = A[i][i-1]
    for i in range(n-1):
        c[i] = A[i][i+1]
    d, l, z, x = np.empty(n), np.empty(n), np.empty(n), np.empty(n)
    d[0] = a[0]
    for i in range(1, n):
        l[i] = b[i] / d[i-1]
        d[i] = a[i] - l[i] * c[i-1]
    z[0] = y[0]
    for i in range(1, n):
        z[i] = y[i] - l[i] * z[i-1]
    x[n-1] = z[n-1] / d[n-1]
    for i in range(2, n+1):
        j = n-i
        x[j] = (z[j] - c[j] * x[j+1]) / d[j]
    L, U = np.eye(n), np.eye(n)
    for i in range(1, n):
        L[i][i-1] = l[i]
    for i in range(n):
        U[i][i] *= d[i]
    for i in range(n-1):
        U[i][i+1] = c[i]
    return L, U, x
