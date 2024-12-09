import time
import random
from collections import defaultdict
import heapq

# Structura pentru mulțimi disjuncte (Kruskal)
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

# Algoritmul lui Kruskal
def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])  # Sortează muchiile după cost
    ds = DisjointSet(n)
    mst = []

    for u, v, weight in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, weight))
            if len(mst) == n - 1:
                break

    return mst

# Algoritmul lui Prim
def prim(n, graph):
    visited = [False] * n
    min_heap = [(0, 0)]  # (cost, vertex)
    mst = []
    total_cost = 0

    while min_heap:
        cost, u = heapq.heappop(min_heap)
        if visited[u]:
            continue

        visited[u] = True
        total_cost += cost
        mst.append((u, cost))

        for v, weight in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (weight, v))

    return mst, total_cost

# Generarea unui graf cu densitate specificată
def generate_graph(n, density):
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() <= density:
                cost = random.randint(1, 100)
                edges.append((i, j, cost))
    return edges

# Conversie: Lista de muchii -> Listă de adiacență (Prim)
def edges_to_adj_list(edges, n):
    graph = defaultdict(list)
    for u, v, cost in edges:
        graph[u].append((v, cost))
        graph[v].append((u, cost))
    return graph

# Analiza empirică
num_vertices = [10, 50, 100]  # Număr de vârfuri
densities = [0.1, 0.5, 0.9]  # Densitatea grafurilor

for n in num_vertices:
    for density in densities:
        print(f"\nGraf cu {n} vârfuri și densitate {density}:")

        edges = generate_graph(n, density)
        graph = edges_to_adj_list(edges, n)

        # Test Kruskal
        start_time = time.time()
        mst_kruskal = kruskal(n, edges)
        time_kruskal = time.time() - start_time
        print(f"Kruskal: timp = {time_kruskal:.4f}s, cost = {sum(w for _, _, w in mst_kruskal)}")

        # Test Prim
        start_time = time.time()
        mst_prim, cost_prim = prim(n, graph)
        time_prim = time.time() - start_time
        print(f"Prim: timp = {time_prim:.4f}s, cost = {cost_prim}")
