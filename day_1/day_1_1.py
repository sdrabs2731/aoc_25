def part_two(data):
    point = 50
    zeros = 0

    for row in data:
        go_right = 1 if row[0] == "R" else -1
        amount = int(row[1:])

        zeros += amount // 100

        remainder = amount % 100

        new_point = 0
        if remainder > 0:
            new_point = point + go_right * remainder
        
        if (go_right > 0 and new_point >= 100) or (go_right < 0 and new_point < 1 and point > 0):
            zeros += 1

        point = (new_point + 100) % 100
    
    return zeros

def read_input(filename: str):
    with open(filename, 'r', encoding="utf_8") as file:
        return [line.strip() for line in file.readlines()]
    
if __name__ == "__main__":
    input_data = read_input("aoc_day1_1.txt")
    print("Part two: ", part_two(input_data))