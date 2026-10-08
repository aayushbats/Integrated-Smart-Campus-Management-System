class CampusGraph:
    def __init__(self, locations=None):
        self.adj = {v: [] for v in (locations or [])}

    def add_location(self, location):
        self.adj.setdefault(location, [])

    def add_edge(self, u, v, weight=1, undirected=True):
        self.add_location(u)
        self.add_location(v)
        self.adj[u].append((v, weight))
        if undirected:
            self.adj[v].append((u, weight))

    def vertices(self):
        return list(self.adj)

    def edges(self):
        result, seen = [], set()
        for u in self.adj:
            for v, w in self.adj[u]:
                key = tuple(sorted((u, v)))
                if key not in seen:
                    result.append((u, v, w))
                    seen.add(key)
        return result
