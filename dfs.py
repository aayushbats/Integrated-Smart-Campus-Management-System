def dfs(graph, start):
    visited, order = set(), []
    def visit(u):
        visited.add(u)
        order.append(u)
        for v, _ in graph.adj[u]:
            if v not in visited:
                visit(v)
    visit(start)
    return order
