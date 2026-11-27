# Get the Input from the user and store the key and value data:

dictionary = {}

a = int(input("How many numbers: "))

for x in range(a):
    key = input("Key: ")
    value = input("Value: ")
    dictionary[key] = value

print(dictionary)
print()

