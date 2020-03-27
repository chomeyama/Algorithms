""" Dinic法
    最大流を求める """

from collections import deque

class Dinic:

    def __init__(self, N):
        self.N = N
        self.es = [[] for _ in range(N)]
        self.level = None
        self.iter = None

    def add(self, _from, to, cap):
        self.es[_from].append([to, cap, len(self.es[to])])
        self.es[to].append([_from, 0, len(self.es[_from]) - 1])

    def bfs(self, s):
        level = [-1] * self.N
        level[s] = 0
        q = deque()
        q.append(s)
        while q:
            v = q.popleft()
            for to, cap, rev in self.es[v]:
                if cap > 0 and level[to] < 0:
                    level[to] = level[v] + 1
                    q.append(to)
        self.level = level

    def dfs(self, v, t, flow):
        if v == t:
            return flow
        for i in range(self.iter[v], len(self.es[v])):
            self.iter[v] = i
            to, cap, rev = self.es[v][i]
            if cap > 0 and self.level[v] < self.level[to]:
                f = self.dfs(to, t, min(cap, flow))
                if f > 0:
                    self.es[v][i][1] -= f
                    self.es[to][rev][0] += f
                    return f
        return 0

    def maximumFlow(self, s, t):
        flow = 0
        while True:
            self.bfs(s)
            if self.level[t] < 0:
                return flow
            self.iter = [0] * self.N
            while True:
                f = self.dfs(s, t, float('inf'))
                if f <= 0:
                    break
                flow += f
