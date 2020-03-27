""" 連続する K 個以上の連続部分列の
    K 番目の数を並べた列の L 番目の数を
    O(Nlog(N)) で求める """
# https://atcoder.jp/contests/joi2018yo/tasks/joi2018_yo_f

def select(S, k):
    if len(S) == 1:
        return S[0]
    M = []
    for i in range(0, int(len(S) / 5)):
        M.append(sorted(S[5 * i : 5 * i + 5])[2])
    if (len(M) < 5):
        m = sorted(S)[int(len(S) / 2)]
    else:
        m = select(M, int((len(M) + 1) / 2))
    A = []
    B = []
    flag = False
    for x in S:
        if x < m:
            A.append(x)
        elif x >= m:
            if x == m and flag == False:
                flag = True
                continue
            B.append(x)
    if len(A) == k - 1:
        return m
    elif len(A) >= k:
        return select(A, k)
    else:
        return select(B, k - len(A) - 1)

N, K, L = map(int, input().split())
a = list(map(int, input().split()))
b = []
for l in range(0, N):
    for r in range(l + K - 1, N):
        b.append(select(a[l:r + 1], K))
print(select(b, L))
