# Access List Items

print()

print("Access List Item:-")
print()

thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)

print()

thisset = {"apple", "banana", "cherry"}

print("apple" in thisset)
print()

thisset = {"apple", "banana", "cherry"}

print("apple" not in thisset)
print()

# Frozenset

thisset = frozenset({"apple", "banana", "cherry"})
print(thisset)
print()
print(type(thisset))
print()

