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
# remove a zero

safe_counts = 0

for report in in_data:
    arr_report = np.array(report)
    arr_report2 = np.array(report[1:])

    diff = arr_report[:-1] - arr_report2

    print(arr_report, arr_report2, diff)

    if np.sum(np.isin(diff, np.array([1, 2, 3]))) >= arr_report2.shape[0] - 1 or \
            np.sum(np.isin(diff, np.array([-1, -2, -3]))) >= arr_report2.shape[0] - 1:
        safe_counts+= 1
    print(safe_counts)