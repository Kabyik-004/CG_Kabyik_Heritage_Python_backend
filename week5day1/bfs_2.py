from collections import deque


def bfs_shortest_path(graph, start, end):
    """
    Find shortest path between start and end using BFS.
    Returns the path as a list of nodes.
    """
    if start == end:
        return [start]
 
    visited  = {start}
    queue    = deque([[start]])  # Queue of PATHS (not just nodes)
 
    while queue:
        path = queue.popleft()     # Get the current path
        node = path[-1]            # Last node in path
 
        for neighbour in graph[node]:
            if neighbour not in visited:
                new_path = path + [neighbour]  # Extend path
                if neighbour == end:
                    return new_path            # Found the destination!
                visited.add(neighbour)
                queue.append(new_path)
 
    return None  # No path exists
 
# Social network: find shortest connection chain
social_net = {
    'Alice':   ['Bob', 'Carol'],
    'Bob':     ['Alice', 'David'],
    'Carol':   ['Alice', 'Eve'],
    'David':   ['Bob', 'Frank'],
    'Eve':     ['Carol', 'Frank'],
    'Frank':   ['David', 'Eve']
}
 
path = bfs_shortest_path(social_net, 'Alice', 'Frank')
print(path)  # ['Alice', 'Bob', 'David', 'Frank']
print(f'{len(path)-1} degrees of separation')
