# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

row = int(input("Row: "))

for i in range(1,row+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print()

# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

for i in range(1,row+1):
    for j in range(1,row-i+2):
        print(j,end=" ")
    print()

print()

#         1
#       1 2
#     1 2 3
#   1 2 3 4
# 1 2 3 4 5

for i in range(1,row+1):
    for j in range(1,row-i+1):
        print(" ",end=" ")

    for j in range(1,i+1):
        print(j,end=" ")
    print()

print()

# 1 2 3 4 5
#   1 2 3 4
#     1 2 3
#       1 2
#         1

for i in range(1,row+1):
    for j in range(1,i):
        print(" ",end=" ")

    for j in range(1,row-i+2):
        print(j,end=" ")
    print()

print()

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

for i in range(1,row+1):
    print((str(i) + " ") * i)

print()

# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1

for i in range(row,0,-1):
    print((str(i) + " ") * i)

print()

# Floyd's Triangle:

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

num=1

print("Floyd's Triangle")

for i in range(1,row+1):
    for j in range(i):
        print(num,end=" ")
        num=num+1
    print()

print()

# Palindrome Pattern:

print("Palindrome Pattern")

for i in range(1,row+1):
    print(" " * (row-i) ,end="")
    for j in range(i,0,-1):
        print(j,end="")
    for j in range(2,i+1):
        print(j,end="")
    print()

print()



