# Tree structure and leaf values from the diagram
tree = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": ["H", "I"],
    "E": ["J", "K"],
    "F": ["L", "N"],
    "G": ["R", "S"],
}

leaf_values = {"H": 5, "I": 6, "J": 7, "K": 4, "L": 3, "N": 2, "R": 8, "S": 1}


# Minimax Algorithm
def minimax(node, is_maximizing):
    if node in leaf_values:
        return leaf_values[node]

    if is_maximizing:
        best_val = float("-inf")
        for child in tree[node]:
            val = minimax(child, False)
            best_val = max(best_val, val)
        return best_val
    else:
        best_val = float("inf")
        for child in tree[node]:
            val = minimax(child, True)
            best_val = min(best_val, val)
        return best_val


# Alpha-Beta Pruning Algorithm
def alpha_beta(node, alpha, beta, is_maximizing, pruned):
    if node in leaf_values:
        return leaf_values[node]

    if is_maximizing:
        best_val = float("-inf")
        for i, child in enumerate(tree[node]):
            val = alpha_beta(child, alpha, beta, False, pruned)
            best_val = max(best_val, val)
            alpha = max(alpha, best_val)
            if beta <= alpha:
                pruned.extend(tree[node][i + 1 :])  # Prune remaining siblings
                break
        return best_val
    else:
        best_val = float("inf")
        for i, child in enumerate(tree[node]):
            val = alpha_beta(child, alpha, beta, True, pruned)
            best_val = min(best_val, val)
            beta = min(beta, best_val)
            if beta <= alpha:
                pruned.extend(tree[node][i + 1 :])  # Prune remaining siblings
                break
        return best_val


# Driver Code
pruned_branches = []

optimal_value_minimax = minimax("A", is_maximizing=True)
optimal_value_ab = alpha_beta(
    "A", float("-inf"), float("inf"), is_maximizing=True, pruned=pruned_branches
)

print(f"Optimal Value (Minimax): {optimal_value_minimax}")
print(f"Optimal Value (Alpha-Beta Pruning): {optimal_value_ab}")
print(f"Pruned Branches/Subtrees: {pruned_branches}")