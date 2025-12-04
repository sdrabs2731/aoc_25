"""AOC 2025 - Day 3, Part 1 and Part 2"""

from typing import List


def read_input(file_path: str) -> List[str]:
    """Reads the input file and returns the content as a list of strings."""

    data: List[str] = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            data.append(line.strip())

    return data


def compute_solution(data: List[str], keep: int) -> int:
    """Computes the solution for Day 3, Parts 1 and 2."""
    solution: int = 0

    for line in data:
        to_remove: int = len(line) - keep  # number of digits to remove
        stack: List[str] = []

        for digit in line:
            # Remove smaller digits from stack if to_remove > 0
            while to_remove and stack and stack[-1] < digit:
                stack.pop()
                to_remove -= 1
            stack.append(digit)  # Push the current digit onto the stack

        # If there are still digits to remove, pop from the end of the stack
        if to_remove > 0:
            for _ in range(to_remove):
                stack.pop()

        solution += int(''.join(stack))

    return solution


def main() -> None:
    """Main function to execute the solution."""

    input_data: List[str] = read_input('test_3.txt')

    part_one: int = compute_solution(input_data, 2)
    part_two: int = compute_solution(input_data, 12)

    print(f"Part 1: {part_one}\nPart 2: {part_two}")


if __name__ == "__main__":
    main()
