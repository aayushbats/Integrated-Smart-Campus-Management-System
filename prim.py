import heapq

def prim(graph, start=None):
    if not graph.adj:
        return [], 0
    start = start or next(iter(graph.adj))
    visited = {start}
    pq = [(w, start, v) for v, w in graph.adj[start]]
    heapq.heapify(pq)
    mst, total = [], 0
    while pq and len(visited) < len(graph.adj):
        weight, u, v = heapq.heappop(pq)
        if v in visited:
            continue
        visited.add(v)
        mst.append((u, v, weight))
        total += weight
        for nxt, w in graph.adj[v]:
            if nxt not in visited:
                heapq.heappush(pq, (w, v, nxt))
    return mst, total
