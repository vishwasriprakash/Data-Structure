# * * * * *
# * * * *
# * * *
# * *
# *

row = int(input("Row: "))

for i in range(row):
    for j in range(row-i):
        print("*",end=" ")
    print()

print()

                                                        # or

for i in range(row,0,-1):
    print("* " * i)

print()


# *
# * *
# * * *
# * * * *
# * * * * *

for i in range(row):
    for j in range(i+1):
        print("*",end=" ")
    print()

print()

                                                        # or

for i in range(1,row+1):
    print("* " * i)

print()


#         *
#       * *
#     * * *
#   * * * *
# * * * * *

for i in range(row+1):
    for j in range(row-i):
        print(" ",end=" ")

    for j in range(i):
        print("*",end=" ")
    print()

print()

                                              # or

for i in range(1,row+1):
    print(" " * (row-i) + "*" * i)

print()

# * * * * *
#   * * * *
#     * * *
#       * *
#         *

for i in range(row+1):
    for j in range(i):
        print(" ",end=" ")

    for j in range(row-i):
        print("*",end=" ")
    print()

print()

                                          # or

for i in range(row,0,-1):
    print(" " * (row-i) + "*" * i)

print()

# * * * * *
#  * * * *
#   * * *
#    * *
#     *

for i in range(row,0,-1):
    print(" " * (row-i) + "* " * i)

print()

#     *
#    * *
#   * * *
#  * * * *
# * * * * *

for i in range(1,row+1):
    print(" " * (row-i) + "* " * i)

print()

#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

for i in range(1,row+1):
    print(" " * (row-i) + "* " * i)
for i in range(row-1, 0, -1):
    print(" " * (row-i) +"* " * i)

print()

# * * * * *
# *       *
# *       *
# *       *
# * * * * *

for i in range(row):
    for j in range(row):
        if i == 0 or i == row-1 or j == 0 or j == row-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print()

# Butterfly Pattern

print("Butterfly Pattern")
# Upper Part
for i in range(1,row+1):
    print("*" * i + " " * (2*(row-i)) + "*" * i)

# Lower Part
for i in range(row,0,-1):
    print("*" * i + " " * (2*(row-i)) + "*" * i)

print()


