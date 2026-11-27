print()

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
print(thisdict)
print()

# Print the "brand" value of the dictionary

print("Print the 'brand' value of the dictionary:-")
print()

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
print(thisdict["brand"])
print()

# Duplicate values will overwrite existing values:

print("Duplicate values will overwrite existing values:-")
print()

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964,
    "year" : 2020
}
print(thisdict)
print()

# Get the value of the "model" key

print("Get the value of the 'model' key:-")
print()

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
x = thisdict["model"]
print(x)
print()

# Change Before and After of Key values:

print("Change Before and After of Key Values:-")
print()

car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

x = car.keys()

print("Before the Change:-\n",x)    # before the change

car["color"] = "white"

print("After the Change:-\n",x)     # after the change
print()

# change the "year" to 2018:

print("Change the 'year' to 2018")
print()

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

thisdict["year"] = 2018
print(thisdict)
print()

# add item

print("Add Item:-")
print()

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

thisdict["color"] = "red"
print(thisdict)
print()

# remove items

print("Remove Item:-")
print()

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

thisdict.pop("model")
print(thisdict)
print()

# Copy dictionary

print("Copy Dictionary:-")
print()

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

mydict = dict(thisdict)
print(mydict)
print()

# Nested Dictionary

print("Nested Dictionary:-")
print()

child1 = {
    "name" : "Emil",
    "year" : 2004
}

child2 = {
    "name" : "Tobias",
    "year" : 2007
}

child3 = {
    "name" : "Linus",
    "year" : 2011
}

myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}

print(myfamily)
print()