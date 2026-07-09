# Basic Patterns

# 1 Patterns (witout space)

size = 5
for i in range(size):
    for j in range(size):
        print("*",end="")
    print()

# 2 Right-Angled Triangle Patterns

size = int(input("Enter a Number: "))
for i in range(1,size+1):
    for j in range(i):
        print("*", end="")
    print()

# 3 Inverted Right-Angle Triangle Patterns

size = 5

for i in range(size, 0 , -1):
    for j in range(i):
        print("*",end="")
    print()

# 4 Patterns (With Space)
    # (i)Pyramid Pattern
rows = 5

for i in range(1,rows+1):
    for j in range(rows - i):
        print(" ",end="")
    for k in range(2 * i - 1):
        print("*",end="")
    print()

    # (ii)
rows = 5
for i in range(rows - 1,0,-1):
    for j in range(rows - i):
        print(" ",end="")
    for k in range(2 * i - 1):
        print("*",end="")
    print()

    # Diamond Pattern
rows = 5
for i in range(1,rows+1):
    print(" " *(rows - i),end="")

    if i == 1:
        print("*")
    #elif i == rows:
     #   print("*" + " " * (2 *  rows - i))
    else :
        print("*" + " " * (2 * i - 3) + "*")

for i in range(rows - 1 , 0 , -1):
        print(" " * (rows - i)  , end="")
        if i == 1:
            print("*")
        else:
            print("*" + " " * (2 * i - 3) + "*")
