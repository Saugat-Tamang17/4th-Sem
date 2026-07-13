
graph = {
    'A': {'B': 22, 'D': 30, 'E': 25},
    'B': {'A': 22, 'C': 20, 'D': 11},
    'C': {'B': 20},
    'D': {'A': 30, 'B': 11, 'F': 10},
    'E': {'A': 25, 'F': 25, 'G': 40},
    'F': {'D': 10, 'E': 25, 'G': 12},
    'G': {'E': 40, 'F': 12, 'H': 6},
    'H': {'G': 6}
}


def print_undirected_graph(g):
    print("Node -> (Neighbor: Weight)")
    print("--------------------------")
    for node, edges in g.items():
        connections = ", ".join([f"({neighbor}: {weight})" for neighbor, weight in edges.items()])
        print(f"  {node}  ->  {connections}")


print_undirected_graph(graph)