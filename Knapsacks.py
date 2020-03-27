""" ナップサック各種 """

from collections import defaultdict
from bisect import bisect_right

def knapsack1():
    hN = N//2
    dic1, dic2 = defaultdict(lambda : 0), defaultdict(lambda : 0)
    for i in range(1 << hN):
        _w, _v = 0, 0
        for j in range(hN):
            if (i >> j) & 1:
                _w += w[j]
                _v += v[j]
        if W < _w:
            continue
        if dic1[_w] < _v:
            dic1[_w] = _v
    for i in range(1 << (N - hN)):
        _w, _v = 0, 0
        for j in range(N - hN):
            if (i >> j) & 1:
                _w += w[hN+j]
                _v += v[hN+j]
        if W < _w:
            continue
        if dic2[_w] < _v:
            dic2[_w] = _v
    ws = list(dic2.keys())
    ws.sort()
    pre = 0
    for w2 in ws:
        if dic2[w2] < pre:
            dic2[w2] = pre
        else:
            pre = dic2[w2]
    ans = 0
    for w1 in dic1:
        i = bisect_right(ws, W - w1) - 1
        w2 = ws[i]
        ans = max(ans, dic1[w1] + dic2[w2])
    return ans

def knapsack2():
    INF = float('inf')
    dp = defaultdict(lambda : INF)
    dp[0] = 0
    for i in range(N):
        wi, vi = w[i], v[i]
        dpc = dp.copy()
        for _v, _w in dpc.items():
            dp[_v+vi] = min(dp[_v+vi], _w + wi)
    for value in sorted(dp.keys(), reverse = 1):
        if dp[value] <= W:
            return value

def knapsack3():
    dp = defaultdict(lambda : 0)
    dp[0] = 0
    for i in range(N):
        wi, vi = w[i], v[i]
        dpc = dp.copy()
        for _w, _v in dpc.items():
            if _w + wi <= W:
                dp[_w+wi] = max(dp[_w+wi], _v + vi)
    return max(dp.values())

N, W = map(int, input().split())
v, w = [None] * N, [None] * N
for i in range(N):
    v[i], w[i] = map(int, input().split())
if N <= 40:
    print(knapsack1())
elif max(v) <= 1000:
    print(knapsack2())
else:
    print(knapsack3())
