"""
Generator functions use yield keyword instead of return. They return a generator object. Generator objects are used either by calling the next method on the
generator object or using the generator object in a “for in” loop .
"""

# A generator function that yields 1 for first time,
# 2 second time and 3 third time

def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
    yield 3
    yield 3

# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)
print('')

# x is a generator object
x = simpleGeneratorFun()
# Iterating over the generator object using next
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print('')


# A Generator function for infinite sequence

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

# This will run an infinite sequence
#for i in infinite_sequence():
 #  print(i, end=" ")

a = infinite_sequence()

#We can go on to infinity as there is no limit specified in the for loop.

print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))


