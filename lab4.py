import heapq
import time
import random

# Algoritmul lui Dijkstra
def dijkstra(n, graph, start):
    distances = [float('inf')] * n
    distances[start] = 0
    min_heap = [(0, start)]

    while min_heap:
        curr_distance, u = heapq.heappop(min_heap)
        if curr_distance > distances[u]:
            continue

        for v, weight in graph[u]:
            distance = curr_distance + weight
            if distance < distances[v]:
                distances[v] = distance
                heapq.heappush(min_heap, (distance, v))

    return distances

# Algoritmul lui Floyd-Warshall
def floyd_warshall(n, matrix):
    dist = [row[:] for row in matrix]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

# Funcție pentru generarea grafurilor
def generate_graph(n, density, max_weight=100):
    """Generează un graf cu n noduri și densitate specificată."""
    graph = [[] for _ in range(n)]
    matrix = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        matrix[i][i] = 0

    for i in range(n):
        for j in range(n):
            if i != j and random.random() <= density:
                weight = random.randint(1, max_weight)
                graph[i].append((j, weight))
                matrix[i][j] = weight

    return graph, matrix

# Analiza empirică
def analyze_algorithms(num_vertices, densities):
    for n in num_vertices:
        for density in densities:
            print(f"\nGraf cu {n} noduri și densitate {density:.2f}:")
            graph, matrix = generate_graph(n, density)

            # Algoritmul Dijkstra
            start_time = time.time()
            for start in range(n):
                dijkstra(n, graph, start)
            dijkstra_time = time.time() - start_time
            print(f"Dijkstra: timp total = {dijkstra_time:.4f}s")

            # Algoritmul Floyd-Warshall
            start_time = time.time()
            floyd_warshall(n, matrix)
            floyd_time = time.time() - start_time
            print(f"Floyd-Warshall: timp = {floyd_time:.4f}s")

# Parametri de testare
num_vertices = [10, 50, 100]  # Număr de noduri
densities = [0.1, 0.5, 0.9]  # Densitatea grafurilor (rare/dense)

analyze_algorithms(num_vertices, densities)
