from collections import Counter

in_file = "20241201_input.txt"

f = open(in_file, "r")
in_data = f.read().split("\n")
left = [int(i.split("   ")[0]) for i in in_data]
right = [int(i.split("   ")[1]) for i in in_data]
f.close()

print(in_data)
print(left)
print(right)

# Part 1: Align the lists and find the differences, then sum the differences

diffs = []

for i in range(len(left)):
    diffs.append(abs(sorted(left)[i] - sorted(right)[i]))

print("Part 1 solution:", sum(diffs))

# Part 2: Find out how often items in the left list appear in the right list
# Multiply everything in the left list by its number of appearances in the right list
# Alternately, get a key-count of everything in the right list and check for appearances in the left list

right_count = dict(Counter(right))

similarity = 0

for rc in right_count.keys():
    if rc in left:
        similarity+= rc * right_count[rc]

print("Part 2 solution:", similarity)