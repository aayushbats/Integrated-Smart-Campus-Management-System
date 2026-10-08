# PBL Progress Report-II — Development & Application

## Integrated Smart Campus Management System

Review-II marks the transition from the conceptual modelling completed in Report-I to executable implementation and verification.

### Unit 2 — Graphs
The campus is represented as a weighted undirected graph using an adjacency-list structure.

Implemented:
- BFS
- DFS
- Dijkstra
- Prim
- Kruskal
- Transitive Closure
- Bellman-Ford
- Floyd-Warshall

Project applications:
- BFS/DFS: campus traversal and connectivity
- Dijkstra: shortest navigation route
- Prim/Kruskal: minimum-cost campus connectivity
- Transitive Closure: reachability analysis
- Bellman-Ford/Floyd-Warshall: shortest-path verification and comparison

### Unit 3 — Dynamic Programming
Implemented:
- 0/1 Knapsack
- Longest Common Subsequence
- Matrix Chain Multiplication
- Resource Allocation

Project applications:
- 0/1 Knapsack: selecting high-utility campus resources under limited capacity
- Resource Allocation: distributing limited resources to maximize utility
- LCS and Matrix Chain Multiplication: Unit-III algorithm validation modules

### Verification
Run:

    python tests/test_review2.py

Expected final line:

    ALL REVIEW-II TESTS PASSED

### Review progression
Report-I: conceptual modelling and DSA selection.
Report-II: executable Unit-2 and Unit-3 implementation plus testing.
Final Review: integration, refinement, documentation and demonstration.
