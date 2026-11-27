print()

thistuple = ("apple","banana","cherry")
print(thistuple)
print()

thistuple = ("apple","banana","cherry")
print(len(thistuple))
print()

thistuple = ("apple","banana","cherry","orange","kiwi","melon","mango")
print(thistuple[2:5])
print()

tuple1 = ("a","b","c")
tuple2 = (1,2,3)

tuple3 = tuple1 + tuple2
print(tuple3)
print()

# Multiple Tuples:

print("Multiple Tuples:-")
print()

fruits = ("apple","banana","cherry")
mytuple = fruits * 2
print(mytuple)
print()

# Change Tuple Values:

print("Change Tuple Values:-")
print()

x = ("apple","banana","cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
print()

# both are same but i explain the above program in below program

x = ("apple","banana","cherry")
y = list(x)
print("To Convert tuple to list\n",y)
y[1] = "kiwi"
x = tuple(y)
print("To Convert list to tuple and change 'banana' as 'kiwi'\n",x)
print()

# Convert to list:

print("Convert to List:-")
print()

thistuple = ("apple","banana","cherry")
y = list(thistuple)
y.append("orange")
print("Convert tuple to list\n",y)
thistuple = tuple(y)
print("Convert list to tuple\n",thistuple)
print()

# Add tuple to tuple:

print("Add Tuple to Tuple:-")
print()

thistuple = ("apple","banana","cherry")
y = ("orange",)
thistuple += y
print(thistuple)
print()

# Using Looping:

print("Using Looping to Print the tuple Values:-")
print()

thistuple = ("apple","banana","cherry")
for x in thistuple:
    print(x)
print()

thistuple = ("apple","banana","cherry")
i = 0
while i<len(thistuple):
    print(thistuple[i])
    i = i + 1
print()

# Count

print("Count:-")
print()

thistuple = (1,3,7,8,7,5,4,6,8,5)
x = thistuple.count(7)
print(x)
print()

# index

print("Index:-")
print()

thistuple = (1,3,7,8,7,5,4,6,8,5)
x = thistuple.index(8)
print(x)
print()

# All tuple exercise:

print("All tuple exercise:-")
print()

tuplex = (4,6,2,8,3,1)
print(tuplex)
print()

tuplex = tuplex + (9,)
print(tuplex)
print()

tuplex = tuplex[:5] + (15,20,25) + tuplex[:5]
print(tuplex)
print()

tuplex = (4,6,2,8,3,1)
listx = list(tuplex)
listx.append(30)
print("Convert tuple to list and add another Value\n",listx)
tuplex = tuple(listx)
print("Convert list to tuple\n",tuplex)
print()