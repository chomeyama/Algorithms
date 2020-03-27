""" ガウス・ザイデル法
    n 元の連立一次方程式を反復法によって解く """

def Gauss_Seidel(A, y, max_k = 100, ep = 10 ** (-6)):
    n = len(y)
    f = [[y[i] / A[i][i]] + [-A[i][j] / A[i][i] for j in range(n) if i != j] for i in range(n)]
    x, px = [0] * n, [None] * n
    for k in range(max_k):
        for i in range(n):
            it, x_i = 1, f[i][0]
            for j in range(n):
                if i == j:
                    continue
                x_i += f[i][it] * x[j]
                it += 1
            px[i] = x[i]
            x[i] = x_i
        dis = [abs(x[i] - px[i]) for i in range(n)]
        if sum(dis) < ep * sum([abs(x[i]) for i in range(n)]):
            break
    return x
