""" Partially Permanent Union-Find
    半永久ユニオンファインド木

    parent[v] : vの親ノード
    height[v] : vの高さ
    nowsize[v] : vの現在のサイズ
    sizes[v] = [(t, size), ...] : 時刻tにおけるvのサイズを格納したもの
    T[v] : vが親頂点でなくなる時刻

    find(x, t) : 時刻tにおけるvの親を返す
    unite(x, y, t) : x, yを含む集合を時刻tにおいてマージする
    size(x, t) : 時刻tにおけるxのサイズを返す
    same(x, y, t) : 時刻tにおいてx, yが同じ集合に属するか判定する
    search(x, y) : x, yが同じ集合になった時刻を返す """

class ppUnionFind:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.height = [1] * n
        self.nowsize = [1] * n
        self.sizes = [[(0, 1)] for i in range(n)]
        self.T = [INF] * n

    def find(self, x, t):
        while self.T[x] <= t:
            x = self.parent[x]
        return x

    def unite(self, x, y, t):
        x, y = self.find(x, t), self.find(y, t)
        if x != y:
            a, b = (x, y) if self.height[x] < self.height[y] else (y, x)
            self.parent[a] = b
            self.T[a] = t
            self.nowsize[b] += self.nowsize[a]
            self.sizes[b].append((t, self.nowsize[b]))
            self.height[b] += (a == b)

    def size(self, x, t):
        x = self.find(x, t)
        idx = bisect(self.sizes[y], (t, INF))-1
        return self.sizes[x][idx]

    def same(self, x, y, t):
        return self.find(x, t) == self.find(y, t)

    def search(self, x, y):
        while x != y:
            Tx, Ty = self.T[x], self.T[y]
            if Tx == Ty == INF:
                res = -1
                break
            elif Tx < Ty:
                res = Tx
                x = self.parent[x]
            else:
                res = Ty
                y = self.parent[y]
        return res
