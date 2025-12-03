"""AOC 2025 - Day 3, Part 2"""

def read_input(file_path: str) -> str:
    """Reads the input file and returns the content as a string."""

    data = []
    with open(file_path, 'r') as file:
        for line in file:
            data.append(line.strip())
    return data

def compute_solution(data: str, keep=12) -> int:
    """Computes the solution for Day 3, Part 2."""
    solution = 0

    for line in data:
        to_remove = len(line) - keep  # number of digits to remove
        stack = []

        for digit in line:
            # Remove smaller digits from stack if to_remove > 0
            while to_remove and stack and stack[-1] < digit:
                stack.pop()
                to_remove -= 1
            stack.append(digit)  # Push the current digit onto the stack
        
        # If there are still digits to remove, pop from the end of the stack
        if to_remove > 0:
            for _ in range(to_remove):
                stack.pop(  )

        solution += int(''.join(stack[:keep]))

    return solution


def main():
    """Main function to execute the solution."""
    input_data = read_input('data_3.txt')
    solution = compute_solution(input_data)
    print(solution)
    
if __name__ == "__main__":
    main()