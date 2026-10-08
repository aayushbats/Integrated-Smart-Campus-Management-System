def bellman_ford(vertices, edges, source):
    distance = {v: float("inf") for v in vertices}
    distance[source] = 0
    for _ in range(len(vertices) - 1):
        changed = False
        for u, v, weight in edges:
            if distance[u] != float("inf") and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                changed = True
        if not changed:
            break
    for u, v, weight in edges:
        if distance[u] != float("inf") and distance[u] + weight < distance[v]:
            raise ValueError("Negative-weight cycle detected")
    return distance
