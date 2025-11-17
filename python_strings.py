my_string = "Hello, World!"
print(my_string)

# About escape sequences
# Escape sequences are used to insert characters that are illegal in a string
# For example, to insert a newline, use \n
my_string_with_newline = "Hello,\nWorld!"
print(my_string_with_newline)

# check the length of the string
length = len(my_string)
print("Length of the string:", length)

# indexing and slicing
# indexing means accessing individual characters in a string
first_character = my_string[0]
print("First character:", first_character)

#slicing means accessing a range of characters in a string
substring = my_string[0:5] # 0 means start index, 5 means end index (not inclusive)
print("Substring (0-5):", substring)

# reverse indexing means accessing characters from the end of the string
last_character = my_string[-1]
print("Last character:", last_character)

# using the 3rd parameter in slicing to define step
every_second_character = my_string[0:13:2] # 2 means step
print("Every second character:", every_second_character)

# reverse a string using step
reversed_string = my_string[::-1]
print("Reversed string:", reversed_string)

#Immutability of strings
# Strings are immutable, meaning you cannot change them after they are created
# For example, the following line would raise an error
# my_string[0] = "h"

#Concatenation in strings
greeting = "Hello"
name = "Alice"
full_greeting = greeting + ", " + name + "!"
print(full_greeting)

# String multiplication. It means repeating the string multiple times
repeat_hello = "Hello! " * 3
print(repeat_hello)

# python built-in string methods
upper_case = my_string.upper()
print("Upper case:", upper_case)

lower_case = my_string.lower()
print("Lower case:", lower_case)

# split method. Means splitting a string into a list of substrings based on a delimiter. It produces a list out of strings.
split_string = my_string.split(", ")
print("Split string:", split_string)

# formatting strings using f-strings and format() method
# first using format() method
age = 25
formatted_string1 = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string1)

# now using f-strings or formatted string literals
formatted_string2 = f"My name is {name} and I am {age} years old."
print(formatted_string2)