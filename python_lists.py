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

# concatenation of lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print("Concatenated list:", concatenated_list)

# list is mutable, meaning you can change its content. In strings, we saw that they are immutable. Meaning you cannot change them after they are created.
my_list[0] = 100
print("Modified list:", my_list)

# adding elements to end of the list using append() method
my_list.append(60)
print("List after appending 60:", my_list)

# removing elements at end of the list using pop() method. It also returns the removed element.
removed_element = my_list.pop()
print("Removed element:", removed_element)
print("List after popping an element:", my_list)

# removing element at specific index using pop(index) method
removed_element_at_index = my_list.pop(1) # removes element at index 1
print("Removed element at index 1:", removed_element_at_index)
print("List after popping element at index 1:", my_list)

# sort and reverse methods
# sorting means arranging the elements in ascending order
my_list.sort()
print("Sorted list:", my_list)

# reversing means arranging the elements in descending order
my_list.reverse()
print("Reversed list:", my_list)