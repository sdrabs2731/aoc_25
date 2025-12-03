"""AOC 2025 - Day 2"""

from math import isqrt

def read_input(filename: str):
    """Read input"""
    with open(filename, 'r', encoding="utf_8") as file:
        line = file.readline().strip()
        return line.split(',')

def get_factors(num_digits):
    """Compute all positive factors of 'num_digits' excluding the number itself"""

    factors = []
    limit = isqrt(num_digits)  # us isqrt to avoid floats

    # Check each integer from 1 to sqrt(number)
    for idx in range(1, limit + 1):
        if num_digits % idx == 0:
            factors.append(idx)

            # Add paired factor
            if idx * idx != num_digits:
                factors.append(num_digits // idx)

    factors.sort()

    # remove factor equal to number digits
    if factors and factors[-1] == num_digits:
        factors.pop()

    return factors

def split_groups(str_number, factor):
    "Create list of all possible groups"

    groups = []
    num_digits = len(str_number)

    # Iterate by group size
    for idx in range(0, num_digits, factor):
        groups.append(str_number[idx:idx + factor])

    return groups

def is_invalid(str_number, factors):
    """Calculate solution"""

    for factor in factors:
        split_string = split_groups(str_number, factor)

        # Test if all groups are the same
        if len(set(split_string)) == 1:
            return True

    return False

def main():
    """Entry point"""
    solution = 0
    filename = "data_2.txt"
    data = read_input(filename)

    for item in data:
        parts = item.split('-')
        minimum = int(parts[0])
        maximum = int(parts[1])

        for number in range(minimum, maximum + 1):
            str_number = str(number)
            num_digits = len(str_number)

            factors = get_factors(num_digits)

            # If number is invalid, add to solution total
            if is_invalid(str_number, factors):
                solution += number

    print(solution)

if __name__ == "__main__":
    main()
