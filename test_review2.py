import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from unit2_graphs.graph import CampusGraph
from unit2_graphs.bfs import bfs
from unit2_graphs.dfs import dfs
from unit2_graphs.dijkstra import dijkstra, reconstruct_path
from unit2_graphs.prim import prim
from unit2_graphs.kruskal import kruskal
from unit2_graphs.transitive_closure import transitive_closure
from unit2_graphs.bellman_ford import bellman_ford
from unit2_graphs.floyd_warshall import floyd_warshall
from unit3_dynamic_programming.knapsack_01 import knapsack_01
from unit3_dynamic_programming.lcs import lcs
from unit3_dynamic_programming.matrix_chain_multiplication import matrix_chain_cost
from unit3_dynamic_programming.resource_allocation import resource_allocation

locations = [
    "Main Gate", "Admin Block", "Central Library", "CSE Block", "CSE Lab",
    "Auditorium", "Cafeteria", "Hostel", "Sports Complex", "Transport Hub"
]
edges = [
    ("Main Gate", "Admin Block", 2), ("Main Gate", "Transport Hub", 4),
    ("Admin Block", "Central Library", 2), ("Admin Block", "Auditorium", 4),
    ("Central Library", "CSE Block", 2), ("Central Library", "Cafeteria", 3),
    ("CSE Block", "CSE Lab", 2), ("CSE Block", "Sports Complex", 4),
    ("Auditorium", "Cafeteria", 2), ("Auditorium", "Hostel", 5),
    ("Cafeteria", "Hostel", 2), ("Hostel", "Sports Complex", 3),
    ("Transport Hub", "Hostel", 6)
]
g = CampusGraph(locations)
for u, v, w in edges:
    g.add_edge(u, v, w)

assert len(bfs(g, "Main Gate")) == 10
assert len(dfs(g, "Main Gate")) == 10

dist, prev = dijkstra(g, "Main Gate")
assert dist["CSE Lab"] == 8
assert reconstruct_path(prev, "Main Gate", "CSE Lab") == [
    "Main Gate", "Admin Block", "Central Library", "CSE Block", "CSE Lab"
]

mst_p, cost_p = prim(g)
mst_k, cost_k = kruskal(g)
assert cost_p == cost_k
assert len(mst_p) == len(mst_k) == 9

vertices, reach = transitive_closure(g)
idx = {v: i for i, v in enumerate(vertices)}
assert reach[idx["Main Gate"]][idx["CSE Lab"]]

bf = bellman_ford(locations, edges, "Main Gate")
fw = floyd_warshall(locations, edges)
assert bf["CSE Lab"] == 8
assert fw["Main Gate"]["CSE Lab"] == 8

items = [
    {"name": "Smart Projector", "weight": 4, "value": 100},
    {"name": "Laptop Set", "weight": 5, "value": 120},
    {"name": "IoT Sensor Pack", "weight": 3, "value": 95},
    {"name": "Smart Board", "weight": 4, "value": 90},
    {"name": "Wi-Fi Router", "weight": 2, "value": 55},
    {"name": "CCTV Upgrade", "weight": 6, "value": 130}
]
value, selected = knapsack_01(items, 12)
assert value == 315

assert lcs("LIBRARY", "LABORATORY") == "LBRARY"
assert matrix_chain_cost([10, 20, 30, 40])[0] == 18000
assert resource_allocation([0, 20, 45, 70, 90, 105], 5)[0] == 105

print("ALL REVIEW-II TESTS PASSED")
