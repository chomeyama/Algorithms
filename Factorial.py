""" N までの階乗の mod による
    剰余と逆元を O(N) で求める """
    
mod = 10**9+7
def factrial(N):
    fc = [1, 1] + [None] * N
    inv = [0, 1] + [None] * N
    fcInv = [1, 1] + [None] * N
    for i in range(2, N+1):
        fc[i] = i*fc[i-1]%mod
        inv[i] = mod-(inv[mod%i]*(mod//i))%mod
        fcInv[i] = fcInv[i-1]*inv[i]%mod
    return fc, fcInv

fc, fcInv = factrial(n+1)
def modCom(n, k):
    return 0 if n < k else fc[n] * fcInv[k] * fcInv[n-k] % mod
