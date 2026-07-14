import heapq

# Sample Representation for Graph B (Weighted Graph)
# Format: node: [(neighbor, cost)]
graph = {
    'S': {'A': 1, 'G': 12},
    'A': {'B': 3, 'C': 1},
    'B': {'D': 3},
    'C': {'D': 1, 'G': 2},
    'D': {'G': 3},
    'G': {}  # Empty dictionary because G has no outgoing arrows
}


def ucs(graph, start, goal):
    # Priority queue stores tuples of (cost, current_node, path)
    queue = [(0, start, [start])]
    visited = set()
    
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        
        if node not in visited:
            visited.add(node)
            
            if node == goal:
                return path, cost
                
            for neighbor, weight in graph.get(node, {}).items():
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + weight, neighbor, path + [neighbor]))
                    
    return None, float('inf')

print("\n--- Question (ii) ---")
path, total_cost = ucs(graph, 'A', 'G')
print(f"UCS Optimal Path to 'G': {path} with Total Cost: {total_cost}")