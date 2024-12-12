from copy import copy
from collections import defaultdict

input = "27 10647 103 9 0 5524 4594227 902936"
in_data = [int(i) for i in input.split()]

# 3 rules
# If it's a 0, make it a 1
# If it's an even number of digits split the number in two
# Otherwise, multiply by 2024

# Use defaultdict so key-value pairs initialize at 0
stones = defaultdict(int)
for i in in_data:
    stones[i]+= 1

for j in range(75):
    print("iteration", j+1)
    new_stones = defaultdict(int)
    # Apply the conditions for each key
    for stone in stones.keys():
        if stone==0:
            # Stone is 0
            new_stones[1]+= stones[0]
        elif len(str(stone)) % 2 == 0:
            # Even number of digits
            stone1 = int(str(stone)[:len(str(stone)) // 2])
            stone2 = int(str(stone)[len(str(stone)) // 2:])
            new_stones[stone1]+= stones[stone]
            new_stones[stone2]+= stones[stone]
        else:
            # Multiply by 2024
            new_stones[stone*2024]+= stones[stone]

    stones = copy(new_stones)
    print(stones)

total = sum([stone*stones[stone] for stone in stones])

print(total)
print("final number of unique stones", len(stones.keys()))
for k in sorted(stones.keys()):
    total+= stones[k]

print("Total stones", total)