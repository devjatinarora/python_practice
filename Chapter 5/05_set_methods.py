# Creating an empty set
b = set()
print(type(b))

# Adding values to an empty set
b.add(4)
b.add(4)
b.add(3)
b.add(3) # Adding a value repeadetly does not changes a set
b.add((4, 5, 6))

# b.add({4:5}) # Cannot add list or dictionary to sets
print(b)

print(len(b)) # Prints length of this set

# Removal of an item
b.remove(4) # Removes 4 from set b
b.remove(15) # Throws an error while trying to remove 15(which is not present in the set)
print(b)