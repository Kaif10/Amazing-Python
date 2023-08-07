#Dictionaries help a lot while solving Data Structure and Algorithm problems.
#here's a short revision I did of them.

# Empty dictionary
my_dict = {}
my_dict = dict()

# Dictionary with key-value pairs
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

print(my_dict['name'])   # Output: 'John'
print(my_dict['age'])    # Output: 30

print(my_dict.get('name'))   # Output: 'John'
print(my_dict.get('gender')) # Output: None (key not found)
print(my_dict.get('gender', 'Unknown')) # Output: 'Unknown' (default value provided)

my_dict = {'name': 'John', 'age': 30}

# Adding a new key-value pair
my_dict['city'] = 'New York'
# Output: {'name': 'John', 'age': 30, 'city': 'New York'}

# Updating an existing key's value
my_dict['age'] = 31
# Output: {'name': 'John', 'age': 31, 'city': 'New York'}

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Removing an item using del
del my_dict['age']
# Output: {'name': 'John', 'city': 'New York'}

# Removing an item using pop()
my_dict.pop('city')
# Output: {'name': 'John'}


my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

keys = my_dict.keys()
print(keys)    # Output: dict_keys(['name', 'age', 'city'])

values = my_dict.values()
print(values)  # Output: dict_values(['John', 30, 'New York'])

items = my_dict.items()
print(items)   # Output: dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])

print(len(my_dict))  # Output: 3


my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Iterating over keys
for key in my_dict:
    print(key)

# Output: name
#         age
#         city

# Iterating over values
for value in my_dict.values():
    print(value)

# Output: John
#         30
#         New York

# Iterating over key-value pairs
for key, value in my_dict.items():
    print(f'{key}: {value}')

# Output: name: John
#         age: 30
#         city: New York



# Example: Create a dictionary of squares for numbers from 1 to 5
squares = {x: x*x for x in range(1, 6)}
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


my_dict = {'name': 'John', 'age': 30}

print('name' in my_dict)   # Output: True
print('gender' in my_dict) # Output: False

