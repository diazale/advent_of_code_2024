import numpy as np

# Import data
f = open("20241213_input.txt","r")
in_data = f.read()
f.close()

tokens = 0
extra = 0 # 10000000000000 for part 2

for d in in_data.split("\n"):
    if d.startswith("Button A:"):
        a = np.array([int(d.split()[2][2:-1]), int(d.split()[3][2:])], dtype=np.int64)
    elif d.startswith("Button B:"):
        b = np.array([int(d.split()[2][2:-1]), int(d.split()[3][2:])], dtype=np.int64)
    elif d.startswith("Prize"):
        c = np.array([int(d.split("X=")[1].split(",")[0]), int(d.split("Y=")[1])], dtype=np.int64) + extra
        # Now have enough information to calculate the solution

        denom = (a[0]*b[1] - b[0]*a[1])

        num1 = (c[0]*b[1] - b[0]*c[1])
        num2 = (a[0]*c[1] - c[0]*a[1])

        print("Numerators", num1, num2)

        if num1 % denom==0 and num2 % denom==0:
            # Check that an integer solution exists
            x0 = int((c[0]*b[1] - b[0]*c[1])/(a[0]*b[1] - b[0]*a[1]))
            x1 = int((a[0]*c[1] - c[0]*a[1])/(a[0]*b[1] - b[0]*a[1]))
            print("Integer solutions:", x0, x1)
            print("Tokens needed:", 3 * x0 + x1)
            tokens+=3*x0 + x1

print(tokens)


    #print(d)

#print(in_data)