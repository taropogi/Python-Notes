# Tuples in Python are used to store multiple items in a single variable.
# This is similar to lists, but tuples are immutable, meaning once they are created, their content cannot be changed.

t = (1, 2, 3, 4, 5)
print("Original tuple:", t)

# check lenght of the tuple
tuple_length = len(t)
print("Length of the tuple:", tuple_length)

# can mix different data types in a tuple
mixed_tuple = (1, "Hello", 3.14, True)
print("Mixed tuple:", mixed_tuple)

# indexing and slicing
first_element = t[0]
print("First element:", first_element)

# slicing means accessing a range of elements in a tuple
subtuple = t[1:4] # 1 means start index, 4 means end index (not inclusive)
print("Subtuple (1-4):", subtuple)

# built-in tuple methods
count_of_2 = t.count(2)
print("Count of 2 in tuple:", count_of_2)

index_of_3 = t.index(3) # will return the index of first occurrence of 3
print("Index of 3 in tuple:", index_of_3)

# proof that tuples are immutable
# the following line would raise an error
# t[0] = 10 # Uncommenting this line will cause a TypeError
