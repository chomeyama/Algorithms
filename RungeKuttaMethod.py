""" ルンゲ・クッタ法により連立常微分方程式を解く関数
    T / N を Δt として, Δt ごとの 近似解 Y[k] (k = 0, ... , N-1)を返す
    a は初期値
    fs は 連立常微分方程式の右辺を関数と見做した時の, それら関数のリスト """

def Runge_Kutta_Method(T, N, fs, a):
    dt = T / N
    n = len(fs)
    Y = [[x for x in a]]
    for j in range(N):
        t = j * dt
        tmp = []
        k1 = [fs[i](t, Y[j]) for i in range(n)]
        Y_tmp = [Y[j][i] + 0.5 * dt * k1[i] for i in range(n)]
        k2 = [fs[i](t + 0.5 * dt, Y_tmp) for i in range(n)]
        Y_tmp = [Y[j][i] + 0.5 * dt * k2[i] for i in range(n)]
        k3 = [fs[i](t + 0.5 * dt, Y_tmp) for i in range(n)]
        Y_tmp = [Y[j][i] + dt * k2[i] for i in range(n)]
        k4 = [fs[i](t + dt, Y_tmp) for i in range(n)]
        for i in range(n):
            tmp.append(Y[j][i] + dt * (k1[i] + k2[i] + k3[i] + k4[i]) / 6)
        Y.append(tmp)
    return Y


""" 使用例 """

# 引数設定
sigma, r, b = 10.0, 28.0, 8/3

def f1(t, Y):
    return -sigma * Y[0] + sigma * Y[1]

def f2(t, Y):
    return -Y[0] * Y[2] + r * Y[0] - Y[1]

def f3(t, Y):
    return Y[0] * Y[1] - b * Y[2]

fs = [f1, f2, f3]
a = [0.1, 0.1, 0.1]
T, N = 200, 200000

Y_R = Runge_Kutta_Method(T, N, fs, a)

# 結果 Y_R をプロットするファイル
# 今回は３次元でプロットするとバタフライ・エフェクトのグラフが得られる
f = open('data_bat.dat', mode = 'w')
for Y in Y_R:
    f.write("{} {} {}\n".format(Y[0], Y[1], Y[2]))
f.close()
