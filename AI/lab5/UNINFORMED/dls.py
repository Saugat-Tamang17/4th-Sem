
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


def dls(graph, current, goal, limit, current_depth=0, path=None):
    if path is None:
        path = []
    
    path = path + [current]
    
    if current == goal:
        return path
    
    if current_depth >= limit:
        return None
        
    for neighbor in graph.get(current, []):
        result = dls(graph, neighbor, goal, limit, current_depth + 1, path)
        if result is not None:
            return result
            
    return None

print("\n--- Question (iii) ---")
# Testing DLS on Graph A with limit = 2 and goal = 'F'
result_path = dls(graph, 'A', 'F', limit=2)
if result_path:
    print(f"Goal 'F' found within depth limit 2. Path: {result_path}")
else:
    print("Goal 'F' not reachable or exceeds depth limit 2.")