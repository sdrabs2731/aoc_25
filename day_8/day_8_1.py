from typing import List
from math import dist


def read_input(file_path: str) -> List[tuple]:
    data = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            data.append(tuple(int(x) for x in line.strip().split(',')))
    return data


def calculate_distance(a, b):
    return dist(a, b)


# class UnionFind:
#     def __init__(self, elements):
#         self.parent = {e: e for e in elements}
#         self.size   = {e: 1 for e in elements}

#     def find(self, x):
#         if self.parent[x] != x:
#             self.parent[x] = self.find(self.parent[x])
#         return self.parent[x]

#     def union(self, a, b):
#         ra = self.find(a)
#         rb = self.find(b)
#         if ra == rb:
#             return  # already connected
#         # union by size
#         if self.size[ra] < self.size[rb]:
#             ra, rb = rb, ra
#         self.parent[rb] = ra
#         self.size[ra] += self.size[rb]


def build_circuits(data):
    n = len(data)

    circuits = []

    count = 0
    while count < 10:
        min_distance = float('inf')
        point_one = None
        point_two = None
        for i in range(n):
            for j in range(i + 1, n):
                distance = calculate_distance(data[i], data[j])
                if distance < min_distance:
                    min_distance = distance
                    point_one = data[i]
                    point_two = data[j]
        
        circuits.append([point_one, point_two])

        count += 1
    
    return circuits
    

    # return the list of circuit sizes
    # return sorted(list(circuits.values()), reverse=True)

from math import prod
def main():
    input_data = read_input("test_8.txt")
    circuits = build_circuits(input_data)
    
    print("Circuit sizes:", circuits)
    # print("Number of circuits:", len(circuits))


if __name__ == "__main__":
    main()
