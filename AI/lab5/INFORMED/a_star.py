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

def a_star_search(graph, start, goal, h_table):
    # Priority Queue stores: (f_score, actual_cost_g, current_node, path)
    queue = [(h_table[start], 0, start, [start])]
    visited = set()
    
    while queue:
        f, g, node, path = heapq.heappop(queue)
        
        if node == goal:
            return path, g
            
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph.get(node, []):
                if neighbor not in visited:
                    g_new = g + weight
                    f_new = g_new + h_table.get(neighbor, 0)
                    heapq.heappush(queue, (f_new, g_new, neighbor, path + [neighbor]))
    return None, float('inf')

# --- Execution ---
start_node = 'A'
goal_node = 'H'

print("--- A* Search ---")
a_star_path, a_star_cost = a_star_search(graph_c, start_node, goal_node, heuristics)
if a_star_path:
    print(f"starting point :{start_node}")
    print(f"ending or goal node:{goal_node}")
    print(f"Path: {' -> '.join(a_star_path)}")
    print(f"Total Actual Cost: {a_star_cost}")
    print("saugat tamang")
else:
    print("No path found.")