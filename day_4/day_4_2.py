"""AOC 2025 - Day 4, Part 2"""

from typing import List, Tuple


DIRECTIONS: List[Tuple[int, int]] = [
    (-1, 0),   # north
    (1, 0),    # south
    (0, 1),    # east
    (0, -1),   # west
    (-1, 1),   # northeast
    (-1, -1),  # northwest
    (1, 1),    # southeast
    (1, -1),   # southwest
]


def read_input(file_path: str) -> List[List[str]]:
    """Reads the input file and returns the content as a list of lists of chars."""

    data: List[List[str]] = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            data.append(list(line.strip()))
    return data

def count_neighbors(loc: Tuple[int, int], grid: List[List[str]]) -> int:
    """Counts '@' in all 8 directions from current location"""

    row, col = loc
    max_row = len(grid)
    max_col = len(grid[0])

    count = 0
    for dr, dc in DIRECTIONS:
        nr, nc = row + dr, col + dc
        if 0 <= nr < max_row and 0 <= nc < max_col:
            if grid[nr][nc] == '@':
                count += 1

    return count


def calculate_solution(grid: List[List[str]]) -> int:
    """Calculates the solution based on the input data."""

    result = 0
    changed = True

    while changed:
        changed = False
        for row, line in enumerate(grid):
            for col, char in enumerate(line):
                if char == '@':
                    loc = (row, col)
                    count = count_neighbors(loc, grid)
                    if count < 4:
                        grid[row][col] = '.'
                        result += 1
                        changed = True

    return result


def main() -> None:
    """Main function to execute the solution logic."""

    grid = read_input('data_4.txt')
    result = calculate_solution(grid)
    print(result)


if __name__ == '__main__':
    main()
