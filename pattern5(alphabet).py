# A
# A B
# A B C
# A B C D
# A B C D E

row = int(input("Row: "))

for i in range(1,row+1):
    for j in range(1,i+1): # (or) for i in range(i):
        print(chr(64+j),end=" ")  #  print(chr(65+j),end=" ")
    print()

print()

# A B C D E
# A B C D
# A B C
# A B
# A

for i in range(1,row+1):
    for j in range(1,row-i+2):
        print(chr(64+j),end=" ")
    print()

print()

#         A
#       A B
#     A B C
#   A B C D
# A B C D E

for i in range(1,row+1):
    for j in range(1,row-i+1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()

print()

# A B C D E
#   A B C D
#     A B C
#       A B
#         A

for i in range(1,row+1):
    for j in range(1,i):
        print(" ",end=" ")

    for j in range(1,row-i+2):
        print(chr(64+j),end=" ")
    print()

print()

# A
# B B
# C C C
# D D D D
# E E E E E

for i in range(row):
    print((chr(65+i) + " ") * (i+1))

print()

# E E E E E
# D D D D
# C C C
# B B
# A

for i in range(row,0,-1):
    print((chr(64+i) + " ") * i)

print()

