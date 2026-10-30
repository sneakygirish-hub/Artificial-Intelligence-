import math

class GameNode:
    def __init__(self, name, value=None, children=None):
        self.name = name          # Identifiable label for tracking (e.g., "Node_B")
        self.value = value        # Terminal state utility score (None for internal decision steps)
        self.children = children if children else []

    def is_terminal(self):
        return len(self.children) == 0


def alpha_beta_search(node, depth, alpha, beta, is_maximizing):
    """
    Core Alpha-Beta Pruning Algorithm implementation.
    alpha: The best score the Maximizer can guarantee so far (starts at -inf).
    beta: The best score the Minimizer can guarantee so far (starts at +inf).
    """
    # Base case: if we hit a leaf node, return its static value
    if node.is_terminal():
        print(f"[Leaf Evaluated] {node.name} = {node.value}")
        return node.value

    if is_maximizing:
        max_evaluation = -math.inf
        print(f"\n[MAX Turn] Visiting Node {node.name} | Current α={alpha}, β={beta}")
        
        for child in node.children:
            evaluation = alpha_beta_search(child, depth + 1, alpha, beta, False)
            max_evaluation = max(max_evaluation, evaluation)
            
            # Update Alpha tracker value
            alpha = max(alpha, max_evaluation)
            
            # Pruning condition checking
            if beta <= alpha:
                print(f"   !!! PRUNING TRIGGERED at Node {node.name} !!!")
                print(f"   Skipping remaining branches because β ({beta}) <= α ({alpha})")
                break  # Cut off the remaining sibling nodes
                
        return max_evaluation

    else:
        min_evaluation = math.inf
        print(f"\n[MIN Turn] Visiting Node {node.name} | Current α={alpha}, β={beta}")
        
        for child in node.children:
            evaluation = alpha_beta_search(child, depth + 1, alpha, beta, True)
            min_evaluation = min(min_evaluation, evaluation)
            
            # Update Beta tracker value
            beta = min(beta, min_evaluation)
            
            # Pruning condition checking
            if beta <= alpha:
                print(f"   !!! PRUNING TRIGGERED at Node {node.name} !!!")
                print(f"   Skipping remaining branches because β ({beta}) <= α ({alpha})")
                break  # Cut off the remaining sibling nodes
                
        return min_evaluation


# --- Execution Flow ---
if __name__ == "__main__":
    print("=" * 65)
    print("           ALPHA-BETA PRUNING ADVERSARIAL TREE EXPLORER")
    print("=" * 65)

    # 1. Constructing a standard 3-layer deep custom search tree
    # Deepest Level: Terminal Leaf Nodes with explicit hardcoded static evaluations
    n1 = GameNode("Leaf_1", value=3)
    n2 = GameNode("Leaf_2", value=5)
    n3 = GameNode("Leaf_3", value=6)
    
    n4 = GameNode("Leaf_4", value=0)
    n5 = GameNode("Leaf_5", value=1)
    n6 = GameNode("Leaf_6", value=2)
    
    n7 = GameNode("Leaf_7", value=8)
    n8 = GameNode("Leaf_8", value=9)
    n9 = GameNode("Leaf_9", value=12)

    # Middle Level: Branching Decision Layers
    branch_B = GameNode("Branch_B", children=[n1, n2, n3])
    branch_C = GameNode("Branch_C", children=[n4, n5, n6])
    branch_D = GameNode("Branch_D", children=[n7, n8, n9])

    # Top Level: Root Node
    root_node = GameNode("Root_A", children=[branch_B, branch_C, branch_D])

    # 2. Execute Alpha-Beta Search from Root
    # Setting initial Alpha to -infinity and Beta to +infinity
    optimal_score = alpha_beta_search(
        node=root_node, 
        depth=0, 
        alpha=-math.inf, 
        beta=math.inf, 
        is_maximizing=True
    )

    print("\n" + "=" * 65)
    print(f"Optimal Score for Max Player from Root: {optimal_score}")
    print("=" * 65)
