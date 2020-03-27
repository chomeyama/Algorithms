""" ニュートン法により 関数 func(x) の根を求める関数
    start : 初期値, delta : 中心差分で用いる幅, error : 打ち切り誤差
    収束先の根が 0 の場合は収束しないので収束判定を変えるか, 自明な根として処理 """

def Newton_Method(func, start, delta, error):
    half_delta = delta / 2
    def func_d(x):
        return (func(x + half_delta) - func(x - half_delta)) / delta
    x = start
    while True:
        new_x = x - func(x) / func_d(x)
        if abs(new_x - x) < error * abs(new_x):
            return new_x
        x = new_x


def g(x):
    return x ** 2 + 3 * x + 2

r = Newton_Method(g, 4.0, 0.0002, 0.00001)
print(r, g(r))
