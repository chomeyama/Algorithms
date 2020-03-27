""" 最小共通祖先を求める """

import sys
sys.setrecursionlimit(10000000)
from math import log

class LCA:

    def __init__(self, N, root, edges):
        # N : 頂点数, root : 木の根, edges : 辺の連接リスト
        self.N = N
        self.root = root
        self.edges = edges
        self.LOG_N = LOG_N = int(log(N, 2)) + 1
        self.parent = [[-1 for _ in range(N)] for _ in range(LOG_N)]
        self.depth = [0 for _ in range(N)]
        self.dfs(root, -1, 0)
        parent = self.parent
        for k in range(LOG_N-1):
            for v in range(N):
                if parent[k][v] < 0:
                    parent[k+1][v] = -1
                else:
                    parent[k+1][v] = parent[k][parent[k][v]]
        self.parent = parent

    def dfs(self, v, p, d):
        self.parent[0][v] = p
        self.depth[v] = d
        for u in self.edges[v]:
            if u != p:
                self.dfs(u, v, d+1)

    # u, v の LCA を求める
    def lca(self, u, v):
        LOG_N = self.LOG_N
        depth = self.depth
        parent = self.parent
        if depth[u] > depth[v]:
            t, u = u, v
            v = t
        for k in range(LOG_N):
            if (depth[v] - depth[u]) >> k & 1:
                v = parent[k][v]
        if u == v:
            return u
        for k in range(LOG_N)[::-1]:
            if parent[k][u] != parent[k][v]:
                u, v = parent[k][u], parent[k][v]
        return parent[0][u]
