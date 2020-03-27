""" 重み付きユニオンファインド木 """

class WeightedUnionFind:

    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.level = [0] * n
        self.weight = [0] * n

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            px = self.find(self.par[x])
            self.weight[x] += self.weight[self.par[x]]
            self.par[x] = px
            return px

    def unite(self, x, y, w):
        px = self.find(x)
        py = self.find(y)
        if self.level[px] < self.level[py]:
            self.par[px] = py
            self.weight[px] = -self.weight[x] + self.weight[y] + w
        else:
            self.par[py] = px
            self.weight[py] = self.weight[x] - self.weight[y] - w
            if self.level[px] == self.level[py]:
                self.level[px] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def diff(self, x, y):
        return self.weight[x] - self.weight[y]


""" 使用例 """
N, Q = map(int, input().split())
uf = WeightedUnionFind(N)
for i in range(Q):
    q = [int(x) for x in input().split()]
    if q[0] == 0:
        uf.unite(q[1], q[2], q[3])
    else:
        if uf.same(q[1], q[2]):
            print(uf.diff(q[1], q[2]))
        else:
            print('?')
