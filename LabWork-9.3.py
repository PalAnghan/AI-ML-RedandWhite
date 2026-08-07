#Q 1:
print("=" * 30)
print("Q 1:")
print("=" * 30)
'''
class Parent:

    def display(self):
        print("I am Parent!....")

class Child(Parent):

    def show(self):
        print("I am child!....")

c1 = Child()
c1.display()
'''

#Q 2:
print("=" * 30)
print("Q 2:")
print("=" * 30)
'''
class Teacher:

    def teaching(self):
        print("Teaching Subjects!...")

class Administer:

    def manage(self):
        print("Managing!....")

class Headmaster(Teacher,Administer):

    def guide(self):
        print("Students and Teachers guideing!....")

H1 = Headmaster()
H1.teaching()
H1.manage()
'''

#Q 3:
print("=" * 30)
print("Q 3:")
print("=" * 30)
'''
class Grandparent:

    def blessing(self):
        print("Blessing!....")

class Parent(Grandparent):

    def responsblity(self):
        print("Responsblity!......")

class Child(Parent):

    def study(self):
        print("Studying!......")

Child1 = Child()
Child1.responsblity()

Parent1 = Parent()
Parent1.blessing()
'''

#Q 4:
print("=" * 30)
print("Q 4:")
print("=" * 30)
'''
class Animal:

    def eat(self):
        print("Animal is Eating!....")

class Dog(Animal):

    def sound(self):
        print("Bow...Bow...")

class Cat(Animal):

    def sound(self):
        print("Meow...Meow...")

Animal1 = Dog()
Animal1.eat()
Animal1.sound()
'''

#Q 5:

print("=" * 30)
print("Q 5:")
print("=" * 30)

"""
class car:
    def start(self):
        print("car is Starting.....")

class bike(car):
    def start(self):
        super().start()
        print("Bike is Starting.....")

class cycle(car):
    def start(self):
        super().start()
        print("cycle is Starting.......")

class serach(bike , cycle):

    def start(self):
        super().start()
        print("Starting all vehicals.")

s = serach()

s.start()
"""

print("="*30)
print("Q 6:")
print("="*30)
"""
class Student:
    def __init__(self , name):
        self.name = name
        print(f"{self.name} Welcome.")

    def display(self):
        print("Hello , Student.")

class child(Student):
    def display(self):
        super().display()
        print("Hello , Child.")

c1 = child("Shrey")

print(type(c1))
"""

print("="*30)
print("Q 7:")
print("="*30)
"""
class car:
    def __init__(self , name):
        self.name = name
        print(f"{self.name} Welcome")

    def display(self):
        print("Hello car.")

class bike(car):
    def display(self):
        super().display()
        print("Hello , bike.")

b1 = bike("pagani")

print(dir(b1))
"""

print("="*30)
print("Q 8:")
print(":-"*30)
"""
class car:
    def __init__(self, name):
        self.name = name


c1 =  car("Alice")

print(isinstance(c1 , car))
print(isinstance(c1 , str))
"""

print("="*30)
print("Q 9:")
print("="*30)


class Calculator:
    """This class performs basic arithmetic operations like addition."""

    def add(self, a, b):
        """Returns the sum of two numbers."""
        return a +b

print("--- Class Documentation ---")
help(Calculator)

print("\n--- Method Documentation --- ")
help(Calculator.add)

        









































