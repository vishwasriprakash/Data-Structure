# Get the input from the user and print the list:

list = []

a = int(input("How many People: "))

for i in range(a):
    b = input("Name: ")
    list.append(b)

print("List = ",list)
print()

# Get the input from the user and check whether the name is in the list or not:

list = []

a = int(input("How many People: "))

for i in range(a):
    b = input("Name: ")
    list.append(b)

print("List = ",list)
print()

if "Hari" in list:
    print("Yes, The Name is in the list")
else:
    print("No,The Name is not in the list")
