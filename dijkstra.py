import math
from queue import PriorityQueue


def printDistance(result, nodes, s):
    n = len(result)
    for i in range(0, n):
        print(f"Distance from vertex {s} to vertex {i} equals {result[i]} via {nodes[i]}")


def dijkstra(G, s):
    n = len(G)
    dist = [math.inf] * n
    visited = [False] * n
    parent = [-1] * n

    dist[s] = 0
    nodes = [[] for i in range(n)]
    q = PriorityQueue()
    q.put((0, s))

    while not q.empty():
        v = q.get()
        visited[v[1]] = True
        for i in range(n):
            if visited[i] is True:
                continue
            if G[v[1]][i] != -1 and dist[i] > dist[v[1]] + G[v[1]][i]:
                dist[i] = dist[v[1]] + G[v[1]][i]
                nodes[i].append(v[1])
                parent[i] = v[1]
                q.put((dist[i], i))

    printDistance(dist, nodes, s)
