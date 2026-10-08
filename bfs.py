from collections import deque

def bfs(graph, start):
    visited, order = {start}, []
    queue = deque([start])
    while queue:
        u = queue.popleft()
        order.append(u)
        for v, _ in graph.adj[u]:
            if v not in visited:
                visited.add(v)
                queue.append(v)
    return order
