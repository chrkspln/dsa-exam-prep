graph = {}

def topological_sort(graph):
    visited = []
    stack = []
    for v in graph.keys():
        if v not in visited:
            dfs(graph, v, visited, stack)
    return stack # [::-1] if want it to be reversed

# when to reverse stack? top-bottom approach in DP
# else - bottom-up

def dfs(graph, v, visited, stack):
    visited.append(v)
    for neighbor in graph[v]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, stack)
    stack.append(v)