""" 強連結成分分解 """

import sys
sys.setrecursionlimit(10**5)
from heapq import heappush, heappop, heapify

# 強連結成分分解
class SCC:

    def __init__(self, N):
        self.N = N
        self.edges = [[] for _ in range(self.N)]
        self.rev_edges = [[] for _ in range(self.N)]

    def append_edge(self, s, t):
        self.edges[s].append(t)
        self.rev_edges[t].append(s)

    def scc(self):
        vs, cmp, used = [], [0 for i in range(self.N)], [False for _ in range(self.N)]
        def dfs(v):
            used[v] = True
            for e in self.edges[v]:
                if not used[e]:
                    dfs(e)
            vs.append(v)
        def r_dfs(v, k):
            used[v] = True
            cmp[v] = k
            for e in self.rev_edges[v]:
                if not used[e]:
                    r_dfs(e, k)
        for v in range(self.N):
            if not used[v]:
                dfs(v)
        k = 0
        used = [False for _ in range(self.N)]
        for v in vs[::-1]:
            if not used[v]:
                r_dfs(v, k)
                k += 1
        return k, cmp


# 重み付きグラフの強連結成分分解
class Weighted_Graph_SCC:

    def __init__(self, N):
        # N: グラフの頂点数, self.edges: グラフの隣接リスト表現
        self.N = N
        self.edges = [[] for _ in range(self.N)]
        self.rev_edges = [[] for _ in range(self.N)]

    def append_edge(self, s, t, cost):
        self.edges[s].append([t, cost])
        self.rev_edges[t].append([s, cost])

    def dijkstra(self, s):
        # s: start, return: distance_list
        dist = [10**20 for _ in range(self.N)]
        dist[s], h = 0, []
        heappush(h, [0, s])
        while (len(h)):
            p = heappop(h)
            dv, v = p[0], p[1]
            if dv > dist[v]:
                continue
            for i in range(len(self.edges[v])):
                u, cost = self.edges[v][i][0], self.edges[v][i][1]
                if dv + cost < dist[u]:
                    dist[u] = dv + cost
                    heappush(h, [dist[u], u])
        return dist

    def rev_dijkstra(self, s):
        # s: start, return: distance_list
        from heapq import heappush, heappop, heapify
        dist = [10**20 for _ in range(self.N)]
        dist[s], h = 0, []
        heappush(h, [0, s])
        while (len(h)):
            p = heappop(h)
            dv, v = p[0], p[1]
            if dv > dist[v]:
                continue
            for i in range(len(self.rev_edges[v])):
                u, cost = self.rev_edges[v][i][0], self.rev_edges[v][i][1]
                if dv + cost < dist[u]:
                    dist[u] = dv + cost
                    heappush(h, [dist[u], u])
        return dist

    def scc(self):
        vs, cmp, used = [], [0 for i in range(self.N)], [False for _ in range(self.N)]
        def dfs(v):
            used[v] = True
            for e in self.edges[v]:
                if not used[e[0]]:
                    dfs(e[0])
            vs.append(v)
        def r_dfs(v, k):
            used[v] = True
            cmp[v] = k
            for e in self.rev_edges[v]:
                if not used[e[0]]:
                    r_dfs(e[0], k)
        for v in range(self.N):
            if not used[v]:
                dfs(v)
        k = 0
        used = [False for _ in range(self.N)]
        for v in vs[::-1]:
            if not used[v]:
                r_dfs(v, k)
                k += 1
        return k, cmp


""" 使用例 """

# V : 頂点数 , E : 辺の数
V, E = map(int, input().split())
g = SCC(V)
# g = Weighted_Graph_SCC(V)
for i in range(E):
    # s -> t の辺
    s, t = map(int, input().split())
    g.append_edge(s, t)
    # g.append_edge(s, t, 1)

# k : 連結成分の数 , cmp : 属する連結成分の番号をリストで持たせている
k, cmp = g.scc()

# Q : クエリ数
Q = int(input())
for i in range(Q):
    u, v = map(int, input().split())
    print(int(cmp[u] == cmp[v]))
