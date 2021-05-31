import math
from queue import PriorityQueue


def printDistance(result, s):
    n = len(result)
    for i in range(0, n):
        print(f"Distance from vertex {s} to vertex {i} equals {result[i]}")


def dijkstra(G, s):
    n = len(G)
    dist = [math.inf] * n
    visited = [False] * n
    parent = [-1] * n

    dist[s] = 0
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
                parent[i] = v[1]
                q.put((dist[i], i))

    printDistance(dist, s)


if __name__ == '__main__':

    f = open("graph.txt", "r")

    matrix = []
    for line in f:
        data = [int(i) for i in line.replace(',', '').split()]
        matrix.append(data)
    start = matrix[-1]
    start = start[0]
    matrix.pop(-1)
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if matrix[i][j] == 0:
                matrix[i][j] = -1

    dijkstra(matrix, start)
