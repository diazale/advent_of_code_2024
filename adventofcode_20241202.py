in_file = "20241202_input.txt"

f = open(in_file, "r")
in_data = [[int(j) for j in i.split()] for i in f.read().split("\n")]
f.close()

print(in_data)

# Part 1: Reports are safe if:
# 1. All values in a row are strictly decreasing or decreasing
# 2. The difference between sequential values is between 1 and 3
# Count the number of safe reports

for report in in_data:
    for level in report:
        if 