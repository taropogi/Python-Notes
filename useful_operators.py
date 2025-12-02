# range - Generates a sequence of numbers within a specified range.

for nom in range(3,50,2): # 3,5,2 means start at 3, end before 50, step by 2
    print(nom)  # Outputs numbers from 3 to 4

    # range to list
my_range = range(5)  # Generates numbers from 0 to 4
my_list = list(my_range)  # Converts range to list
print(my_list)  # Outputs: [0, 1, 2, 3, 4]

# enumerate - Adds a counter to an iterable and returns it as an enumerate object.
my_list = ['apple', 'banana', 'cherry']
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")

    #zip - Combines multiple iterables (like lists or tuples) into a single iterable of tuples.
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
# for item in zipped:
#     print(item)  # Outputs: (1, 'a'), (2, 'b'), (3, 'c')

# question - what if the lists are of different lengths?
list3 = [1, 2]
zipped_diff = zip(list1, list2, list3)
for item in zipped_diff:
    print(item)  # Outputs: (1, 'a', True), (2, 'b', False)

# the In operator - Checks for membership in an iterable (like a list, tuple, or string).
my_list = [10, 20, 30, 40, 50]
print(20 in my_list)  # Outputs: True
print(60 in my_list)  # Outputs: False

# min and max - Returns the smallest and largest items from an iterable or among multiple arguments.
numbers = [5, 2, 9, 1, 7]
print(min(numbers))  # Outputs: 1
print(max(numbers))  # Outputs: 9

# random - Provides functions to generate random numbers and make random selections.
from random import shuffle, randint # Importing only the shuffle function. random is a module in Python's standard library
my_list = [1, 2, 3, 4, 5]
shuffle(my_list)  # Shuffles the list in place
print(my_list)  # Outputs the shuffled list

random_number = randint(1, 10)  # Generates a random integer between 1 and 10 (inclusive)
print(random_number)  # Outputs the random number

# Input - Allows user input from the console.
user_input = input("Enter something: ")  # Prompts the user to enter something
print(f"You entered: {user_input}")  # Outputs what the user entered