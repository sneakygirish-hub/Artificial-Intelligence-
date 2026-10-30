import heapq

class Graph:
    def __init__(self):
        # Adjacency list representation: {node: [(neighbor, edge_cost), ...]}
        self.edges = {}
        # Heuristic values dictionary: {node: estimated_distance_to_target}
        self.heuristics = {}

    def add_edge(self, u, v, cost):
        self.edges.setdefault(u, []).append((v, cost))
        self.edges.setdefault(v, []).append((u, cost))  # Undirected graph

    def set_heuristic(self, node, value):
        self.heuristics[node] = value

    def get_neighbors(self, node):
        return self.edges.get(node, [])

    def get_h(self, node):
        return self.heuristics.get(node, 0)


def a_star_search(graph, start, goal):
    # Priority queue stores tuples of format: (f_score, current_node, path_taken, actual_g_score)
    # Priority is determined entirely by the f_score (index 0)
    open_set = []
    heapq.heappush(open_set, (graph.get_h(start), start, [start], 0))
    
    # Track the absolute minimum g_score (actual cost) found to each node so far
    shortest_g_scores = {start: 0}

    print(f"Starting A* Search from '{start}' to '{goal}'...\n")

    while open_set:
        f_score, current, path, g_score = heapq.heappop(open_set)
        
        print(f"[Exploring] Node: '{current}' | Current Path Cost (g): {g_score} | Total Est. Cost (f): {f_score}")

        # Goal verification
        if current == goal:
            return path, g_score

        # Process all neighboring connections
        for neighbor, edge_cost in graph.get_neighbors(current):
            tentative_g_score = g_score + edge_cost

            # If this path to neighbor is cheaper than any previously discovered path
            if neighbor not in shortest_g_scores or tentative_g_score < shortest_g_scores[neighbor]:
                shortest_g_scores[neighbor] = tentative_g_score
                
                # Evaluation Function: f(n) = g(n) + h(n)
                f_score_neighbor = tentative_g_score + graph.get_h(neighbor)
                new_path = list(path) + [neighbor]
                
                heapq.heappush(open_set, (f_score_neighbor, neighbor, new_path, tentative_g_score))
                print(f"   -> Enqueued neighbor '{neighbor}' (Calculated f = {tentative_g_score} + {graph.get_h(neighbor)} = {f_score_neighbor})")
                
        print("-" * 65)

    return None, float('inf')


# --- Execution Flow ---
if __name__ == "__main__":
    # Initialize our sample graph structure
    g = Graph()

    # Define Graph Edges and Travel Costs
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'C', 3)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 7)
    g.add_edge('D', 'E', 2)

    # Define Straight-Line Heuristics (Estimated distance remaining to Goal 'E')
    g.set_heuristic('A', 8)
    g.set_heuristic('B', 6)
    g.set_heuristic('C', 5)
    g.set_heuristic('D', 2)
    g.set_heuristic('E', 0)

    print("=" * 65)
    print("                A* SEARCH ALGORITHM SIMULATION")
    print("=" * 65)
    
    # Execute A* Search
    optimal_path, total_cost = a_star_search(g, 'A', 'E')
    
    print("=" * 65)
    if optimal_path:
        print("Optimal Shortest Path Found:")
        print(" -> ".join(optimal_path))
        print(f"\nAbsolute Minimum Path Cost: {total_cost}")
    else:
        print("Target Goal location is unreachable from the designated start point.")
    print("=" * 65)
