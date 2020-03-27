""" トポロジカルソートを行う関数
    トポロジカル順序昇順にノード番号を並べたリストを返す
    トポロジカルソート不可能なら False を返す
    es はグラフの隣接リスト
    ordered を指定するとインデックス昇順の結果を返す """

# トポロジカルソート
def tpsort(es, ordered = False):
    n = len(es)
    indgr = [0] * n
    for e in es:
        for u in e:
            indgr[u] += 1
    if ordered:
        from heapq import heappop, heappush
        st = []
        for v in range(n):
            if indgr[v] == 0: heappush(st, v)
        ret = []
        while st:
            v = heappop(st)
            ret.append(v)
            print(v, st, indgr)
            for u in es[v]:
                indgr[u] -= 1
                if indgr[u] == 0: heappush(st, u)
    else:
        st = [v for v in range(n) if indgr[v] == 0]
        ret = []
        while st:
            v = st.pop()
            ret.append(v)
            for u in es[v]:
                indgr[u] -= 1
                if indgr[u] == 0: st.append(u)
    if len(ret) == n:
        return ret
    else:
        return False


# 有り得るトポロジカル順序が何通りあるかを数えて返す
def tpCount(es):
    n = len(es)
    jbs = [1 << j for j in range(n)]
    b = [0] * n
    for i, e in enumerate(es):
        for j in e:
            b[i] = b[i] | jbs[j]
    dp = [0] * (1 << n)
    dp[0] = 1
    for i in range(1 << n):
        for j, jb in enumerate(jbs):
            if (i & jb) == 0 and (i & b[j]) == 0:
                dp[i | jb] += dp[i]
    return dp[-1]
