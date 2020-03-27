""" クラスカル法
    最小全域木を求めるアルゴリズム """ 

def kruskal(N, edges):
    sort(edges)
    uf = UnionFind(N)
    ret = 0
    for u, v, c in edges:
        if not uf.same(u, v):
            unite(u, v)
            ret += cost
    return ret
