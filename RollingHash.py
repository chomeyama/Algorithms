from collections import defaultdict

CHRtoINT = defaultdict(int)
AtoZ = [chr(i) for i in range(65,65+26)]
atoz = [chr(i) for i in range(97,97+26)]
for i, c in enumerate(atoz):
    CHRtoINT[c] = i

""" 文字列 S の長さ x の連続した部分文字列を
    ２種類の base と mod で (base, mod は互いに素)
    でハッシュ化したリストを返す """

def RollingHash(S, x, b1 = 1009, b2 = 1007, m1 = 10**9+7, m2 = 10**9+9):
    h1, h2, B1, B2 = 0, 0, 1, 1
    for c in S[:x]:
        h1 = (h1 * b1 + CHRtoINT[c]) % m1
        h2 = (h2 * b2 + CHRtoINT[c]) % m2
        B1 *= b1
        B2 *= b2
    hash = [(h1, h2)] + [None] * (len(S)-x)
    for i, c in enumerate(S[:-x]):
        h1 = (h1 * b1 - CHRtoINT[c] * B1 + CHRtoINT[S[i+x]]) % m1
        h2 = (h2 * b2 - CHRtoINT[c] * B2 + CHRtoINT[S[i+x]]) % m2
        hash[i+1] = (h1, h2)
    return hash


""" s が S に部分文字列として何個含まれているか判定する """
def RollingHash(S, s, x, b, h):
    B, v, val = pow(b, x-1, h), 0, 0
    t = B
    for c in s:
        v = (v + CHRtoINT[c] * t) % h
        t //= b
    t = B
    for c in S[:x]:
        val = (val + CHRtoINT[c] * t) % h
        t //= b
    ret = int(v == val)
    B *= b
    for i, c in enumerate(S[:-x]):
        val = (val * b - CHRtoINT[c] * B + CHRtoINT[S[i+x]]) % h
        ret += int(v == val)
    return ret


""" 文字列 S の長さ x の連続した部分文字列を
    b, h (b, h は互いに素)でハッシュ化したリストを返す """
def RollingHash(S, x, b, h):
    B, val = pow(b, x-1, h), 0
    t = B
    for c in S[:x]:
        val = (val + CHRtoINT[c] * t) % h
        t //= b
    hash = [val] + [None]*(len(S)-x)
    B *= b
    for i, c in enumerate(S[:-x]):
        val = (val * b - CHRtoINT[c] * B + CHRtoINT[S[i+x]]) % h
        hash[i+1] = val
    return hash
