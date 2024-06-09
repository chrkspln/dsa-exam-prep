graph = []
prev_v = [-1 for _ in range(len(graph))]
_ = [] #pass
start = _[0]
end = _[-1]
INF = 10e5
def bfs(graph, start, end):
    visited = []
    queue = [] #heapq here for opt
    queue.append(graph[0])
    while queue:
        v = queue.pop(0)
        for neighbour, capacity in graph[v]:
            if v not in visited:
                visited.append(v)
                if not prev_v[neighbour]:
                    prev_v[neighbour] = []
                prev_v[neighbour] = v
                if neighbour == end:
                    return True
    return False


def ford_fulkerson(graph):
    flow = 0
    while bfs(graph):
        path_flow = INF
        e = end
        while e != start:
            path_flow = min(path_flow, graph[prev_v[e]][e])
            e = prev_v[e]
        flow+=path_flow
        e = end
        while e != start:
            e_prev = prev_v[e]
            graph[e_prev][e] -= path_flow
    return flow
