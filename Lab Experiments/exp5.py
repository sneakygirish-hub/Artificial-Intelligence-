
from collections import deque

def solve_missionaries_cannibals():
    # State: (missionaries_left, cannibals_left, boat_position)
    # boat_position: 0 = left bank, 1 = right bank

    start = (3, 3, 0)
    goal = (0, 0, 1)

    # Possible boat passenger combinations
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    queue = deque([start])
    parent = {start: None}

    while queue:
        state = queue.popleft()
        m, c, boat = state

        if state == goal:
            path = []
            while state is not None:
                path.append(state)
                state = parent[state]

            path.reverse()

            print("Solution found:\n")
            for step, (ml, cl, b) in enumerate(path):
                mr = 3 - ml
                cr = 3 - cl

                side = "Left" if b == 0 else "Right"
                print(f"Step {step}:")
                print(f"  Left Bank  : {ml} Missionaries, {cl} Cannibals")
                print(f"  Right Bank : {mr} Missionaries, {cr} Cannibals")
                print(f"  Boat       : {side}\n")
            return

        for missionaries, cannibals in moves:
            if boat == 0:
                new_m = m - missionaries
                new_c = c - cannibals
                new_boat = 1
            else:
                new_m = m + missionaries
                new_c = c + cannibals
                new_boat = 0

            # Check bank limits
            if not (0 <= new_m <= 3 and 0 <= new_c <= 3):
                continue

            # Check safety on both banks
            left_safe = new_m == 0 or new_m >= new_c
            right_m = 3 - new_m
            right_c = 3 - new_c
            right_safe = right_m == 0 or right_m >= right_c

            if not (left_safe and right_safe):
                continue

            next_state = (new_m, new_c, new_boat)

            if next_state not in parent:
                parent[next_state] = (m, c, boat)
                queue.append(next_state)

    print("No solution exists.")

# Run the program
solve_missionaries_cannibals()
