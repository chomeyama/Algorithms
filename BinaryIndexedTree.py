""" Binary Indexed Tree """

class BIT:

    def __init__(self, N):
        self.N = N
        self.bit = [0] * (N+1)

    def add(self, x, a):
        while x <= self.N:
            self.bit[x] += a
            x += x & -x

    def sum(self, x):
        ret = 0
        while x != 0:
            ret += self.bit[x]
            x -= x & -x
        return ret

    # x < sum(index) となる最小の index を返す
    def upper_bound(self, x):
        l, r = -1, self.N
        while l+1 < r:
            m = (l+r)//2
            y = self.sum(m)
            if x < y:
                r = m
            else:
                l = m
        return r

    # x <= sum(index) となる最小の index を返す
    def lower_bound(self, x):
        l, r = -1, self.N
        while l+1 < r:
            m = (l+r)//2
            y = self.sum(m)
            if y < x:
                l = m
            else:
                r = m
        return r
