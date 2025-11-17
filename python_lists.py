# Lists in Python are used to store multiple items in a single variable.
# Lists are ordered, changeable (mutable), and allow duplicate values.

my_list = [10, 20, 30, 40, 50]
print("Original list:", my_list)

#getting lenght of the list
my_list_length= len(my_list)
print("Length of the list:", my_list_length)

#indexing and slicing
first_element = my_list[0]
print("First element:", first_element)
#slicing means accessing a range of elements in a list
sublist = my_list[1:4] # 1 means start index, 4 means end index (not inclusive)
print("Sublist (1-4):", sublist)