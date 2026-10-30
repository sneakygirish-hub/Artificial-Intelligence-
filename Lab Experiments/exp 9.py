import itertools
import sys

def calculate_route_distance(route, distance_matrix):
    """Calculates the total distance of a given route path, returning to the start."""
    total_distance = 0
    num_cities = len(route)
    
    # Calculate path cost between all consecutive cities
    for i in range(num_cities):
        from_city = route[i]
        to_city = route[(i + 1) % num_cities] # Wraps around back to the starting city
        
        distance = distance_matrix[from_city][to_city]
        
        # If any city is unreachable, this route variant is invalid
        if distance == 0 and from_city != to_city:
            return float('inf')
            
        total_distance += distance
        
    return total_distance

def solve_tsp_brute_force(distance_matrix, cities):
    """Finds the optimal TSP tour by checking all possible permutations."""
    num_cities = len(cities)
    
    # Fix the starting city to eliminate redundant cyclic permutations
    start_city = 0
    other_cities = [i for i in range(num_cities) if i != start_city]
    
    best_distance = float('inf')
    best_route = None
    
    # Generate all unique combinations of the remaining cities
    for permutation in itertools.permutations(other_cities):
        # Build the full circular path: Start -> Permutation -> Start
        current_route = [start_city] + list(permutation)
        current_distance = calculate_route_distance(current_route, distance_matrix)
        
        # Update trackers if a shorter path layout is uncovered
        if current_distance < best_distance:
            best_distance = current_distance
            best_route = current_route
            
    # Append the starting city to the final output route to visually display the full loop
    final_route_path = [cities[node] for node in best_route] + [cities[start_city]]
    return final_route_path, best_distance

# --- Execution Flow ---
if __name__ == "__main__":
    # Names of the cities to visit
    city_names = ["Mumbai", "Delhi", "Bengaluru", "Kolkata"]
    
    # Symmetric Distance Matrix representation between index locations
    # example: matrix[0][1] is distance from Mumbai to Delhi
    sample_distance_matrix = [
        [0, 1400, 1000, 1650],  # Mumbai
        [1400, 0, 1700, 1300],  # Delhi
        [1000, 1700, 0, 1850],  # Bengaluru
        [1650, 1300, 1850, 0]   # Kolkata
    ]

    print("=" * 50)
    print("      TRAVELLING SALESMAN PROBLEM (TSP)")
    print("=" * 50)
    
    # Run structural calculation
    optimal_route, minimum_distance = solve_tsp_brute_force(sample_distance_matrix, city_names)
    
    # Format and display output results
    print("Optimal Route Path Sequence:")
    print(" -> ".join(optimal_route))
    print(f"\nMinimum Total Travel Distance: {minimum_distance} km")
    print("=" * 50)
