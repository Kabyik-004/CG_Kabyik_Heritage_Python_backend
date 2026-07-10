import heapq
 
def dijkstra(graph, start, end):
    """
    Find shortest path in weighted graph.
    Real-world: GPS navigation, flight cost minimizer
    graph format: {node: [(neighbour, weight), ...]}
    """
    # Priority queue: (cost, path)
    heap = [(0, [start])]
    visited = set()
 
    while heap:
        cost, path = heapq.heappop(heap)  # Get cheapest current path
        node = path[-1]
 
        if node in visited:
            continue
        visited.add(node)
 
        if node == end:
            return cost, path   # Found shortest path!
 
        for neighbour, weight in graph.get(node, []):
            if neighbour not in visited:
                heapq.heappush(heap, (cost + weight, path + [neighbour]))
 
    return float('inf'), []
 
# India city distances (km)
india_map = {
    'Mumbai':  [('Pune', 150), ('Ahmedabad', 530), ('Delhi', 1400)],
    'Pune':    [('Mumbai', 150), ('Hyderabad', 560)],
    'Delhi':   [('Mumbai', 1400), ('Jaipur', 280), ('Agra', 200)],
    'Jaipur':  [('Delhi', 280), ('Ahmedabad', 650)],
    'Ahmedabad':[('Mumbai', 530), ('Jaipur', 650)],
    'Hyderabad':[('Pune', 560), ('Chennai', 700)],
    'Chennai':  [('Hyderabad', 700)],
    'Agra':     [('Delhi', 200)],
}
 
dist, route = dijkstra(india_map, 'Mumbai', 'Chennai')
print(f'Shortest: {route}')
print(f'Distance: {dist} km')
