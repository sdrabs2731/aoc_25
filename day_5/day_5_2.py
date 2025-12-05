"""AOC 2025 - Day 5, Part 2"""

from typing import List, Tuple


def read_input(file_path: str) -> List[str]:
    """Reads input file and returns a list of ranges."""

    with open(file_path, 'r', encoding="utf-8") as db:
        stripped_lines = db.read().splitlines()

    cut_line = 0
    for idx, item in enumerate(stripped_lines):
        if item == '':
            cut_line = idx

    ranges = stripped_lines[:cut_line]

    return ranges

def calculate_solution(ranges: List[str]) -> int:
    """Calculates the solution based on input data."""

    solution = 0
    unique_ranges = set(ranges)

    ranges_sorted = sorted(
        unique_ranges,
        key=lambda r: int(r.split('-')[0])
    )

    converted: List[Tuple[int, int]] = []
    for line in ranges_sorted:
        low, high = line.split('-')
        span = (int(low), int(high))
        converted.append(span)

    merged: List[Tuple[int, int]] = []
    merged.append(converted[0])

    for idx, (start, end) in enumerate(converted):
        if idx == 0:
            continue

        last_start, last_end = merged[-1]

        if start <= last_end:
            merged[-1] = last_start, max(last_end, end)
        else:
            merged.append((start, end))

    for low, high in merged:
        solution += (high - low) + 1

    return solution


def main() -> None:
    """Main function to execute the solution logic."""

    ranges = read_input('data_5.txt')
    print(calculate_solution(ranges))


if __name__ == "__main__":
    main()