""" ダイクストラ法 """

from heapq import *

def dijkstra(s, edges):
    dist = [INF] * len(edges)
    dist[s], h = 0, []
    heappush(h, (0, s))
    while (len(h)):
        dv, v = heappop(h)
        if dv > dist[v]:
            continue
        for u, cost in edges[v]:
            tmp = dv+cost
            if tmp < dist[u]:
                dist[u] = tmp
                heappush(h, (tmp, u))
    return dist

def dijkstra_path(s, edges):
    dist = [INF for i in range(len(edges))]
    dist[s], h, p = 0, [], [-1]*len(edges)
    heappush(h, (0, s))
    while (len(h)):
        dv, v = heappop(h)
        if dv > dist[v]:
            continue
        for u, cost in edges[v]:
            tmp = dv+cost
            if tmp < dist[u]:
                dist[u] = tmp
                p[u] = v
                heappush(h, (tmp, u))
    return dist, p


from collections import defaultdict
INF = float('inf')

def dijkstra_ch(s, edges):
    dist = defaultdict(lambda : INF)
    dist[s], h = 0, []
    heappush(h, (0, s))
    while (len(h)):
        dv, v = heappop(h)
        if dv > dist[v]:
            continue
        for u, cost in edges[v]:
            tmp = dv+cost
            if tmp < dist[u]:
                dist[u] = tmp
                heappush(h, (tmp, u))
    return dist

def dijkstra_ch_path(s, edges):
    dist = defaultdict(lambda : INF)
    dist[s], h, p = 0, [], defaultdict(lambda : -1)
    heappush(h, (0, s))
    result = []
    while (len(h)):
        dv, v = heappop(h)
        if dv > dist[v]:
            continue
        for key, value in dist.items():
            print(key, value)
        print()
        result.append((v, dv))
        for u, cost in edges[v]:
            tmp = dv+cost
            if tmp < dist[u]:
                dist[u] = tmp
                p[u] = v
                heappush(h, (tmp, u))
    return dist, p, result
