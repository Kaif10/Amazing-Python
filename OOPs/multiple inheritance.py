# Multiple Inheritance
# A class can inherit from multiple parents.
#In below example class MultiDerived inherits from Class Base1 and Base2
class Base1:
  pass

class Base2:
  pass

class MultiDerived(Base1, Base2):
  pass



# Python Program to depict multiple inheritance
# when method is overridden in both classes

class Class1:
  def m(self):
    print("In Class1")

class Class2(Class1):
  def m(self):
    print("In Class2")

class Class3(Class1):
  def m(self):
    print("In Class3")

class Class4(Class2, Class3):
  pass

obj = Class4()
obj.m()
print()

#In Class2


# Python Program to depict multiple inheritance
# when method is overridden in one of the classes

class Class1:
  def m(self):
    print("In Class1")

class Class2(Class1):
  pass

class Class3(Class1):
  def m(self):
    print("In Class3")

class Class4(Class2, Class3):
  pass

obj = Class4()
obj.m()
print()

#In Class3

# Python Program to depict multiple inheritance
# when every class defines the same method
class Class1:
  def m(self):
    print("In Class1")

class Class2(Class1):
  def m(self):
    print("In Class2")

class Class3(Class1):
  def m(self):
    print("In Class3")

class Class4(Class2, Class3):
  def m(self):
    print("In Class4")

obj = Class4()
obj.m()
Class2.m(obj)
Class3.m(obj)
Class1.m(obj)
print()

#In Class4
#In Class2
#In Class3
#In Class1

# Python Program to depict multiple inheritance
# when we try to call the method m for Class1, Class2, Class3 from the method m of Class4

class Class1:
  def m(self):
    print("In Class1")

class Class2(Class1):
  def m(self):
    print("In Class2")

class Class3(Class1):
  def m(self):
    print("In Class3")

class Class4(Class2, Class3):
  def m(self):
    print("In Class4")
    Class2.m(self)
    Class3.m(self)
    Class1.m(self)

obj = Class4()
obj.m()
print()

#In Class4
#In Class2
#In Class3
#In Class1

# Python program to demonstrate
# super()
class Class1:
  def m(self):
    print("In Class1")

class Class2(Class1):
  def m(self):
    print("In Class2")
    super().m()

class Class3(Class1):
  def m(self):
    print("In Class3")
    super().m()

class Class4(Class2, Class3):
  def m(self):
    print("In Class4")
    super().m()


obj = Class4()
obj.m()
print()

#In Class4
#In Class2
#In Class3
#In Class1





# Simple example of using super and the MRO( method resolution order) in OOPS
class Car:
  def __init__(self, door, wheel):
    self.door = door
    self.wheel = wheel

  def start(self):
    print('Start the Car')

  def go(self):
    print('Going')


class Flyable:
    def __init__(self, wing):
      self.wing = wing

    def start(self):
      print('Start the Flyable object')

    def fly(self):
      print('Flying')


class FlyingCar(Flyable, Car):
  def __init__(self, door, wheel, wing):
    super().__init__(wing=wing)
    self.door = door
    self.wheel = wheel

  def start(self):
    super().start()

if __name__ == '__main__':
    car = FlyingCar('door', 'wheel', 'wing')
    car.start()









#Start the Flyable object