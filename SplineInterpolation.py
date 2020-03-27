""" スプライン補間を行うプログラム """

import numpy as np

def LU_Decomponent(A, y):
    if y.ndim == 1:
        ysize = y.shape[0]
    elif y.ndim == 2:
        ysize = y.shape[1]
        y = y[0]
    else:
        print("Unavailable vector")
        return
    Asize = A.shape
    n = Asize[0]
    if n != Asize[1] or n != ysize:
        print("Not match size")
        return
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
    return x


""" 使用例 """

N = 10
x = np.linspace(-1, 1, num = N+1)
y = 1 / (1 + 25 * x * x)
h, v = np.empty(N), np.empty(N)
h[0] = x[1] - x[0]
for i in range(1, N):
    h[i] = x[i+1] - x[i]
    v[i] = 6 * ((y[i+1] - y[i]) / h[i] - (y[i] - y[i-1]) / h[i-1])

A = np.empty((N-1)*(N-1)).reshape(N-1, N-1)
for i in range(N-1):
    A[i][i] = 2 * (h[i] + h[i+1])
for i in range(1, N-1):
    A[i][i-1] = h[i]
for i in range(N-2):
    A[i][i+1] = h[i+1]

u = np.hstack((np.array([0]), LU_Decomponent(A, v[1:]])))
u = np.hstack((u, np.array([0])))

k0, k1, k2, k3 = [None] * N, [None] * N, [None] * N, [None] * N
for j in range(N):
    k3[j] = (u[j+1] - u[j]) / 6 / (x[j+1] - x[j])
    k2[j] = u[j] / 2
    k1[j] = (y[j+1] - y[j]) / (x[j+1] - x[j]) - (x[j+1] - x[j]) * (2 * u[j] + u[j+1]) / 6
    k0[j] = y[j]

def S(t):
    x = np.linspace(-1, 1, num = N+1)
    for i in range(N):
        if x[i] <= t <= x[i+1]:
            j = i
            break
    return k3[j] * (t - x[j]) ** 3 + k2[j] * (t - x[j]) ** 2 + k1[j] * (t - x[j]) + k0[j]

f = open('spline.dat', mode = 'w')
for i in range(10001):
    t = -1 + 2 * i / 10000
    f.write("{} {}\n".format(t, S(t)))
f.close()

f = open('points.dat', mode = 'w')
for i in range(N+1):
    f.write("{} {}\n".format(x[i], y[i]))
f.close()
