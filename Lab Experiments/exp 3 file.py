
from collections import deque

def water_jug(capacity1, capacity2, target):
    queue = deque([(0, 0)])
    visited = set()
    parent = {}

    start = (0, 0)
    visited.add(start)
    parent[start] = None

    while queue:
        x, y = queue.popleft()

        if x == target or y == target:
            path = []
            state = (x, y)

            while state is not None:
                path.append(state)
                state = parent[state]

            path.reverse()

            print("Solution found:")
            for step, (a, b) in enumerate(path):
                print(f"Step {step}: Jug 1 = {a} L, Jug 2 = {b} L")
            return

        next_states = [
            (capacity1, y),  # Fill Jug 1
            (x, capacity2),  # Fill Jug 2
            (0, y),          # Empty Jug 1
            (x, 0),          # Empty Jug 2
            (x - min(x, capacity2 - y),
             y + min(x, capacity2 - y)),  # Pour Jug 1 into Jug 2
            (x + min(y, capacity1 - x),
             y - min(y, capacity1 - x))   # Pour Jug 2 into Jug 1
        ]

        for state in next_states:
            if state not in visited:
                visited.add(state)
                parent[state] = (x, y)
                queue.append(state)

    print("No solution possible.")

# Main program
jug1 = int(input("Enter capacity of Jug 1: "))
jug2 = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target amount: "))

if jug1 < 0 or jug2 < 0 or target < 0:
    print("Capacities and target must be non-negative.")
elif target == 0:
    print("Target amount is 0. No steps required.")
elif target > max(jug1, jug2):
    print("Target cannot be measured in either jug.")
else:
    water_jug(jug1, jug2, target)
