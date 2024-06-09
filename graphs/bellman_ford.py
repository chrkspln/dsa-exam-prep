graph = {} # pass
visited = []
INF = 10e5

class NegativeCycle(Exception):
    def __init__(self):
        pass


def relax(dist, vertex, dist_to_vertex, edge):
    if dist_to_vertex + edge < dist[vertex]:
        dist[vertex] = dist_to_vertex + edge
    return edge

def bellman_ford(graph):
    dist = {key: INF for key in graph.keys()}
    dist[graph[0]] = 0
    for _ in range(len(graph.keys()) - 1):
        for edge in graph[_]:
            edge = relax(dist, _, dist[_], edge)
    for key, edges in graph.items():
        if dist[key] != INF and dist[key] + edge[1] < dist[edge[0]]:
            return NegativeCycle
    return dist
