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
