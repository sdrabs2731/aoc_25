"""AOC 2025 - Day 6, Part 1"""

from typing import List, Tuple
from math import prod


def read_input(file_path: str):
    """Reads the input file and returns the content as a list of lists of chars."""

    numbers = []


    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            digest = line.strip().split()
            numbers.append((digest))

    operands = numbers[-1]

    return numbers[:-1], operands


def collate_problems(numbers, operands):
    """Collate numbers and operands into proper math problems"""

    collated = []
    for idx, operand in enumerate(operands):
        temp = []
        for line in numbers:
            temp.append(int(line[idx]))

        temp.append(operand)
        collated.append(temp)

    return collated


def calculate_solution(collated):
    """Calculate the solution for day 6 part 1"""

    solution = 0

    for problem in collated:
        if problem[-1] == '+':
            solution += sum(problem[:-1])
        else:
            solution += prod(problem[:-1])

    return solution


def main() -> None:
    """Exectute solution"""

    numbers, operands = read_input("data_6.txt")
    collated = collate_problems(numbers, operands)
    solution = calculate_solution(collated)

    print(numbers, operands)
    print(collated)
    print(solution)


if __name__ == "__main__":
    main()
