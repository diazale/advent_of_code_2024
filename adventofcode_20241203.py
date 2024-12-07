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
        #print(data_copy[start_pos:split_point], data_copy[split_point+1:end_pos])
        first, second = int(data_copy[start_pos:split_point]), int(data_copy[split_point+1:end_pos])
        running_sum+= first*second
        #print(running_sum)
        data_copy = data_copy[end_pos:]
    except:
        #print("INVALID")
        data_copy = data_copy[start_pos:]

# Part 2:
# Scan for do() and don't()
# Count the values after a do(), ignore those after a don't()
# Basically look for a do() before the mul()
data_copy = in_data
running_sum = 0
#usevals =  True

while data_copy.find("mul(") > -1:
    if data_copy.find("don't()") < data_copy.find("mul("):
        # If we reach a don't(), look ahead til we get to a do()
        print("DON'T DO WHAT DONNY DON'T DOES")

        if data_copy.find("do()") > -1:
            # If there's a do(), jump to there
            print("DO DO WHAT DONNY DO DOES")
            data_copy = data_copy[data_copy.find("do()"):]
        else:
            # Otherwise, nothing left to do so exit the loop
            break

    start_pos = data_copy.find("mul(") + 4
    end_pos = start_pos + data_copy[start_pos:].find(")")

    print(data_copy[start_pos-4:end_pos+1])

    try:
        split_point = data_copy[start_pos:end_pos].find(",") + start_pos
        #print(data_copy[start_pos:split_point], data_copy[split_point+1:end_pos])
        first, second = int(data_copy[start_pos:split_point]), int(data_copy[split_point+1:end_pos])
        running_sum+= first*second
        print(running_sum)
        data_copy = data_copy[end_pos:]
    except:
        #print("INVALID")
        data_copy = data_copy[start_pos:]
