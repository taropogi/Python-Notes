# for loops

my_iterable = [1, 2, 3, 4, 5]
for item in my_iterable:
    print(item)

#pring even/odd numbers from my_iterable
for item in my_iterable:
    if item % 2 ==0:
        print(f"Even number: {item}")
    else:
        print(f"Odd number: {item}")

# get sum using for loop
total = 0
for item in my_iterable:
    total += item
print(f"Sum of all items: {total}")

# loop through a string
my_string = "Hello"
for letter in my_string:
    print(letter)

# loop through a tuple
my_tuple = (10, 20, 30)
for number in my_tuple:
    print(number)

#tuple unpacking in for loop. This is like destructuring in other languages like JavaScript
my_list_of_tuples = [(1, 'a'), (2, 'b'), (3, 'c')]
for number, letter in my_list_of_tuples:
    print(f"Number: {number}, Letter: {letter}")

# loop through a dictionary. Dictionaries are like objects in JavaScript
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
for key in my_dict:
    print(f"Key: {key}, Value: {my_dict[key]}")

# using the .items() method to get key-value pairs
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

# using the .values() method to get values only
for value in my_dict.values():
    print(f"Value: {value}")