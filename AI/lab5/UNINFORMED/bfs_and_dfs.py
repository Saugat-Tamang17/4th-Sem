from collections import deque

# Sample Representation for Graph A
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'G'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['D'],
    'H': ['E']
}


def bfs(graph, start):
    visited = []
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend([neighbor for neighbor in graph[node] if neighbor not in visited])
    return visited

def dfs(graph, start, visited=None):
    if visited is None:
        visited = []
    if start not in visited:
        visited.append(start)
        for neighbor in graph[start]:
            dfs(graph, neighbor, visited)
    return visited

print("--- Question (i) ---")
print("BFS Order for Graph A:", bfs(graph, 'A'))
print("DFS Order for Graph A:", dfs(graph, 'A'))