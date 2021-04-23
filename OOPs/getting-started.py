#Simple class syntax
class Dog:
    pass



# Lets add some properties to the class. The properties must be defined in  __init__ method.

class Dog_2:
    def __init__(self, name, age):

   #Attributes created in.__init__() are called instance attributes
        self.name = name
        self.age = age



# Instance methods(funcs defined inside a class)
class Dog_3:


# Class attributes (same for all class instances)
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # All instance methods use a by-default self argument as they belong to a particular class.
    def description(self):
        return f"{self.name} is {self.age} years old "

    # Another instance method with an argument along with self
    def speak(self, sound):
        return f"{self.name} is {sound} and his age is {self.age}"

arnold = Dog_3('Arnold', 12)
tommy = Dog_3('Tommy', 13)

print(arnold.description())

print(tommy.speak('barking'))

print(tommy.species)

# Output

#Arnold is 12 years old
#Tommy is bark and his age is 13
#Canis familiaris