import numpy as np

class PDE:

    def __init__(self, p, q, f):
        self.p = p
        self.q = q
        self.f = f
        self.prepFlag = False

    def prepare(self, alpha, beta, x0, xn, n):
        self.n = n
        h = (xn - x0) / (n+1)
        self.a, self.b, self.c, self.g = np.empty(n), np.empty(n), np.empty(n), np.empty(n)
        for j in range(n):
            self.a[j] = self.p(h*(j+0.5)) + self.p(h*(j+1.5)) + h**2 * self.q(h*(j+1))
        for j in range(n-1):
            self.b[j] = self.c[j+1] = -self.p(h*(j+1.5))
        self.g[0] = self.p(x0+0.5*h) * alpha + h**2 * self.f(x0)
        self.g[n-1] = self.p(xn-0.5*h) * beta + h**2 * self.f(xn)
        self.prepFlag = True

    def solve(self):
        if self.prepFlag == False:
            return
        u = self.LUD(self.a, self.b, self.c, self.g, self.n)
        return u

    def LUD(self, a, b, c, g, n):
        d, v, u, m =  np.empty(n), np.empty(n), np.empty(n), np.empty(n)
        d[0] = a[0]
        for i in range(1, n):
            m[i] = c[i] / d[i-1]
            d[i] = a[i] - m[i] * b[i-1]
        v[0] = g[0]
        for i in range(1, n):
            v[i] = g[i] - m[i] * v[i-1]
        u[n-1] = v[n-1] / d[n-1]
        for i in range(2, n+1):
            j = n-i
            u[j] = (v[j] - b[j] * u[j+1]) / d[j]
        return u


def correct_u(x):
    return np.cos(x) - np.sin(x) / np.tan(1.0)

def p(x):
    return 1.0

def q(x):
    return -1

def f(x):
    return 0.0

pde = PDE(p, q, f)

alpha = 1.0
beta = 0.0
x0, xn = 0, 1.0
n = 15

pde.prepare(alpha, beta, x0, xn, n)
u = pde.solve()

h = (xn - x0) / (n+1)
f = open('data1.dat', mode = 'w')
f.write("{} {:.7f} {:.7f} {:.7f} {:.7f}\n".format(x0, alpha, alpha, 0, 0))
for i in range(n):
    _y = correct_u(h * (i+1))
    abser = abs(u[i] - _y)
    reler = abs(u[i] - _y) / abs(_y)
    f.write("{} {:.7f} {:.7f} {:.7f} {:.7f}\n".format(h * (i+1), u[i], _y, abser, reler))
    print("{} {:.7f} {:.7f} {:.7f} {:.7f}\n".format(i+1, u[i], _y, abser, reler))
f.write("{} {:.7f} {:.7f} {:.7f} {:.7f}\n".format(xn, beta, beta, 0, 0))

nc = 99
hc = (xn - x0) / (nc+1)
f = open('data2.dat', mode = 'w')
f.write("{} {}\n".format(x0, alpha))
for i in range(nc):
    f.write("{} {}\n".format(hc*(i+1), correct_u(hc*(i+1))))
f.write("{} {}\n".format(xn, beta))
