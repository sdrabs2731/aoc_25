def read_input(filename="input.txt"):
    """
    Reads the puzzle text from an input file.
    Returns a list of machines, where each machine is:
    (goal_bitmask, button_bitmasks, num_lights)
    """
    machines = []

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            parts = line.split()

            # --- indicator pattern ---
            pattern = parts[0].strip("[]")
            num_lights = len(pattern)

            # convert pattern to goal bitmask
            goal = 0
            for i, ch in enumerate(pattern):
                if ch == "#":
                    goal |= (1 << i)

            # --- button bitmasks ---
            button_bitmasks = []
            for p in parts[1:]:
                if p.startswith("{"):  # joltage section - ignore
                    break
                p = p.strip("()")
                if p == "":
                    continue
                indices = list(map(int, p.split(",")))
                bm = 0
                for idx in indices:
                    bm |= (1 << idx)
                button_bitmasks.append(bm)

            machines.append((goal, button_bitmasks, num_lights))

    return machines


def fewest_presses_for_machine(goal, buttons):
    """
    Brute-force smallest number of button presses (subset of buttons)
    whose XOR equals the goal bitmask.
    """
    from itertools import combinations

    n = len(buttons)

    for k in range(n + 1):
        for combo in combinations(range(n), k):
            state = 0
            for idx in combo:
                state ^= buttons[idx]
            if state == goal:
                return k
    return None


def main():
    machines = read_input("data_10.txt")
    total = 0

    for goal, buttons, _ in machines:
        presses = fewest_presses_for_machine(goal, buttons)
        total += presses

    print(total)


if __name__ == "__main__":
    main()
