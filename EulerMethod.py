""" オイラー法により連立常微分方程式を解く関数
    T / N を Δt として, Δt ごとの 近似解 Y[k] (k = 0, ... , N-1)を返す
    a は初期値
    fs は 連立常微分方程式の右辺を関数と見做した時の, それら関数のリスト """

def Euler_Method(T, N, fs, a):
    dt = T / N
    n = len(fs)
    Y = [[x for x in a]]
    for j in range(1, N + 1):
        t = j * dt
        tmp = []
        for i in range(n):
            tmp.append(Y[j-1][i] + dt * fs[i](t, Y[j-1]))
        Y.append(tmp)
    return Y
