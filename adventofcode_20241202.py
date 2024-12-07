import numpy as np

in_file = "20241202_input.txt"

f = open(in_file, "r")
in_data = [[int(j) for j in i.split()] for i in f.read().split("\n")]
f.close()

#print(in_data)

# Part 1: Reports are safe if:
# 1. All values in a row are strictly decreasing or decreasing
# 2. The difference between sequential values is between 1 and 3
# Count the number of safe reports
# Basic approach: Loop through and see if the items meet the criteria
# More advanced: Get the diffs between all values?

safe_counts = 0

for report in in_data:
    arr_report = np.array(report)
    arr_report2 = np.array(report[1:])

    diff = arr_report[:-1] - arr_report2

    #print(arr_report, arr_report2, diff)

    if np.all(np.isin(diff, np.array([1, 2, 3]))) or np.all(np.isin(diff, np.array([-1, -2, -3]))):
        safe_counts+= 1

print(safe_counts)

# Part 2:
# We can remove a single level. If that makes it safe, we count the report as safe.
# What are the possibilities?
# First value is bad
# Last value is bad
# Exactly one 0 diff
# Large value like... [60, 67, 61, 62, 63]
## >[-7, 6, -1, -1]
## Dropping 67 would give [-1, -1, -1]
## [60, 67, 62, 63, 64]
## >[-7, 5, -1, -1]
## [60, 61, 67, 62, 63]
## >[-1, -6, 5, -1]
## [70, 68, 60, 67, 65]
## >[2, 8, -7, 2]

safe_counts = 0

for report in in_data:
    arr_report = np.array(report)
    arr_report2 = np.array(report[1:])

    diff = arr_report[:-1] - arr_report2

    print(arr_report, arr_report2, diff)

    if np.all(np.isin(diff, np.array([1, 2, 3]))) or np.all(np.isin(diff, np.array([-1, -2, -3]))):
        # Standard case
        safe_counts+= 1
        print("Safe.")
    elif np.all(np.isin(diff[1:], np.array([1, 2, 3]))) or np.all(np.isin(diff[:-1], np.array([1, 2, 3]))) \
        or np.all(np.isin(diff[1:], np.array([-1, -2, -3]))) or np.all(np.isin(diff[:-1], np.array([-1, -2, -3]))):
        # Only the first or last value is bad
        safe_counts+= 1
        print("Almost safe.")
    elif (np.sum(np.isin(diff, np.array([1, 2, 3]))) >= arr_report2.shape[0] - 1 and 0 in diff) \
            or (np.sum(np.isin(diff, np.array([-1, -2, -3]))) >= arr_report2.shape[0] - 1 and 0 in diff):
        # Only one zero
        safe_counts+= 1
        print("Almost safe.")
    elif np.sum(np.isin(diff, np.array([1, 2, 3]))) == arr_report2.shape[0] - 2:
        # There are exactly two consecutive bad values that sum to a good value
        # Case 1
        for d in range(diff.shape[0] - 1):
            if diff[d] > 3 and diff[d] + diff[d + 1] in [1, 2, 3]:
                safe_counts += 1
                print("Almost safe.")
            #print(diff[d], diff[d + 1], diff[d] + diff[d + 1])
    elif np.sum(np.isin(diff, np.array([-1, -2, -3]))) == arr_report2.shape[0] - 2:
        # There are exactly two consecutive bad values that sum to a good value
        # Case 2
        for d in range(diff.shape[0] - 1):
            if diff[d] < -3 and diff[d] + diff[d+1] in [-1,-2,-3]:
                safe_counts+= 1
                print("Almost safe.")

    else:
        print("Not safe.")

print(safe_counts)