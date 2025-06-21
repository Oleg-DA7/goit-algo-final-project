import heapq
import math

def dijkstra(graph, start):
    distances = {vertex: math.inf for vertex in graph}
    distances[start] = 0
    preds = {vertex: None for vertex in graph}
    pq = [(0, start)] 
    visited = set()

    while pq:
        current_distance, current = heapq.heappop(pq)
        if current in visited:
            continue
        visited.add(current)

        for neighbor, weight in graph[current]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                preds[neighbor] = current
                heapq.heappush(pq, (distance, neighbor))

    return distances, preds

def get_path(preds, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = preds[current]
    return path[::-1]  # Перевертаємо шлях


# Створення графа
graph = {}
edges = [
    ('A', 'B', 2),
    ('A', 'C', 4),
    ('B', 'C', 1),
    ('B', 'D', 4),
    ('C', 'D', 2),
    ('D', 'E', 3),
    ('C', 'E', 5), 
    ('E', 'F', 2),
    ('F', 'G', 2),
    ('F', 'H', 4)
]

for src, dst, weight in edges:
    print(f"Додаємо ребро: {src} --({weight})--> {dst}")
    if src not in graph:
        graph[src] = []
        print(f"Створено вершину: {src}")
    if dst not in graph:
        graph[dst] = []
        print(f"Створено вершину: {dst}")
    graph[src].append((dst, weight))
    graph[dst].append((src, weight))

print("Граф створено:", graph)

start_vertex = 'A'
distances, preds = dijkstra(graph, start_vertex)

print("Відстані від вершини", start_vertex)
for vertex, distance in distances.items():
    print(f"До {vertex}: {distance}, шлях: {get_path(preds, vertex)}")


