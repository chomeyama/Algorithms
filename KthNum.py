""" 長さ N の数列 S の K 番目に
    小さい要素を O(N) で返す関数 """

def KthNum(S, K):
    if len(S) == 1:
        return S[0]
    M = []
    for i in range(0, int(len(S) / 5)):
        M.append(sorted(S[5 * i : 5 * i + 5])[2])
    if (len(M) < 5):
        m = sorted(S)[int(len(S) / 2)]
    else:
        m = select(M, int((len(M) + 1) / 2))
    A, B, flag = [], [], False
    for x in S:
        if x < m:
            A.append(x)
        elif x >= m:
            if x == m and flag == False:
                flag = True
                continue
            B.append(x)
    if len(A) == K - 1:
        return m
    elif len(A) >= K:
        return select(A, K)
    else:
        return select(B, K - len(A) - 1)
