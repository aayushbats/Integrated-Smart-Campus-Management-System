def floyd_warshall(vertices, edges):
    inf = float("inf")
    dist = {u: {v: inf for v in vertices} for u in vertices}
    for v in vertices:
        dist[v][v] = 0
    for u, v, w in edges:
        dist[u][v] = min(dist[u][v], w)
        dist[v][u] = min(dist[v][u], w)
    for k in vertices:
        for i in vertices:
            for j in vertices:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
