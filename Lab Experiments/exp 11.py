class MapColoringCSP:
    def __init__(self, variables, domains, neighbors):
        self.variables = variables  # List of regions/states (e.g., WA, NT, SA)
        self.domains = domains      # Dictionary of available colors for each region
        self.neighbors = neighbors  # Dictionary containing adjacency list of regions

    def is_consistent(self, variable, color, assignment):
        """Checks if assigning a color to a variable violates any constraints."""
        for neighbor in self.neighbors[variable]:
            if neighbor in assignment and assignment[neighbor] == color:
                return False
        return True

    def get_unassigned_variable_mrv(self, assignment):
        """MRV Heuristic: Returns the unassigned variable with the fewest remaining colors."""
        unassigned = [v for v in self.variables if v not in assignment]
        # Sort based on the number of legal colors remaining in their domain
        return min(unassigned, key=lambda v: len(self.domains[v]))

    def get_ordered_values_lcv(self, variable, assignment):
        """LCV Heuristic: Orders domain values based on how few choices they rule out for neighbors."""
        def count_conflicts(color):
            conflicts = 0
            for neighbor in self.neighbors[variable]:
                if neighbor not in assignment and color in self.domains[neighbor]:
                    conflicts += 1
            return conflicts

        # Sort colors so that the color with the minimum neighbor conflicts comes first
        return sorted(self.domains[variable], key=count_conflicts)

    def backtrack(self, assignment={}):
        """Core Backtracking algorithm framework to find a consistent assignment."""
        # Base Case: If all variables are assigned, CSP is solved successfully
        if len(assignment) == len(self.variables):
            return assignment

        # Select next variable using Minimum Remaining Values (MRV)
        var = self.get_unassigned_variable_mrv(assignment)

        # Order domain values using Least Constraining Value (LCV)
        for color in self.get_ordered_values_lcv(var, assignment):
            if self.is_consistent(var, color, assignment):
                assignment[var] = color

                # Move deeper down the recursion path
                result = self.backtrack(assignment)
                if result is not None:
                    return result

                # Backtrack step if path results in a dead-end failure
                del assignment[var]

        return None


# --- Execution Flow ---
if __name__ == "__main__":
    # 1. Define variables (States of Australia)
    states = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]

    # 2. Define uniform domains (3 colors available per state)
    available_colors = ["Red", "Green", "Blue"]
    state_domains = {state: list(available_colors) for state in states}

    # 3. Define constraints (Adjacency Matrix / Neighbors list)
    # Visual Adjacency Representation:
    # WA borders NT, SA
    # NT borders WA, SA, Q
    # SA borders WA, NT, Q, NSW, V
    # Q borders NT, SA, NSW
    # NSW borders Q, SA, V
    # V borders SA, NSW
    # T (Tasmania) is an island with 0 neighbors
    state_neighbors = {
        "WA": ["NT", "SA"],
        "NT": ["WA", "SA", "Q"],
        "SA": ["WA", "NT", "Q", "NSW", "V"],
        "Q": ["NT", "SA", "NSW"],
        "NSW": ["Q", "SA", "V"],
        "V": ["SA", "NSW"],
        "T": []
    }

    print("=" * 50)
    print("      MAP COLORING CONSTRAINT SATISFACTION PROBLEM")
    print("=" * 50)
    print(f"Available Colors: {available_colors}\n")

    # Initialize the CSP problem solver instance
    csp = MapColoringCSP(states, state_domains, state_neighbors)
    solution = csp.backtrack()

    # Display final structural results
    if solution:
        print("Successful Valid Map Coloring Assignment found:")
        print("-" * 50)
        for state, color in sorted(solution.items()):
            print(f" Region {state.ljust(4)} -> Allocated Color: {color}")
        print("-" * 50)
    else:
        print("No valid assignment satisfies the constraints with the provided colors.")
    print("=" * 50)
