from collections import deque
 
def bfs(graph, start):
    """
    BFS traversal starting from 'start' node.
    Returns list of nodes in BFS order.
    """
    visited = set()         # Track visited nodes (avoid revisiting)
    queue   = deque([start])  # Queue initialized with start node
    result  = []
 
    visited.add(start)      # Mark start as visited immediately
 
    while queue:                    # While there are nodes to process
        node = queue.popleft()      # Dequeue front (FIFO)
        result.append(node)
        print(f'Visiting: {node}')
 
        for neighbour in graph[node]:       # Check all neighbours
            if neighbour not in visited:    # Only visit unvisited
                visited.add(neighbour)
                queue.append(neighbour)     # Enqueue for future visit
 
    return result
 
# ── Test it ──────────────────────────
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}
 
print(bfs(graph, 0))
