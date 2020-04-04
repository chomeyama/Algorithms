""" Lagrange interpolation
    (x, y) : samples(標本点), t : polynomial's argument
    ラグランジュ補間多項式 result に t を代入した値 result(t) を返す　"""

""" ラグランジュ補間, 計算量O(N^2) """
def LI(x, y, t):
    N = len(x)
    result = 0
    numerator = 1
    for x_i in x:
        numerator *= t - x_i
    for i in range(N):
        denominator, x_i = 1, x[i]
        for x_j in x[:i]:
            denominator *= (x_i - x_j)
        for x_j in x[i+1:]:
            denominator *= (x_i - x_j)
        result += y[i] * numerator / (t - x_i) / denominator
    return result 


""" Lagrange interpolation with arithmetic sequence
    特殊ケースにおけるラグランジュ補間, 計算量O(N)
    標本点のx座標が等差数列を為す場合に使用可能 """
def LIA(x, y, t):
    N = len(x)
    numerator = 1
    for x_i in x:
        numerator *= t - x_i
    denominator, x_0 = 1, x[0]
    for x_i in x[1:]:
        denominator *= x_0 - x_i
    result, x_l, d = 0, x[-1], x[1]-x_0
    for x_i, y_i in zip(x[:-1], y[:-1]):
        result += y_i * numerator / (t - x_i) / denominator
        denominator = denominator * (x_i + d - x_0) / (x_i - x_l)
        print(result)
    result += y[-1] * numerator / (t - x_l) / denominator
    return result


""" 使用例 """
def check_arithmetic(x):
    d = x[1]-x[0]
    for x_i, x_i1 in zip(x[1:], x[2:]):
        if x_i + d != x_i1:
            return False
    return True

x = list(map(int, input().split()))
y = list(map(int, input().split()))
t = int(input())
if check_arithmetic(x):
    print(LIA(x, y, t))
else:
    print(LI(x, y, t))