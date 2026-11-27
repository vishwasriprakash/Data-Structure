# Unpack Tuples:

print()

print("Unpack Tuples:-")
print()

fruits = ("apple","banana","orange")

(green, blue, red) = fruits
print(green)
print(blue)
print(red)
print()

fruits = ("apple","banana","orange","kiwi","mango","melon")

(green, blue, *red) = fruits
print(green)
print(blue)
print(red)
print()

fruits = ("apple","banana","orange","kiwi","mango","melon")

(green, *blue, red) = fruits
print(green)
print(blue)
print(red)
print()

fruits = ("apple","banana","orange","kiwi","mango","melon")

(*green, blue, red) = fruits
print(green)
print(blue)
print(red)
print()

# Loop Tuple

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

# Method	                            Description
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found