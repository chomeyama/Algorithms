""" 各種数え上げの関数 """

N, mod = 100, 10**9+7
fac = [1] + [None] * N
for i in range(1, N+1):
    fac[i] = i * fac[i-1] % mod

facInv = [1] + [None] * N
for i in range(1, N+1):
    facInv[i] = pow(fac[i], mod-2, mod)

def modInv(x):
    return pow(x, mod-2, mod)

def modCom(n, k):
    if n < k: return 0
    return fac[n] * facInv[k] * facInv[n-k] % mod

# 包除原理 (Principle of Inclusion-Exclusion)
# n 個の玉を区別する, k 個の箱を区別する, 各箱には 1 個以上
def PIE(n, k):
    ret = 0
    for i in range(k+1):
        tmp = modCom(k, i) * pow(i, n, mod) % mod
        if (k-i) % 2:
             ret -= tmp
        else:
             ret += tmp
        ret %= mod
    return ret

# 第２種スターリング数
# n 個の玉を区別する, k 個の箱を区別しない, 各箱には 1 個以上
def StirlingNumber(n, k):
    return PIE(n, k) * facInv[k] % mod

# ベル数
# n 個の玉を区別する, k 個の箱を区別しない
# n 個の異なるモノを k 個以下のグループに分ける方法
def BellNumber(n, k):
    f = [None] * (k+1)
    for j in range(k+1):
        if j % 2:
            f[j] = -facInv[j]
        else:
            f[j] = facInv[j]
    for j in range(k):
        f[j+1] += f[j]
    ret = 0
    for i in range(k+1):
        ret = (ret + pow(i, n, mod) * facInv[i] * f[k-i]) % mod
    return ret

# n を k 個の 0 以上の整数の和に分割する方法の数
def Partition(n, k):
    P = [[0] * (k+1) for i in range(n+1)]
    for i in range(k+1):
        P[0][i] = 1
    for i in range(1, n+1):
        for j in range(1, k+1):
            if n >= k:
                P[i][j] = P[i][j-1] + P[i-j][j]
            else:
                P[i][j] = P[i][j-1]
    return P[n][k]

# n を k 個の 0 以上 m 以下の整数の和に分割する方法の数
def PartWithLim(n, k, m):
    P = [[0] * (k+1) for i in range(n+1)]
    for i in range(k+1):
        P[0][i] = 1
    for i in range(1, n+1):
        for j in range(1, k+1):
            if n >= k + m:
                P[i][j] = P[i][j-1] + P[i-j][j] - P[n-k-m][k-1]
            elif n >= k:
                P[i][j] = P[i][j-1] + P[i-j][j]
            else:
                P[i][j] = P[i][j-1]
    return P[n][k]
