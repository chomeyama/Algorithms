""" Gaussian_Elimination
    Ax = y -> return x
    ガウス消去法
    Ax = y の 解 x を返す """

import numpy as np

def GE(A, y):
    N = len(y)
    for i in range(N):
        index = i
        for j in range(i + 1, N):
            if abs(A[j][i]) > A[index][i]:
                index = j
        if i != index:
            tmp1, tmp2 = A[[i]], y[[i]]
            A[i], y[i] = A[[index]], y[[index]]
            A[index], y[index] = tmp1, tmp2
        for j in range(i + 1, N):
            alpha = A[j][i] / A[i][i]
            A[j][i] = 0
            for k in range(i + 1, N):
                A[j][k] -= alpha * A[i][k]
            y[j] -= alpha * y[i]
    x = np.array([None] * (N - 1) + [y[N-1] / A[N-1][N-1]])
    for i in range(N - 1):
        j = N - i - 2
        x[j] = y[j]
        for k in range(j + 1, N):
            x[j] -= A[j][k] * x[k]
        x[j] /= A[j][j]
    return x
