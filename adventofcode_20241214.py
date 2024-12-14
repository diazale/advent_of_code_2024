import numpy as np

f = open("20241214_input.txt","r")
in_data = f.read()
f.close()

#print(in_data)

# Given the starting position and the velocity per second, find the position of each robot after each second
# Robots "teleport" at the edge (i.e. their position is modulo whatever the boundary is)
# My grid is 101 tiles wide and 103 tiles tall (i.e. last indices are 100 and 102)
x_lim = 101
y_lim = 103

robots = 0
pos = []
vel = []

for line in in_data.split("\n"):
    # Import positions and velocities
    pos.append([int(i) for i in line.split()[0][2:].split(",")])
    vel.append([int(i) for i in line.split()[1][2:].split(",")])

    robots+= 1

updated_pos = []

seconds = 100
for robot in range(robots):
    # Iterate over all robots
    cur_pos = pos[robot][:]
    cur_vel = vel[robot][:]

    cur_pos[0] = (cur_pos[0] + cur_vel[0]*seconds) % x_lim
    cur_pos[1] = (cur_pos[1] + cur_vel[1]*seconds) % y_lim

    updated_pos.append([cur_pos[0],cur_pos[1]])

q1, q2, q3, q4 = 0,0,0,0
for robot in range(robots):
    # Quadrant 1: x < 50, y < 51
    # Quadrant 2: x < 50, y > 51
    # Quadrant 3: x > 50, y < 51
    # Quadrant 4: x > 50, y > 51
    if updated_pos[robot][0] < 50 and updated_pos[robot][1] < 51:
        q1+= 1
    elif updated_pos[robot][0] < 50 and updated_pos[robot][1] > 51:
        q2+= 1
    elif updated_pos[robot][0] > 50 and updated_pos[robot][1] < 51:
        q3+= 1
    elif updated_pos[robot][0] > 50 and updated_pos[robot][1] > 51:
        q4+=1

print(q1, q2, q3, q4)
print(q1*q2*q3*q4)

# Part 2: Visualize the output?
# Basically set up a grid of dots; if the coords appear in updated_pos, make an X
# Visualize the robot positions every second

# Use the safety score min_safety_score = 224969976 from the last solution
# If we have more unique robots we get a lower minimum safety score
# Look for a minimum in this value

v = 0
iviz = False

min_safety_score = 224969976

for second in range(0,10000):
    updated_pos = []
    q1, q2, q3, q4 = 0, 0, 0, 0
    for robot in range(robots):
        # Iterate over all robots
        cur_pos = pos[robot][:]
        cur_vel = vel[robot][:]

        cur_pos[0] = (cur_pos[0] + cur_vel[0] * second) % x_lim
        cur_pos[1] = (cur_pos[1] + cur_vel[1] * second) % y_lim

        updated_pos.append([cur_pos[0], cur_pos[1]])

        if updated_pos[robot][0] < 50 and updated_pos[robot][1] < 51:
            q1 += 1
        elif updated_pos[robot][0] < 50 and updated_pos[robot][1] > 51:
            q2 += 1
        elif updated_pos[robot][0] > 50 and updated_pos[robot][1] < 51:
            q3 += 1
        elif updated_pos[robot][0] > 50 and updated_pos[robot][1] > 51:
            q4 += 1

    safety_score = q1*q2*q3*q4

    if safety_score < min_safety_score:
        print("New score", second, safety_score)
        min_safety_score = safety_score
        iviz = True #7892?

    if iviz:
        viz = []  # Set up the grid as a list of lists
        for x in range(x_lim):
            viz.append([])

            for y in range(y_lim):
                if [x,y] in updated_pos:
                    viz[x].append("X")
                else:
                    viz[x].append(".")
        for v in viz:
            print(v)

        iviz = False
        print()