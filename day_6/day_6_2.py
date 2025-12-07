"""AOC 2025 - Day 6, Part 2"""

from typing import List
from math import prod


def read_input(file_path: str) -> List[str]:
    """Reads the input file and returns raw lines (no padding)."""
    lines: List[str] = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.rstrip("\n")
            lines.append(line)

    return lines


from typing import List, Tuple


def _print_grid_with_indices(grid: List[str]) -> None:
    """Helper to print the grid with column indices above (for debugging)."""

    if not grid:
        print("[DEBUG] Empty grid")
        return

    # Determine max width
    width = 0
    for line in grid:
        if len(line) > width:
            width = len(line)

    # First line: tens of column numbers
    tens = ""
    i = 0
    while i < width:
        tens_digit = i // 10
        if tens_digit > 0:
            tens += str(tens_digit)
        else:
            tens += " "
        i += 1

    # Second line: ones of column numbers
    ones = ""
    i = 0
    while i < width:
        ones += str(i % 10)
        i += 1

    print("[DEBUG] Grid with column indices:")
    print("      " + tens)
    print("      " + ones)

    row_index = 0
    while row_index < len(grid):
        # Print row with its index
        print(f"row {row_index:2d}: {grid[row_index]}")
        row_index += 1

    print()


def collate_problems(grid: List[str], debug: bool = False) -> List[Tuple[List[int], str]]:
    """Parse math problems from columns right-to-left."""

    if debug:
        _print_grid_with_indices(grid)

    # Determine maximum width so we know how many columns to scan
    width = 0
    for line in grid:
        if len(line) > width:
            width = len(line)

    height = len(grid)
    digit_rows = height - 1  # bottom row is operands

    collated: List[Tuple[List[int], str]] = []

    col = width - 1  # scan right-to-left
    while col >= 0:

        # Check if this is an empty separator column
        empty = True
        r = 0
        while r < height:
            ch = " "
            if col < len(grid[r]):
                ch = grid[r][col]
            if ch != " ":
                empty = False
                break
            r += 1

        if empty:
            if debug:
                print(f"[DEBUG] Column {col} is empty (separator), skipping.")
            col -= 1
            continue

        if debug:
            print(f"\n[DEBUG] Found non-empty column at {col}, starting new block scan.")

        # Start collecting a block of columns belonging to this problem
        cols_in_block: List[int] = []
        current = col

        while current >= 0:
            # Check if current column is empty
            is_empty = True
            r = 0
            while r < height:
                ch = " "
                if current < len(grid[r]):
                    ch = grid[r][current]
                if ch != " ":
                    is_empty = False
                    break
                r += 1

            if is_empty:
                if debug:
                    print(f"[DEBUG] Column {current} is empty, end of this block.")
                break  # end of this block

            cols_in_block.append(current)
            if debug:
                print(f"[DEBUG] Adding column {current} to current block.")
            current -= 1

        # Move scanning pointer
        col = current

        if debug:
            print(f"[DEBUG] Completed block columns (right-to-left): {cols_in_block}")

        # Find operator (bottom row)
        operator = None
        idx = 0
        while idx < len(cols_in_block) and operator is None:
            c = cols_in_block[idx]
            ch = " "
            if c < len(grid[height - 1]):
                ch = grid[height - 1][c]
            if ch in "+*":
                operator = ch
            idx += 1

        if operator is None:
            raise ValueError("Missing operator in problem block")

        if debug:
            print(f"[DEBUG] Operator found for this block: '{operator}'")

        # Extract numbers: each column (top→bottom) forms one number
        numbers: List[int] = []

        # columns must be processed RIGHT→LEFT (cols_in_block is already right→left)
        for c in cols_in_block:
            digits: List[str] = []

            if debug:
                print(f"\n[DEBUG] Processing column {c} for digits:")
                # Show a mini column view
                r_view = 0
                while r_view < height:
                    col_char = " "
                    if c < len(grid[r_view]):
                        col_char = grid[r_view][c]
                    print(f"    row {r_view}: '{col_char}'")
                    r_view += 1

            r = 0
            while r < digit_rows:
                ch = " "
                if c < len(grid[r]):
                    ch = grid[r][c]
                if ch.isdigit():
                    digits.append(ch)
                r += 1

            # Build number if any digits exist
            if digits:
                # Convert list of chars → int (no comprehension)
                num_str = ""
                i = 0
                if debug:
                    print("    [DEBUG] Digits collected in this column (top-to-bottom):", digits)
                while i < len(digits):
                    num_str += digits[i]
                    i += 1
                num_val = int(num_str)
                numbers.append(num_val)
                if debug:
                    print(f"    [DEBUG] Number formed from column {c}: {num_val}")
            else:
                if debug:
                    print(f"    [DEBUG] No digits in column {c}, skipping.")

        if debug:
            print(f"\n[DEBUG] Problem parsed from this block: numbers = {numbers}, operator = '{operator}'")
            print("[DEBUG] --------------------------------------------------------")

        # Add problem
        collated.append((numbers, operator))

    if debug:
        print("\n[DEBUG] All problems parsed:")
        i = 0
        while i < len(collated):
            nums, op = collated[i]
            print(f"    Problem {i}: {nums} {op}")
            i += 1
        print()

    return collated



def calculate_solution(collated):
    """Compute the sum of results of all cephalopod problems."""

    total = 0

    for numbers, oper in collated:
        if oper == "+":
            total += sum(numbers)
        else:
            total += prod(numbers)

    return total


def main() -> None:
    """Execute solution for day 6 part 2"""
    grid = read_input("test_6.txt")
    collated = collate_problems(grid, True)
    solution = calculate_solution(collated)
    print(solution)


if __name__ == "__main__":
    main()
