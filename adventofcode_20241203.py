import re

# Looks like a parsing problem.
in_file = "20241203_input.txt"

f = open(in_file, "r")
in_data = f.read()
f.close()

#print(in_data)

# Part 1: look for mul(X,Y)
# Get each instance of this, multiply X and Y, add their products
data_copy = in_data
running_sum = 0

while data_copy.find("mul(") > -1:

    start_pos = data_copy.find("mul(") + 4
    end_pos = start_pos + data_copy[start_pos:].find(")")

    print(data_copy[start_pos-4:end_pos+1])

    try:
        split_point = data_copy[start_pos:end_pos].find(",") + start_pos
        print(data_copy[start_pos:split_point], data_copy[split_point+1:end_pos])
        first, second = int(data_copy[start_pos:split_point]), int(data_copy[split_point+1:end_pos])
        running_sum+= first*second
        print(running_sum)
        data_copy = data_copy[end_pos:]
    except:
        print("INVALID")
        data_copy = data_copy[start_pos:]