""" SOR 法
    n 元の連立一次方程式を反復法によって解く
    一般にガウス・ザイデルより高速 """

def SOR(A, y, alpha, max_k = 100, ep = 10 ** (-6)):
    n = len(y)
    f = [[y[i] / A[i][i]] + [-A[i][j] / A[i][i] for j in range(n) if i != j] for i in range(n)]
    x, px = [0] * n, [None] * n
    for k in range(max_k):
        for i in range(n):
            it, tmp = 1, f[i][0]
            for j in range(n):
                if i == j:
                    continue
                tmp += f[i][it] * x[j]
                it += 1
            px[i] = x[i]
            x[i] = alpha * tmp + (1 - alpha) * x[i]
        dis = [abs(x[i] - px[i]) for i in range(n)]
        if sum(dis) < ep * sum([abs(x[i]) for i in range(n)]):
            break
    return x
