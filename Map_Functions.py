"""Python’s map() is a built-in function that allows you to process and transform all
the items in an iterable without using an explicit for loop, a technique commonly known
as mapping.
"""
#Below is the basic syntax of map functions in Python.
#map(function, iterable[, iterable1, iterable2,..., iterableN])

# Map Function
# Return double of n
def addition(n):
    return n + n

# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))


# Double all numbers using map and lambda rather than normal function
numbers_2 = (1, 2, 3, 4)
result_2 = map(lambda x: x + x, numbers_2)
print(list(result_2))

# Convert to Fahrenheit
def to_fahrenheit(c):
    return 9 / 5 * c + 32

celsius_temps = [100, 40, 80]
print(list(map(to_fahrenheit, celsius_temps)))


# Below are some examples of mapping two lists

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

#adding numbers in two lists
result_3 = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result_3))


first_it = [1, 2, 3]
second_it = [4, 5, 6, 7]

#the numbers in list 2 are raised to power to numbers in list 1
print(list(map(pow, first_it, second_it)))


""" 

All Outputs
[2, 4, 6, 8]
[2, 4, 6, 8]
[212.0, 104.0, 176.0]
[5, 7, 9]
[1, 32, 729]

"""