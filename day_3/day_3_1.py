"""AOC 2025 - Day 3, Part 1"""

def read_input(file_path: str) -> str:
    """Reads the input file and returns the content as a string."""

    data = []
    with open(file_path, 'r') as file:
        for line in file:
            raw = line.strip()
            data.append(raw)
    return data

def compute_solution(data: str) -> int:
    """Computes the solution for Day 3, Part 1."""
    maximums = []
    maximums_two = []
    for line in data:
       

        maximum = ''
        max2 = ''
        for idx, char in enumerate(line):
            if char > maximum and idx != len(line) - 1:
                maximum = char
                loc_one = idx
        
        for idx, char in enumerate(line[loc_one + 1:]):
            if char > max2:
                max2 = char
                loc_two = idx


        maximums.append((maximum, loc_one))
        maximums_two.append((max2, loc_two))
    
    print(maximums)
    print(maximums_two)

    zipped = list(zip(maximums, maximums_two))
    print(zipped)

    solution = 0

    for item in zipped:
        first_max, second_max = item
        solution += int((first_max[0]) + (second_max[0])) 
    return solution



def main():
    """Main function to execute the solution."""
    input_data = read_input('data_3.txt')
    print(input_data)
    solution = compute_solution(input_data)
    print(f"Solution Day 3, Part 1: {solution}")
    
if __name__ == "__main__":
    main()