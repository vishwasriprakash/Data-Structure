# 0
# 0 1
# 0 1 2
# 0 1 2 3
# 0 1 2 3 4

row = int(input("Row: "))

for i in range(row):
    for j in range(i+1):
        print(j,end=" ")
    print()

print()

#         0
#       0 1
#     0 1 2
#   0 1 2 3
# 0 1 2 3 4

for i in range(row+1):
    for j in range(row-i):
        print(" ",end=" ")

    for j in range(i):
        print(j,end=" ")
    print()

print()

# 0 1 2 3 4
# 0 1 2 3
# 0 1 2
# 0 1
# 0

for i in range(row):
    for j in range(row-i):
        print(j,end=" ")
    print()

print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4

for i in range(1,row):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print()

# 1 2 3
# 1 2
# 1

for i in range(1,row):
    for j in range(1,row-i):
        print(j,end=" ")
    print()

# both have same output:

#for i in range(1,row+1):
#    for j in range(1,row-i):
#       print(j,end=" ")
#    print()

print()

# 1 2 3 4
# 1 2 3
# 1 2
# 1

for i in range(1,row+1):
    for j in range(1,row-i+1):
        print(j,end=" ")
    print()

print()

# 5
# 4 4
# 3 3 3
# 2 2 2 2
# 1 1 1 1 1

for i in range(row,0,-1):
    print((str(i) + " ") * (row-i+1))

print()

# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

for i in range(1,row+1):
    print((str(i) + " ") * (row-i+1))

print()

# 5
# 4 4
# 3 3 3
# 2 2 2 2
# 1 1 1 1 1

for i in range(row,0,-1):
    print((str(i) + " ") * (row-i+1))

print()

