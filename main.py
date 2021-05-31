from dijkstra import dijkstra


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
