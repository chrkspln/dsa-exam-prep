INF = 10e5

graph = {} # pass
visited = []

def dejikstras(graph):
    dist = {key : INF for key in graph.keys()}
    dist[graph[0]] = 0
    pq = [] # priority queue should be used here; holds v,dist pair

    while pq:
        vertex, dist_to_vertex = pq.pop(0)
        if vertex in visited:
            continue
        visited.append(vertex)

        for edge in graph[vertex]:
            if dist_to_vertex + edge < dist[vertex]:
                dist[vertex] = dist_to_vertex + edge
                pq.append((vertex, dist[vertex]))
    return dist
