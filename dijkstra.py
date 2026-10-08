import heapq

def dijkstra(graph, source):
    distance = {v: float("inf") for v in graph.adj}
    previous = {v: None for v in graph.adj}
    distance[source] = 0
    pq = [(0, source)]
    while pq:
        current, u = heapq.heappop(pq)
        if current != distance[u]:
            continue
        for v, weight in graph.adj[u]:
            candidate = current + weight
            if candidate < distance[v]:
                distance[v] = candidate
                previous[v] = u
                heapq.heappush(pq, (candidate, v))
    return distance, previous

def reconstruct_path(previous, source, target):
    path, current = [], target
    while current is not None:
        path.append(current)
        if current == source:
            return path[::-1]
        current = previous[current]
    return []
