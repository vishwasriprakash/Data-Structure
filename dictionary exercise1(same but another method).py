# Get the input from the user and display
# 1. Search the Name 2. Search the Mark 3. Find the Number of name by marks (Above 80 or 90)

dictionary = {}

a = int(input("How many Keys and Values do you want to Enter?: "))

for i in range(a):
    key = input("Name: ")
    value = int(input("Value: "))
    dictionary[key] = value

print(dictionary)
print()

print("Find the Mark using Student Name")
print()
search_name = input("Name: ")
print(dictionary.get(search_name))
print()

print("Find the Student Name using Mark")
print()
search_mark = int(input("Mark: "))
for key, value in dictionary.items():
    if value == int(search_mark):
        print("Name: "+key)

print()

print("Find the Student List by Mark")
print()
search_mark1 = int(input("Mark: "))
for key, value in dictionary.items():
    if value >= int(search_mark1):
        print("Name: "+key)
        print("Mark: "+str(value))

print()

