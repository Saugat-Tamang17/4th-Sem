# Representing the weighted, directed graph using nested dictionaries
# Structure: { 'Parent_Node': { 'Child_Node': Weight, ... } }

graph = {
    'S': {'A': 1, 'G': 12},
    'A': {'B': 3, 'C': 1},
    'B': {'D': 3},
    'C': {'D': 1, 'G': 2},
    'D': {'G': 3},
    'G': {}  # Empty dictionary because G has no outgoing arrows
}

# Function to cleanly display the structure
def print_weighted_graph(g):
    print("Node -> (Neighbor: Weight)")
    print("--------------------------")
    for node, edges in g.items():
        if edges:
            connections = ", ".join([f"({neighbor}: {weight})" for neighbor, weight in edges.items()])
            print(f"  {node}  ->  {connections}")
        else:
            print(f"  {node}  ->  None (End Node)")

# Run the display function
print_weighted_graph(graph)