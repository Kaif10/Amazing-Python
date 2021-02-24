"""Comprehensions in Python provide us with a short and concise way to construct new sequences
(such as lists, set, dictionary etc). List Comprehensions are a great way of writing clean and precise code.
"""


#1. create a list
input_list = [12, 535, 43534, 43, 236, 999]

# use list comprehension in square brackets
list_comp = [var for var in input_list if var % 2 == 0]
print("Output List using list comprehensions: ", list_comp)


# 2. Using range instead of creating a list

list_comp = [var ** 2 for var in range(1, 10)]

print("Output List using list comprehension:",
      list_comp_2)


"""
3. we want to create an output dictionary which contains only the odd numbers
that are present in the input list as keys and their cubes as values
"""
input_list = [1, 2, 3, 4, 5, 6, 7]

dict_comp = {var: var ** 3 for var in input_list if var % 2 != 0}

print("Output Dictionary using dictionary comprehensions:", dict_comp)



#4. Using zip to map elements in two lists
state = ['England', 'Iceland', 'Germany']

capital = ['Birmingham', 'Reykjavík', 'Berlin']

dict_comp_2 = {key: value for (key, value) in zip(state, capital)}

print("Output Dictionary using dictionary comprehensions:", dict_comp_2)



#5. Set:  Curly brackets will make a set i.e. only unique values as output

input_list = [1, 2, 34, 34, 50, 50, 6, 6, 7, 7]

set_comp = {var for var in input_list if var % 2 == 0}

print("Output Set using set comprehensions:",
      set_comp)


"""6.  GENERATOR COMPREHENSION
One difference between list comprehension and generator is that generator comprehensions use circular brackets whereas list comprehensions 
use square brackets. The major difference between them is that generators don’t allocate memory for the whole list. 
Instead, they generate each value one by one which is why they are memory efficient"""
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]

output_gen = (var for var in input_list if var % 2 == 0)

#this will return a generator object pointing to the memory location.
print(output_gen)

print("Output values using generator comprehensions:", end=' ')

# After looping through, we will generate each value one by one from generator object.
for var in output_gen:
      print(var, end=' ')
print('')



#7.  Nested list comprehension
# the below code will create a 7*7 square matrix.
# We used two list comprehensions one embedded in the other to make a nested list comprehension.

matrix = [[i for i in range(7)] for i in range(7)]
print(matrix)

# All the Outputs.

#Output List using list comprehension: [1, 4, 9, 16, 25, 36, 49, 64, 81]

#Output Dictionary using dictionary comprehensions: {1: 1, 3: 27, 5: 125, 7: 343}

#Output Dictionary using dictionary comprehensions: {'England': 'Birmingham', 'Iceland': 'Reykjavík', 'Germany': 'Berlin'}

#Output Set using set comprehensions: {2, 34, 50, 6}

#<generator object <genexpr> at 0x000001FDDAAC42C8>

#Output values using generator comprehensions: 2 4 4 6

#[[0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5, 6]]
