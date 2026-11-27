# Find highest and lowest value using list:

list = []

a = int(input("How many Marks: "))

for x in range(a):
    b = int(input("Marks: "))
    list.append(b)

n = len(list)

high = list[0]
low = list[0]

for i in range(n):
    if list[i] > high:
        high = list[i]

    if list[i] < low:
        low = list[i]

print("Marks: ",list)
print("Highest: ",high)
print("Lowest: ",low)
print()

# Inbuilt Functions

print("Max: ",max(list))
print("Min: ",min(list))
print()