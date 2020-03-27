""" いろいろ """

# ord(alph)-97 : 'a' -> 0
AtoZ = [chr(i) for i in range(65,65+26)]
atoz = [chr(i) for i in range(97,97+26)]
ItoC = defaultdict(str)
for i, x in enumerate(AtoZ):
    ItoC[x] = i

def mat(A, B):
    n = len(A)
    C = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k]*B[k][j]
            C[i][j] %= mod
    return C

b = [[0] * N for i in range(N)]
for i in range(N):
    b[i][i] = 1
while K > 0:
    if K % 2:
        b = mat(b, a)
    a = mat(a, a)
    K //= 2


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

# nCk % mod
def modCom(n, k, mod):
    p, q = 1, 1
    for i in range(n-k+1, n+1):
        p = (p * i) % mod
    for i in range(2, k+1):
        q = (q * i) % mod
    return p * pow(q, mod-2, mod) % mod

def Com(n, k):
    p, q = 1, 1
    for i in range(n-k+1, n+1):
        p *= i
    for i in range(2, k+1):
        q *= i
    return p//q

# nPk % mod, n! % mod = nPn % mod = Mod_Permutation(n, n, mod)
def modPermutation(n, k, mod):
    ret = 1
    for i in range(n - k + 1, n + 1):
        ret = ret * i % mod
    return ret

# gcd(a, b) と ax + by = gcd(a, b) を満たす整数解 x, y を返す
def extGcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extGcd(b, a % b)
        x -= (a // b) * y
        return d, y, x

def modInverse(a, mod):
    return extGcd(a, mod)[1] % mod

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


def popcnt(n):
    c = (n & 0x5555555555555555) + ((n>>1) & 0x5555555555555555)
    c = (c & 0x3333333333333333) + ((c>>2) & 0x3333333333333333)
    c = (c & 0x0f0f0f0f0f0f0f0f) + ((c>>4) & 0x0f0f0f0f0f0f0f0f)
    c = (c & 0x00ff00ff00ff00ff) + ((c>>8) & 0x00ff00ff00ff00ff)
    c = (c & 0x0000ffff0000ffff) + ((c>>16) & 0x0000ffff0000ffff)
    c = (c & 0x00000000ffffffff) + ((c>>32) & 0x00000000ffffffff)
    return c

popcount = lambda s: bin(s).count('1')
