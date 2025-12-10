"""AOC 2025 - Day 9 - Part 1"""

from typing import List


def read_input(file_path: str) -> List[tuple]:
    data: List[tuple] = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            data.append(tuple(int(x) for x in line.strip().split(',')))
    return data


def calculate_area(point_one, point_two) -> int:
    """Return area of rectangle formed from two opposite corner points"""

    length: int = abs(point_one[0] - point_two[0]) + 1
    height: int = abs(point_one[1] - point_two[1]) + 1

    return length * height


def process_data(data) -> int:
    """Process all point and return largest area"""

    max_area: int = 0
    for i, item in enumerate(data):
        for j in range(i + 1, len(data)):
            area = calculate_area(item, data[j])
            max_area = max(max_area, area)

    return max_area


def main() -> None:
    """Execute solution"""

    data = read_input("data_9.txt")
    solution = process_data(data)
    print(f"Solution: {solution}")


if __name__ == "__main__":
    main()