"""AOC 2025 Day 7 Part 2"""

from typing import List, Tuple


def read_input(file_path: str) -> List[List[str]]:
    """Reads the input file and returns the content as a list of lists of chars."""

    data: List[List[str]] = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            data.append(list(line.strip()))
    return data


def replace_dots(data):
    """Replace dots with split |"""


    # Find start and replace first dot
    start_idx = 0
    for idx, char in enumerate(data[0]):
        if char == 'S':
            start_idx = idx
            data[1].pop(start_idx)
            data[1].insert(start_idx, '|')

    solution = 0
    carrot_cnt = 0
    for idx, line in enumerate(data[2:], 2):
        for pos, char in enumerate(line):
            if data[idx - 1][pos] == '|' and line[pos] != '^':
                line.pop(pos)
                line.insert(pos, '|')
            if char == '^':
                carrot_cnt += 1
            if char == '^' and data[idx - 1][pos] == "|":
                line.pop(pos - 1)
                line.insert(pos - 1, '|')
                line.pop(pos + 1)
                line.insert(pos + 1, '|')
                solution += 1

    return solution, data

def count_all_routes(grid):
    # Create DP table without comprehensions

    total_rows = len(grid)
    total_cols = len(grid[0])

    route_count = []
    for row_index in range(total_rows):
        new_row = []
        for col_index in range(total_cols):
            new_row.append(0)
        route_count.append(new_row)

    # Locate start (S)
    for row_index in range(total_rows):
        for col_index in range(total_cols):
            if grid[row_index][col_index] == 'S':
                route_count[row_index][col_index] = 1

    # Process each row top → bottom
    for row_index in range(total_rows - 1):
        for col_index in range(total_cols):

            ways_to_reach_here = route_count[row_index][col_index]
            if ways_to_reach_here == 0:
                continue

            current_cell = grid[row_index][col_index]

            # ---------------------------------------
            # Move STRAIGHT DOWN
            # ---------------------------------------
            if current_cell == 'S' or current_cell == '|' or current_cell == '^':
                below_cell = grid[row_index + 1][col_index]
                if below_cell == '|' or below_cell == '^':
                    route_count[row_index + 1][col_index] += ways_to_reach_here

            # ---------------------------------------
            # Splitter logic: move DOWN-LEFT and DOWN-RIGHT
            # ---------------------------------------
            if current_cell == '^':

                # Down-left
                if col_index > 0:
                    down_left_cell = grid[row_index + 1][col_index - 1]
                    if down_left_cell == '|' or down_left_cell == '^':
                        route_count[row_index + 1][col_index - 1] += ways_to_reach_here

                # Down-right
                if col_index < total_cols - 1:
                    down_right_cell = grid[row_index + 1][col_index + 1]
                    if down_right_cell == '|' or down_right_cell == '^':
                        route_count[row_index + 1][col_index + 1] += ways_to_reach_here

    # ---------------------------------------
    # Sum the bottom row manually
    # ---------------------------------------
    total_routes = 0
    bottom_row_index = total_rows - 1
    for col_index in range(total_cols):
        total_routes += route_count[bottom_row_index][col_index]

    return total_routes


def main():
    """Execute the solution"""

    data = read_input("data_7.txt")


    solution, replaced_data = replace_dots(data)
    print(solution)

    part_2 = count_all_routes(replaced_data)
    print(part_2)


if __name__ == "__main__":
    main()
