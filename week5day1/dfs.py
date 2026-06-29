def dfs_iterative(graph, start):
    """DFS using an explicit stack (mirrors BFS but with stack)"""
    visited = set()
    stack   = [start]   # Stack: use a regular list with .append/.pop
    result  = []
 
    while stack:
        node = stack.pop()          # Pop from TOP (LIFO — unlike BFS's popleft)
        if node not in visited:
            visited.add(node)
            result.append(node)
            print(f'DFS visiting: {node}')
 
            # Push neighbours (push in reverse for alphabetical order)
            for neighbour in reversed(graph[node]):
                if neighbour not in visited:
                    stack.append(neighbour)
 
    return result
 
