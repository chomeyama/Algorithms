""" 最大クリーク数と最大クリークを求める
     N : ノード数 , edges : 辺の隣接行列
     計算量は O(N2^N) """
     
def maximumClique(N, edges):
    ret, maxClq = 1, None
    for i in range(1 << N):
        clq, cnt, flag = [], 0, 0
        for j in range(N):
            if (i >> j & 1) == 0:
                continue
            for k in clq:
                if edges[j][k] == 0:
                    flag = 1
                    break
            if flag:
                cnt = 1
                break
            clq.append(j)
            cnt += 1
        if ret < cnt:
            ret = cnt
            maxClq = clq
    return ret, maxClq
