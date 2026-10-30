def dfs_recursive(graph, current_node, visited=None, traversal_order=None):
    if visited is None:
        visited = set()
    if traversal_order is None:
        traversal_order = []

    # Mark the current node as visited and log it
    visited.add(current_node)
    traversal_order.append(current_node)
    print(f"-> Visited node: {current_node}")

    # Recursively visit all unvisited neighbors
    for neighbor in graph[current_node]:
        if neighbor not in visited:
            print(f"   Moving deeper to neighbor: {neighbor}")
            dfs_recursive(graph, neighbor, visited, traversal_order)
            
    return traversal_order


def dfs_iterative(graph, start_node):
    visited = set()
    stack = [start_node]
    traversal_order = []

    print(f"\nStarting Iterative DFS Traversal from node: {start_node}")

    while stack:
        # Pop a vertex from the top of the stack (LIFO)
        current_node = stack.pop()

        if current_node not in visited:
            visited.add(current_node)
            traversal_order.append(current_node)
            print(f"-> Visited node: {current_node}")

            # Push unvisited neighbors onto the stack
            # Reversed list preservation matches traditional left-to-right processing order
            for neighbor in reversed(graph[current_node]):
                if neighbor not in visited:
                    stack.append(neighbor)
                    
    return traversal_order


# --- Execution Flow ---
if __name__ == "__main__":
    # Defining a sample graph using an adjacency list
    # Visual Layout:
    #      A
    #     / \
    #    B   C
    #   /   / \
    #  D   E   F
    sample_graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['E', 'F'],
        'D': [],
        'E': [],
        'F': []
    }

    print("=" * 40)
    print("      DFS TRAVERSAL EXTENSION")
    print("=" * 40)
    
    print("Executing Recursive DFS:")
    recursive_result = dfs_recursive(sample_graph, 'A')
    print(f"Final Recursive DFS Order: {recursive_result}")
    
    print("-" * 40)
    
    iterative_result = dfs_iterative(sample_graph, 'A')
    print(f"Final Iterative DFS Order: {iterative_result}")
    print("=" * 40)
