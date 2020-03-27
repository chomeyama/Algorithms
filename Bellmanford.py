""" ベルマンフォード法
    重みが負の辺を含むグラフにおいて
    ある頂点から全頂点への最短距離を
    O(n^2)で求める """
    
def bellmanford(edges, s, t):
    N = len(edges)
    dist = [INF] * N
    dist[s] = 0
    for i in range(N):
        update = False
        for v in range(N):
            if dist[v] == INF:
                continue
            for u, c in edges[v]:
                d = dist[v] + c
                if d < dist[u]:
                    dist[u] = d
                    update = True
        if update == False:
            return dist[t]
    else:
        return False
