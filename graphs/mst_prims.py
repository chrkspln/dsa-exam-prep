import heapq
graph = {}      # pass
minheap = []
total = 0
visited = []
mst = []
heapq.heapify(minheap)


def mst_by_prim(graph):
    heapq.heappush(minheap, (0,graph[0],None))
    while minheap:
        w,curr,neigh = heapq.heappop(minheap)
        if curr not in visited:
            visited.append(curr)
            total += w
            if neigh:
                mst.append((w,curr,neigh))
        for w,v in graph[curr]:
            heapq.heappush(minheap, (w,v,curr))
    return total, mst