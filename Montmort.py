mod = 1777777777
def factrial(N):
    fc = [1, 1] + [None] * N
    inv = [0, 1] + [None] * N
    fcInv = [1, 1] + [None] * N
    for i in range(2, N+1):
        fc[i] = i*fc[i-1]%mod
        inv[i] = mod-(inv[mod%i]*(mod//i))%mod
        fcInv[i] = fcInv[i-1]*inv[i]%mod
    return fc, fcInv
fc, fcInv = factrial(K+1)

""" モンモール数を求める
    a[i] = Montmort(i) """

a = [None]*(K+1)
a[0] = a[1] = 0
for i in range(2, K+1):
    if i % 2:
        a[i] = a[i-1]-fc[K]*fcInv[i]
    else:
        a[i] = a[i-1]+fc[K]*fcInv[i]
