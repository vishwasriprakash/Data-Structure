# List

print("List")
print()

thislist = ["apple","banana","cherry","apple","cherry"]
print(thislist)
print()

thislist = ["apple","banana","cherry"]
print(len(thislist))
print()

# Access List

print("Access List")
print()

thislist = ["apple","banana","cherry"]
print(thislist[1])
print()

thislist = ["apple","banana","cherry"]
print(thislist[-1])
print()

thislist = ["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist[:4])
print()

thislist = ["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist[2:])
print()

thislist = ["apple","banana","cherry"]
if "apple" in thislist:
    print("Yes,'apple' is in the fruits list")
print()

# Change the List

print("Change the List")
print()

thislist = ["apple","banana","cherry"]
thislist[1] = "blackcurrant"
print(thislist)
print()

thislist = ["apple","banana","cherry","orange","kiwi","mango"]
thislist[1:3] = ["blackcurrant","watermelon"]
print(thislist)
print()

thislist = ["apple","banana","cherry"]
thislist[1:2] = ["blackcurrant","watermelon"]
print(thislist)
print()

thislist = ["apple","banana","cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
print()

# Add Item

print("Add Item")
print()

thislist = ["apple","banana","cherry"]
thislist.append("orange")
print(thislist)
print()

thislist = ["apple","banana","cherry"]
thislist.insert(2,"watermelon")
print(thislist)
print()

thislist = ["apple","banana","cherry"]
tropical = ["mango","pineapple","papaya"]
thislist.extend(tropical)
print(thislist)
print()

thislist = ["apple","banana","cherry"]
thistuple = ("kiwi","orange")
thislist.extend(thistuple)
print(thislist)
print()

# Remove Item

print("Remove Item")
print()

thislist = ["apple","banana","cherry"]
thislist.remove("banana")
print(thislist)
print()

thislist = ["apple","banana","cherry"]
thislist.pop(1)
print(thislist)
print()

thislist = ["apple","banana","cherry"]
thislist.pop()
print(thislist)
print()

thislist = ["apple","banana","cherry"]
del thislist[0]
print(thislist)
print()

thislist = ["apple","banana","cherry"]
del thislist
print()

thislist = ["apple","banana","cherry"]
thislist.clear()
print(thislist)
print()
