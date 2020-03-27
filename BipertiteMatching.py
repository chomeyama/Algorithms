""" 最大二部マッチング数を返す """

def bipertite_matching(N, edges):
    def dfs(v):
        used[v] = True
        for u in edges[v]:
            w = match[u]
            if w < 0 or (used[w] == False and dfs(w)):
                match[v] = u
                match[u] = v
                return True
        return False
    match = [-1 for _ in range(N)]
    ret = 0
    for v in range(N):
        if match[v] < 0:
            used = [False for _ in range(N)]
            if dfs(v):
                ret += 1
    return ret
