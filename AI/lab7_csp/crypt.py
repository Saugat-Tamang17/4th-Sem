import itertools


def solve_cryptarithm(w1, w2, res):
    # Get all unique letters
    letters = list(set(w1 + w2 + res))

    # Try all possible digit combinations
    for p in itertools.permutations(range(10), len(letters)):
        d = dict(zip(letters, p))

        # Constraint: Leading letters cannot be zero
        if d[w1[0]] == 0 or d[w2[0]] == 0 or d[res[0]] == 0:
            continue

        # Convert words to numbers
        num1 = int("".join(str(d[c]) for c in w1))
        num2 = int("".join(str(d[c]) for c in w2))
        num_res = int("".join(str(d[c]) for c in res))

        # Check if addition holds
        if num1 + num2 == num_res:
            print("\n--- Solution Found ---")
            print(f"Letter Mapping: {d}")
            
            return

    print("No solution found.")


# Get user input
w1 = input("Enter Word 1: ").strip().upper()
w2 = input("Enter Word 2: ").strip().upper()
res = input("Enter Result Word: ").strip().upper()

solve_cryptarithm(w1, w2, res)