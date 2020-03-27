""" 中国剰余定理 (Chinese Remeinder Theorem)
    連立合同方程式
    x ≡ rem[0] (mod[0]) ... x ≡ rem[n-1] (mod[n-1]) を満たす
    x が M = mod[0]*mod[1]*...mod[n-1] を法として一意に存在し,
    その x( = r), M を返す """
    

""" 拡張ユークリッドの互除法により求める """
def ext_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = ext_gcd(b, a % b)
        x -= (a // b) * y
        return d, y, x

def CRT(remains, mods):
    r, M, n = 0, 1, len(remains)
    for i in range(n):
        d, x, y = ext_gcd(M, mods[i])
        if (remains[i] - r) % d != 0:
            return 0, -1
        tmp = (remains[i] - r) // d * x % (mods[i] // d)
        r += M * tmp
        M *= mods[i] // d
    return r, M


""" Garnerのアルゴリズムにより求める
    mods の要素は互いに素である必要がある"""
def garner(remains, mods):
    n = len(remains)
    x, m = remains[0], mods[0]
    for i in range(1, n):
        x += m * pow(m, mods[i]-2, mods[i]) * (remains[i]-x)
        m *= mods[i]
    return x % m, m

rem = [0, 2, 1]
mod = [2, 3, 5]
print(garner(rem, mod))
