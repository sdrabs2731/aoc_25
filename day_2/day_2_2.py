"""AOC 2025 Day 2"""

def read_input(filename: str):
    """Read input"""
    with open(filename, 'r', encoding="utf_8") as file:
        raw_data = file.readlines()
        data = []
        for line in raw_data:
            data.append(line.strip().split(','))
        return data[0]

def split_even(str_number, factor):
    return [str_number[idx:idx + factor] for idx in range(0, len(str_number), factor)]

def count_invalid(data):
    "Count number of invalid entries in given ranges"

    count = 0
    for item in data: 
        item = item.split('-')
        minimum = int(item[0])
        maximum = int(item[1])
    
        for number in range(minimum, maximum + 1):
            factors = []
            str_number = str(number)

            for idx in range(1, int((len(str_number)**0.5) + 1)):
                if len(str_number) % idx == 0:
                    factors.append(idx)
                    if idx * idx != len(str_number):
                        factors.append(len(str_number) // idx)
            factors.sort()
            #print(number, factors)
            
            invalid = False
            for factor in factors:
                if invalid is True:
                    break
                split_string = split_even(str_number, factor)
                #print(split_string)
                if len(split_string) != 1:
                    if len(set(split_string)) == 1:
                        #print(number)
                        count += number
                        invalid = True
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
