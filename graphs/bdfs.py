import heapq

graph = {} # pass

def bfs(graph):
    visited = []
    queue = [] #heapq here for opt
    queue.append(graph[0])
    while queue:
        for _ in graph.values():
            v = queue.pop(0)
            if v not in visited:
                visited.append(v)



visited = []
stack = []
def dfs(graph, v, visited, stack):
    visited.append(v)
    for neighbor in graph[v]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, stack)
    stack.append(v)
