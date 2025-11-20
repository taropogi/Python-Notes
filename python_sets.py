# Sets are used to store multiple items in a single variable.
# Sets are unordered, unchangeable (immutable), and do not allow duplicate values.
# keyword is unique here because sets do not allow duplicate values.

myset = {1, 2, 3, 4, 5}
print("Original set:", myset)

# add elements to a set using add() method
myset.add(6)
print("Set after adding 6:", myset)

# cast a list to a set to remove duplicates
mylist = [1, 2, 2, 3, 4, 4, 5]
myset_from_list = set(mylist)
print("Set from list (duplicates removed):", myset_from_list)