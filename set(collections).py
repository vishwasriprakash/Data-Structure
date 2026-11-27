# Python Set - Complete Example Program

# Creating a Set:

print()

print("Creating a Set:-")
print()

my_set = {10,20,30,40}
print("Initial Set: ",my_set)
print()

# add()

print("add():-")
print()

my_set = {10,20,30,40}
my_set.add(50)
print("After add(50): ",my_set)
print()

# update()

print("update():-")
print()

my_set = {10,20,30,40,50}
my_set.update([60,70])
print("After update([60,70]): ",my_set)
print()

# remove()

print("remove():-")
print()

my_set = {10,20,30,40,50,60,70}
my_set.remove(20)
print("After remove(20): ",my_set)
print()

# discard()

print("discard():-")
print()

my_set = {10,20,30,40,50,60,70}
my_set.discard(100) # No error if element not present
print("After discard(100): ",my_set)
print()

my_set.discard(30)
print("After discard(30): ",my_set)
print()

# pop()

print("pop():-")
print()

my_set = {10,20,30,40,50,60,70}
removed_item = my_set.pop()
print("After pop(): ",my_set)
print("Popped Item: ",removed_item)
print()

# copy()

print("copy():-")
print()

my_set = {10,20,30,40,50,60,70}
copy_set = my_set.copy()
print("Copied Set: ",copy_set)
print()

# clear()

print("clear():-")
print()

temp_set = {1,2,3}
temp_set.clear()
print("After clear(): ",temp_set)
print()

# Set Operations (Join Sets)

print("Set Operations:-")
print()

A = {1,2,3,4}
B = {3,4,5,6}

print("\nSet A: ",A)
print("Set B: ",B)
print()

# union()

print("union():-")
print()

print("Union: ",A.union(B))
print()

# intersection()

print("intersection():-")
print()

print("Intersection: ",A.intersection(B))
print()

# difference()
    # The difference of two sets (A - B) is the set of all elements that belong to the first set (A) but do not belong to the second set (B).

print("difference():-")
print()

print("Difference(A-B): ",A.difference(B))
print()

# symmetric_difference()
    # The symmetric difference of two sets is the set containing all elements that belong to either of the sets, but not to both of them.

print("symmetric_difference():-")
print()

print("Symmetric Difference: ",A.symmetric_difference(B))
print()

# issubset()
    # A ⊆ B (A is a subset of B): Every element of set A is present in set B. Both sets can also be completely equal.

print("issubset():-")
print()

print("Is A Subset of B?: ",A.issubset(B))
print()

# issuperset()
    # If all elements of set B are inside set A, then A is a superset of B. This is the exact opposite of a subset (B is a subset of A).

print("issuperset():-")
print()

print("Is A Superset of B?: ",A.issuperset(B))
print()

# is disjoint()
    # Two or more sets are disjoint if they share no elements in common, meaning their intersection is an empty set.
    #A and B: If \(A = \{1, 2, 3\}\) and \(B = \{4, 5, 6\}\), then \(A \cap B = \emptyset\), making them disjoint.
    # Not Disjoint: If \(A = \{1, 2, 3\}\) and \(C = \{3, 4, 5\}\), they share the number 3, so they are overlapping and not disjoint.

print("isdisjoint():-")
print()

print("Are A and B disjoint?: ",A.isdisjoint(B))
print()

# in operator

print("in operator:-")
print()

print("Is 3 in A?: ",3 in A)
print()

# len()

print("len():-")
print()

print("Length of A: ",len(A))
print()

# max() and min()

print("max() and min():-")
print()

print("Max of A: ",max(A))
print("Min of A: ",min(A))
print()

# sorted()

print("sorted():-")
print()

A = {2,7,5,1,10}
print("Sorted A: ",sorted(A))
print()


