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

def print_graph(g):
  print("Node --> Connected Nodes")
  print("-------------------------")
  for node,neighbour in g.items():
    print(f"{node}-->{', '.join(neighbour)}")

print_graph(graph)