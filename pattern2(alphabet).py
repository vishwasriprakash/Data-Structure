# * * * * *
# *
# * * * * *
# *
# * * * * *

row = int(input("Row: "))
col = int(input("Column: "))

for i in range(1, row + 1):
    if i % 2 != 0: # The outer for loop controls the rows, and i % 2 != 0 checks whether the row number is odd.
                   # For odd rows it prints 5 stars, and for even rows it prints only 1 star.
        for j in range(col):
            print("*", end=" ")
        print()
    else:
        print("*")

print()