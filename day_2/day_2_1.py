"""AOC 2025 Day 2"""

def read_input(filename: str):
    """Read input"""
    with open(filename, 'r', encoding="utf_8") as file:
        raw_data = file.readlines()
        data = []
        for line in raw_data:
            data.append(line.strip().split(','))
        return data[0]

def count_invalid(data):
    "Count number of invalid entries in given ranges"

    count = 0
    for item in data:
        item = item.split('-')
        minimum = int(item[0])
        maximum = int(item[1])
    
        for number in range(minimum, maximum + 1):
            str_number = str(number)
            if len(str_number) % 2 == 0:
                idx = len(str_number) // 2
                first_num = str_number[:idx]
                second_num = str_number[idx:]
                if first_num == second_num:
                    count += number

        
    return count

def main():
    """Entry point"""
    filename = "test_data.txt"
    filename = "data_2.txt"

    data = read_input(filename)
    invalid = count_invalid(data)

    print(invalid)

if __name__ == "__main__":
    main()
