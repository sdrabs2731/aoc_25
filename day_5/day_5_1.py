"""AOC 2025 - Day 5, Part 1."""

from typing import List, Tuple


def read_input(file_path: str) -> Tuple[List[str], List[str]]:
    """Read the puzzle input file."""
    with open(file_path, "r", encoding="utf-8") as f:
        stripped_lines = f.read().splitlines()

    cut_line = 0
    for idx, item in enumerate(stripped_lines):
        if item == "":
            cut_line = idx
            break

    ranges = stripped_lines[:cut_line]
    ingredients = stripped_lines[cut_line + 1:]

    return ranges, ingredients


def calculate_solution(ranges: List[str], ingredients: List[str]) -> int:
    """Calculate the number of ingredients that fall within given ranges."""
    solution = 0
    marked = [False] * len(ingredients)

    for span in ranges:
        low_str, high_str = span.split("-")
        low = int(low_str)
        high = int(high_str)

        for idx, item in enumerate(ingredients):
            value = int(item)
            if low <= value <= high and not marked[idx]:
                solution += 1
                marked[idx] = True

    return solution


def main() -> None:
    """Execute the solution."""

    ranges, ingredients = read_input("data_5.txt")
    print(calculate_solution(ranges, ingredients))


if __name__ == "__main__":
    main()
