from collections import deque

def bfs(graph, start_node):
    # Keep track of all visited nodes to avoid processing them multiple times
    visited = set()
    
    # Create a FIFO queue for BFS and enqueue the starting node
    queue = deque([start_node])
    
    # Mark the start node as visited
    visited.add(start_node)
    
    # Store the final sequence of nodes visited during traversal
    traversal_order = []

    print(f"Starting BFS Traversal from node: {start_node}\n")

    while queue:
        # Dequeue a vertex from the front of the queue
        current_node = queue.popleft()
        traversal_order.append(current_node)
        print(f"-> Visited node: {current_node}")

        # Get all adjacent neighbors of the current node
        for neighbor in graph[current_node]:
            # If a neighbor hasn't been visited yet, mark it visited and enqueue it
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                print(f"   Enqueued unvisited neighbor: {neighbor}")
                
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
    print("      BFS TRAVERSAL EXTENSION")
    print("=" * 40)
    
    # Execute the BFS algorithm starting from node 'A'
    result = bfs(sample_graph, 'A')
    
    print("=" * 40)
    print(f"Final BFS Traversal Order: {result}")
    print("=" * 40)
