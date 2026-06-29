import dfs







def dfs_recursive(graph, node, visited=None, result=None):
    """DFS using recursion — the call stack IS the stack"""
    if visited is None: visited = set()
    if result  is None: result  = []
 
    visited.add(node)
    result.append(node)
    print(f'DFS visiting: {node}')
 
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs_recursive(graph, neighbour, visited, result)
 
    return result
 
# Test both versions
graph = {0:[1,2], 1:[0,3,4], 2:[0,5], 3:[1], 4:[1], 5:[2]}
 
print('Iterative DFS:', dfs.dfs_iterative(graph, 0))
print('Recursive DFS:',dfs_recursive(graph, 0))
# Both output: [0, 1, 3, 4, 2, 5]  (depth-first order)
