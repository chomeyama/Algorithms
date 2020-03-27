""" Lagrange_Polynomial
    x, y : samples, t : P_n's argument
    ラグランジュ補間多項式 P_n に t を代入した値 P_n(t) を返す　"""

def LI(x, y, t):
    n = len(x)
    P_n = 0
    for i in range(n):
        l = 1
        for j in range(n):
            if i != j:
                l /= x[i] - x[j]
                l *= (t - x[j])
        P_n += l * y[i]
    return P_n
