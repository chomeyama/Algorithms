""" パスカルの三角形による二項係数の高速計算 """

def Paskal(N):
    T = [[None] * i for i in range(1, N+1)]
    T[0][0] = 1
    T[1][0] = T[1][1] = 0.5
    for i in range(2, N):
        t = T[i-1]
        T[i][0] = T[i][-1] = t[0]/2
        for j in range(1, i):
            T[i][j] = (t[j-1]+t[j])/2
    return T
