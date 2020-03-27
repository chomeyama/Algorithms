""" 幾何に関する関数群 """

from numpy import cross
from numpy.linalg import norm
from math import sqrt

# 直線 a1a2 と 点 p の距離を求める
def distance(a1, a2, p):
    x = a2 - a1
    y = p - a1
    c = cross(x, y)
    dist = abs(norm(c) / norm(x))
    return dist

# 直線 a と 直線 b の平行判定
def is_parallel(a, b):
    val = cross(a, b) == 0
    return val

# 直線 a1a2 上に 点 p が存在するか判定する
def is_on_line(a1, a2, p):
    return is_parallel(a2 - a1, p - a1)

# 線分 a1a2 上に 点 p が存在するか判定する
def is_on_linesegment(a1, a2, p):
    return is_on_line(a1, a2, p) and (norm(a1-p) + norm(a2-p) <= norm(a1-a2))

# 線分 a1a2 と 線分 b1b2 が交差しているか判定する
def is_intersected(a1, a2, b1, b2):
    a, b = a2 - a1, b2 - b1
    val1 = cross(a, b1 - a1) * cross(a, b2 - a1) <= 0
    val2 = cross(b, a1 - b1) * cross(b, a2 - b1) <= 0
    return val1 and val2

# 点 P0(x0, y0) と 線分 P1(x1, y1) - P2(x2, y2) の距離
def dist(x0, y0, x1, y1, x2, y2):
    a, b = x2-x1, y2-y1
    r, t = a*a+b*b, -a*(x1-x0)-b*(y1-y0)
    if t < 0:
        return sqrt((x1-x0)**2 + (y1-y0)**2)
    elif r < t:
        return sqrt((x2-x0)**2+(y2-y0)**2)
    f = a*(y1-y0)-b*(x1-x0)
    return sqrt(f*f/r)
