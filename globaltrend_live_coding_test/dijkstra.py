import heapq
from collections import defaultdict

def dijkstra(graph, source):
    distances = {vertex: float('inf') for vertex in graph}
    distances[source] =0
    
    queue = [(0, source)]
    
    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
                
    return distances
    
def main():
    number_vertices = int(input("Number of vertices: "))
    number_edges = int(input("Number of edges: "))
    
    graph = defaultdict(dict)
    
    for _ in range(number_edges):
        u, v, weight = map(int, input("Enter edge (u v weight): ").split())
        graph[u][v] = weight
        
    source = int(input("Enter source vertex: "))
    
    short_distences = dijkstra(graph, source)
    for vertex, distance in short_distances.items():
        print(vertex, distance)
    
if __name__ == "__main__":
    main()
    
    
