# Syntax: lambda arguments: expression

#1.
# Python code to illustrate cube of a number
# showing difference between def() and lambda().
def cube(y):
    return y * y * y

lambda_cube = lambda y: y * y * y


# using the normally
# defined function
print(cube(5))

# using the lamda function
print(lambda_cube(5))



def funcc(x):
    if x % 2 != 0:
        return x

print(filter(funcc, li))

2. # filter() with lambda()
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(filter(lambda x: (x % 2 != 0), li))
print(final_list)

# map() with lambda()
# to get double of a list.
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(map(lambda x: x * 2, li))
print(final_list)




# importing functools for reduce()
import functools

# initializing list
lis = [1, 3, 5, 6, 2, ]

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))