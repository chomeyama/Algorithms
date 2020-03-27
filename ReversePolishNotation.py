""" Reverse Polish Notation
   （逆ポーランド記法の計算を行うプログラム）"""

from collections import deque

def RPN(lst):
    dq = deque()
    for c in lst:
        if c.isdigit():
            dq.append(int(c))
        else:
            if c == '+':
                try:
                    x = dq[-2] + dq[-1]
                    dq.pop()
                    dq.pop()
                    dq.append(x)
                except Exception:
                    return False
            elif c == '-':
                try:
                    x = dq[-2] - dq[-1]
                    dq.pop()
                    dq.pop()
                    dq.append(x)
                except Exception:
                    return False
            elif c == '*':
                try:
                    x = dq[-2] * dq[-1]
                    dq.pop()
                    dq.pop()
                    dq.append(x)
                except Exception:
                    return False
            elif c == '/':
                try:
                    x = dq[-2] / dq[-1]
                    dq.pop()
                    dq.pop()
                    dq.append(x)
                except Exception:
                    return False
            elif c == '//':
                try:
                    x = dq[-2] // dq[-1]
                    dq.pop()
                    dq.pop()
                    dq.append(x)
                except Exception:
                    return False
            elif c == '%':
                try:
                    x = dq[-2] % dq[-1]
                    dq.pop()
                    dq.pop()
                    dq.append(x)
                except Exception:
                    return False
            else:
                return False
    return dq[0] if len(dq) == 1 else False

""" 使用例
    s = "1 5 + 2 3 - /".split() の計算"""

s = "1 2 * 3 4 5 + * -".split()
print(s)
print(RPN(s))
