"""AOC 2025 Day 7 Part 1"""

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
                print("here")
                line.pop(pos - 1)
                line.insert(pos - 1, '|')
                line.pop(pos + 1)
                line.insert(pos + 1, '|')
                solution += 1

    for line in data:
        print(line)
    print(carrot_cnt)
    return solution

def main():
    """Execute the solution"""

    data = read_input("test_7.txt")


    solution = replace_dots(data)
    print(solution)


if __name__ == "__main__":
    main()