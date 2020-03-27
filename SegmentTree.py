""" セグメント・ツリー """

INF = float('inf')

# Range Maximum Query
class SegmentTree:

    def __init__(self, seq, _INF = -INF):
        self.N, N = 1, len(seq)
        while self.N < N:
            self.N *= 2
        self.data = [_INF for i in range(self.N*2-1)]
        for k in range(N):
            self.Update(k, seq[k])

    def Update(self, k, a):
        k += self.N-1
        self.data[k] = a
        while k > 0:
            k = (k-1)//2
            self.data[k] = max(self.data[k*2+1], self.data[k*2+2])

    def RMQ(self, a, b, k=0, l=0, r=-1):
        if r == -1: r = self.N
        if r <= a or b <= l:
            return -INF
        if a <= l and r <= b:
            return self.data[k]
        vl = self.RMQ(a, b, k*2+1, l, (l+r)//2)
        vr = self.RMQ(a, b, k*2+2, (l+r)//2, r)
        return max(vl, vr)


# Range Minimum query
class SegmentTree:

    def __init__(self, seq, INF = INF):
        self.N, N = 1, len(seq)
        while self.N < N:
            self.N *= 2
        self.data = [INF for i in range(self.N*2-1)]
        for k in range(N):
            self.update(k, seq[k])

    def update(self, k, a):
        k += self.N-1
        self.data[k] = a
        while k > 0:
            k = (k-1)//2
            self.data[k] = min(self.data[k*2+1], self.data[k*2+2])

    def RmQ(self, a, b, k=0, l=0, r=-1):
        if r == -1: r = self.N
        if r <= a or b <= l:
            return INF
        if a <= l and r <= b:
            return self.data[k]
        vl = self.RmQ(a, b, k*2+1, l, (l+r)//2)
        vr = self.RmQ(a, b, k*2+2, (l+r)//2, r)
        return min(vl, vr)


# Range Add Query, Range Sum Query
class SegmentTree:

    def __init__(self, N):
        self.N = 1
        while self.N < N:
            self.N *= 2
        self.data1 = [0] * (2*self.N)
        self.data2 = [0] * (2*self.N)

    # [a, b) に x を加算する
    def add(self, a, b, x, k = 0, l = 0, r = -1):
        if r == -1: r = self.N
        if r <= a or b <= l: return
        if a <= l and r <= b:
            self.data1[k] += x
        else:
            self.add(a, b, x, k*2+1, l, (l+r)//2)
            self.add(a, b, x, k*2+2, (l+r)//2, r)
            self.data2[k] = max(self.data1[k*2+1]+self.data2[k*2+1], self.data1[k*2+2]+self.data2[k*2+2])

    # [a, b) の和を計算する
    def sum(self, a, b, k = 0, l = 0, r = -1):
        if r == -1: r = self.N
        if r <= a or b <= l: return 0
        if a <= l and r <= b: return self.data1[k]+self.data2[k]
        vl = self.sum(a, b, k*2+1, l, (l+r)//2)
        vr = self.sum(a, b, k*2+2, (l+r)//2, r)
        return max(vl, vr) + self.data1[k]


# Range Update Query
class SegmentTree:

    def __init__(self, N):
        self.N = 1<<(N-1).bit_length()
        self.data = [None] * (2*self.N)

    # 時刻 t に [l, r) を v に変更する
    def Update(self, l, r, t, v):
        L, R, val = l+self.N, r+self.N, (t, v)
        while L < R:
            if R & 1:
                R -= 1
                self.data[R-1] = val
            if L & 1:
                self.data[L-1] = val
                L += 1
            L >>= 1
            R >>= 1

    # 現在の x の値を得る
    def getValue(self, x):
        x += self.N-1
        ret = (-1, INF)
        while x >= 0:
            if self.data[x]:
                ret = max(ret, self.data[x])
            x = (x-1)//2
        return ret[1]
