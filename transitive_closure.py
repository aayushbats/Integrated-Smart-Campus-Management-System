def transitive_closure(graph):
    vertices = graph.vertices()
    index = {v: i for i, v in enumerate(vertices)}
    n = len(vertices)
    reach = [[False] * n for _ in range(n)]
    for u in vertices:
        reach[index[u]][index[u]] = True
        for v, _ in graph.adj[u]:
            reach[index[u]][index[v]] = True
    for k in range(n):
        for i in range(n):
            if reach[i][k]:
                for j in range(n):
                    reach[i][j] = reach[i][j] or reach[k][j]
    return vertices, reach
