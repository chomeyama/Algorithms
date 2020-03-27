""" x を p で置換した結果を返す """

def replace(x, p):
    return [p[i] for i in x]


""" x を p で n 回置換した結果を返す """

def powReplace(x, p, n):
    while n > 0:
        if n % 2:
            x = replace(x, p)
        p = replace(p, p)
        n //= 2
    return x
