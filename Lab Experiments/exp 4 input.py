
from itertools import permutations

def solve_cryptarithmetic():
    # Puzzle: SEND + MORE = MONEY
    letters = "SENDMORY"
    digits = "0123456789"

    for perm in permutations(digits, len(letters)):
        d = dict(zip(letters, perm))

        # First letters cannot be zero
        if d['S'] == '0' or d['M'] == '0':
            continue

        SEND = int(d['S'] + d['E'] + d['N'] + d['D'])
        MORE = int(d['M'] + d['O'] + d['R'] + d['E'])
        MONEY = int(
            d['M'] + d['O'] + d['N'] + d['E'] + d['Y']
        )

        if SEND + MORE == MONEY:
            print("Solution found:")
            print("SEND =", SEND)
            print("MORE =", MORE)
            print("MONEY =", MONEY)
            print()
            print(f"  {SEND}")
            print(f"+ {MORE}")
            print("------")
            print(f" {MONEY}")
            return

    print("No solution found.")

# Run the program
solve_cryptarithmetic()
