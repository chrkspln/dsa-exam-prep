graph = [] # pass
dist = [] # same n*n as graph with INF and edge weight

def floyd_warshall(graph):
    # i, j, k - iterators where i stands for rows, j for columns, k for vertexes
    for i in range(len(graph)):
        for j in range(len(graph)):
            for k in range(len(graph)):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist
