# List comprehensive

print("List Comprehension:-")
print()

fruits = ["apple", "banana", "cherry","kiwi","mango","melon"]
newlist = []

for x in fruits:
    if 'a' in x:
        newlist.append(x)

print(newlist)
print()

print("List Comprehension Other Method:-")
print()

fruits = ["apple", "banana", "cherry","kiwi","mango","melon"]
newlist = [x for x in fruits if 'a' in x]
print(newlist)
print()

# Sort Lists

# Ascending Sort Lists and Descending Sort List

print("Ascending Sort List:-")
print()

print("String Sort List:-")
print()

fruits = ["melon", "kiwi", "banana","apple","mango","cherry"]
fruits.sort()
print(fruits)
print()

print("Number Sort List:-")
print()

numbers = [10,5,7,2,6,9,8]
numbers.sort()
print(numbers)
print()

print("Descending Sort List:-")
print()

print("String Sort List:-")
print()

fruits = ["melon", "kiwi", "banana","apple","mango","cherry"]
fruits.sort(reverse=True)
print(fruits)
print()

print("Number Sort List:-")
print()

numbers = [10,5,7,2,6,9,8]
numbers.sort(reverse=True)
print(numbers)
print()

# Using reverse()
    # it only reverse the given list

print("Reverse the List:-")
print()

fruits = ["melon", "kiwi", "banana","apple","mango","cherry"]
fruits.reverse()
print(fruits)
print()

fruits = ["apple", "banana", "cherry","kiwi","mango","melon"]
fruits.reverse()
print(fruits)
print()

# Copy List

print("Copy List:-")
print()

print("Three Methods:-")
print()

print("Method 1:-")
print()

thislist = ["apple", "banana", "cherry"]
newlist = thislist.copy()
print(newlist)
print()

print("Method 2:-")
print()

thislist = ["apple", "banana", "cherry"]
newlist = list(thislist)
print(newlist)
print()

print("Method 3:-")
print()

thislist = ["apple", "banana", "cherry"]
newlist = thislist[:]
print(newlist)
print()

# List Join:

print("Join List:-")
print()

print("Three Methods:-")
print()

print("Method 1:-Join two list")
print()

list1 = ["a","b","c"]
list2 = [1,2,3]

list3 = list1 + list2
print(list3)
print()

print("Method 2:-Append list2 into list1")
print()

list1 = ["a","b","c"]
list2 = [1,2,3]

for x in list2:         # for x in list1:
    list1.append(x)     #   list2.append(x)

print(list1)            # print(list2)
print()                 # print()

print("Method 3:-Use the extend() method to add list2 at the end of list1")
print()

list1 = ["a","b","c"]
list2 = [1,2,3]

list1.extend(list2)     # list2.extend(list1)
print(list1)            # print(list2)
print()                 # print()

# Method	                Description
# append()	    Adds an element at the end of the list
# clear()	    Removes all the elements from the list
# copy()	    Returns a copy of the list
# count()	    Returns the number of elements with the specified value
# extend()	    Add the elements of a list (or any iterable), to the end of the current list
# index()	    Returns the index of the first element with the specified value
# insert()	    Adds an element at the specified position
# pop()	        Removes the element at the specified position
# remove()	    Removes the item with the specified value
# reverse()	    Reverses the order of the list
# sort()	    Sorts the list



