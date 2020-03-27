""" 最小費用流を求める """

from heapq import *

class MinimumCostFlow:

    def __init__(self, N, INF = 10**9):
        self.N = N
        self.INF = INF
        self.edges = [[] for _ in range(N)]

    def add(self, _from, to, cap, cost):
        self.edges[_from].append([to, cap, cost, len(self.edges[to])])
        self.edges[to].append([_from, 0, -cost, len(self.edges[_from]) - 1])

    def solve(self, s, t, flow):
        ret, h = 0, [0] * self.N
        pre_v, pre_e = [0] * self.N, [0] * self.N
        while flow:
            dist = [self.INF] * self.N
            dist[s] = 0
            q = [[0, s]]
            while q:
                c, v = heappop(q)
                if dist[v] < c:
                    continue
                for i, (u, cap, cost, rev) in enumerate(self.edges[v]):
                    if cap > 0 and dist[u] > dist[v] + cost + h[v] - h[u]:
                        dist[u] = dist[v] + cost + h[v] - h[u]
                        pre_v[u], pre_e[u] = v, i
                        heappush(q, [dist[u], u])
            if dist[t] == self.INF:
                return -1
            h = [x + y for x, y in zip(h, dist)]
            d, v = flow, t
            while v != s:
                d = min(d, self.edges[pre_v[v]][pre_e[v]][1])
                v = pre_v[v]
            flow -= d
            ret += d * h[t]
            v = t
            while v != s:
                edge = self.edges[pre_v[v]][pre_e[v]]
                edge[1] -= d
                self.edges[v][edge[3]][1] += d
                v = pre_v[v]
        return ret


""" 使用例 """
V, E, F = map(int, input().split())
mcf = MinimumCostFlow(V)
for i in range(E):
    u, v, c, d = map(int, input().split())
    mcf.add(u, v, c, d)
print(mcf.solve(0, V-1, F))
