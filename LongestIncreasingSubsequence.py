from bisect import bisect_left, bisect_right

# 狭義最長単調増加部分列
def LIS(seq):
    L = [seq[0]]
    for x in seq[1:]:
        if x > L[-1]:
            L.append(x)
        else:
            L[bisect_left(L, x)] = x
    return len(L)

# 広義最長単調増加部分列
def LIS2(seq):
    INF = float('inf')
    n = len(seq)
    L = [INF] * n
    for x in seq:
        L[bisect_right(L, x)] = x
    return bisect_left(L, INF)
