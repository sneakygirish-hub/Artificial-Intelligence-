import heapq

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def heuristic(state):
    distance = 0
    for i, tile in enumerate(state):
        if tile != 0:
            goal_pos = tile - 1
            distance += abs(i // 3 - goal_pos // 3)
            distance += abs(i % 3 - goal_pos % 3)
    return distance

def get_neighbors(state):
    neighbors = []
    blank = state.index(0)
    row, col = divmod(blank, 3)

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = row + dr, col + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            pos = nr * 3 + nc
            new_state = list(state)
            new_state[blank], new_state[pos] = new_state[pos], new_state[blank]
            neighbors.append(tuple(new_state))

    return neighbors

def solve(start):
    priority_queue = [(heuristic(start), 0, start)]
    parent = {start: None}
    cost = {start: 0}

    while priority_queue:
        _, g, current = heapq.heappop(priority_queue)

        if g != cost[current]:
            continue

        if current == GOAL:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]

        for neighbor in get_neighbors(current):
            new_cost = g + 1

            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                parent[neighbor] = current
                f = new_cost + heuristic(neighbor)
                heapq.heappush(priority_queue, (f, new_cost, neighbor))

    return None

def display(state):
    for i in range(0, 9, 3):
        print(" ".join("_" if x == 0 else str(x) for x in state[i:i+3]))
    print()

def main():
    try:
        start = tuple(map(int, input(
            "Enter 9 numbers (0 for blank), separated by spaces: "
        ).split()))

        if len(start) != 9 or set(start) != set(range(9)):
            print("Invalid input! Enter each number from 0 to 8 exactly once.")
            return

        inversions = sum(
            1 for i in range(9) for j in range(i + 1, 9)
            if start[i] != 0 and start[j] != 0
            and start[i] > start[j]
        )

        if inversions % 2 != 0:
            print("Puzzle is unsolvable.")
            return

        path = solve(start)

        if path is None:
            print("No solution found.")
            return

        print("\nSolution found!")
        print("Minimum number of moves:", len(path) - 1)

        for step, state in enumerate(path):
            print("Step", step)
            display(state)

    except ValueError:
        print("Invalid input! Enter integers separated by spaces.")

if __name__ == "__main__":
    main()
