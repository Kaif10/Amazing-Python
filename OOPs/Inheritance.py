class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)


#Student class inherited properties (fname, lname) from Person class with help of super() funtion
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)





Student_1 = Student("Mike", "Olsen", 2019)

Student_1.welcome()
#Welcome Mike Olsen to the class of 2019



print(Student_1.firstname)
#Mike

