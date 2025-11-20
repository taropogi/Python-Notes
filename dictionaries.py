# Dictionaries are used to store data values in key:value pairs.
# In javascript, they are similar to objects.
 
my_dict = {
    "name": "Alice",
    "age": 30,
}

the_name = my_dict["name"]
print("Name:", the_name)

# Dictionaries can also hold another dictionary as a value
my_dict["address"] = {
    "street": "123 Main St",    
    "city": "Wonderland"
}

# can also hold lists as values
my_dict["hobbies"] = ["reading", "traveling", "swimming"]
print("Updated dictionary:", my_dict)

# useful dictionary methods
keys = my_dict.keys()
print("Keys:", keys)

values = my_dict.values()
print("Values:", values)

items = my_dict.items()
print("Items:", items)