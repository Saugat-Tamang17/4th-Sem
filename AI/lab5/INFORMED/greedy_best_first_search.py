import heapq

# Provided Heuristic Values h(n)
heuristics = {
    'A': 46, 'B': 39, 'C': 41, 'D': 29, 
    'E': 38, 'F': 17, 'G': 6, 'H': 0
}

# Graph representation (node: [(neighbor, edge_cost)])
graph_c = {
    'A': [('B', 10), ('C', 8)],
    'B': [('D', 12), ('E', 15)],
    'C': [('E', 10), ('F', 25)],
    'D': [('G', 20)],
    'E': [('G', 30), ('H', 40)],
    'F': [('H', 18)],
    'G': [('H', 7)],
    'H': []
}

def greedy_best_first_search(graph, start, goal, h_table):
    # Priority Queue stores: (h_score, current_node, path)
    queue = [(h_table[start], start, [start])]
    visited = set()
    
    while queue:
        h, node, path = heapq.heappop(queue)
        
        if node == goal:
            return path
            
        if node not in visited:
            visited.add(node)
            for neighbor, _ in graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(queue, (h_table.get(neighbor, 0), neighbor, path + [neighbor]))
    return None

# --- Execution ---
start_node = 'A'
goal_node = 'H'

print("--- Greedy Best-First Search ---")
greedy_path = greedy_best_first_search(graph_c, start_node, goal_node, heuristics)
if greedy_path:
        print(f"starting point :{start_node}")
        print(f"ending or goal node:{goal_node}")
        print(f"Path: {' -> '.join(greedy_path)}")
        print("saugat tamang")
else:
    print("No path found.")