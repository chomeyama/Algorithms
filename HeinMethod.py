""" ホイン法により連立常微分方程式を解く関数
    T / N を Δt として, Δt ごとの 近似解 Y[k] (k = 0, ... , N-1)を返す
    a は初期値
    fs は 連立常微分方程式の右辺を関数と見做した時のそれら関数のリスト """

def Heun_Method(T, N, fs, a):
    dt = T / N
    n = len(fs)
    Y = [[x for x in a]]
    for j in range(N):
        t = j * dt
        tmp = []
        k1 = [fs[i](t, Y[j]) for i in range(n)]
        Y_tmp = [Y[j][i] + dt * k1[i] for i in range(n)]
        k2 = [fs[i](t + dt, Y_tmp) for i in range(n)]
        for i in range(n):
            tmp.append(Y[j][i] + dt * 0.5 * (k1[i] + k2[i]))
        Y.append(tmp)
    return Y


""" 使用例 """

def f1(t, Y):
    beta = 0.0015
    return -beta * Y[0] * Y[1]

def f2(t, Y):
    beta, ganma = 0.0015, 0.9
    return beta * Y[0] * Y[1] - ganma * Y[1]

def f3(t, Y):
    ganma = 0.9
    return ganma * Y[1]

""" 引数設定 """
fs = [f1, f2, f3]
a = [1000, 1, 0]
T, N = 100, 10000

Y_H = Heun_Method(T, N, fs, a)

""" Y の結果をプロットするファイル """
f = open('data_SIR.dat', mode = 'w')
t = 0
dt = 0.01
for Y in Y_H:
    f.write("{} {} {} {} {}\n".format(t, Y[0], Y[1], Y[2], sum(Y)))
    t += dt
f.close()
