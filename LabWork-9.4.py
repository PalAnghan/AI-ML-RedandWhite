# Q 1:
print("=" * 40)
print("Q 1:")
print("=" * 40)
'''
class Calculate():

    def __init__(self,num1,num2,str1,str2):
        self.num1 = num1
        self.num2 = num2
        self.str1 = str1
        self.str2 = str2

    def getter_int(self):
        return self.num1 + self.num2

    def getter_str(self):
        return self.str1 + self.str2

number1 = Calculate(10,20,"Pal","Anghan")
print(number1.getter_int())
print(number1.getter_str())

# Q 2:
print("=" * 40)
print("Q 2:")
print("=" * 40)
'''
'''
import math

class Shape():
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

shapes = [Rectangle(10,7),Circle(5)]

for shape in shapes:
    print(f"Area: {shape.area():.2f}")
'''

print("=" * 40)
print("Q 3:")
print("=" * 40)
'''
class string:
    def __init__(self, name):

        self.name = name

    def display(self):
        print(f"name : {self.name} length of : {len(self.name)} ")

class lists(string):

    def __init__(self,lists):

        self.lists = lists

    def display(self):
        print(f"list : {self.lists} length of : {len(self.lists)}")

class dicts(string):

    def __init__(self, Dict):

        self.Dict = Dict

    def display(self):
        print(f"dict : {self.Dict} length of : {len(self.Dict)}")

displays = [string("Pal Anghan") , lists([1, 2, 3, 4 ,5, 6]) , dicts({"name" : "Pal Anghan" , "Age" : 30})]

for dis in displays:
    dis.display()

'''

print("=" * 40)
print("Q 4:")
print("=" * 40)

'''
class Transport:
    def travel(self):
        pass

class Train(Transport):
    def travel(self):
        return "Traveling on tracks thought countryside."

class Plane(Transport):
    def travel(self):
        return "Flying High in Clouds"
    
vehicles = [Train(), Plane()]

for vehicle in vehicles:
    print(vehicle.travel())
'''
print("=" * 40)
print("Q 5:")
print("=" * 40)
'''
class Calculater:

    def multiply(self, a , b = 2 , c = 1):
        return a * b *c

c1 = Calculater()
print("multiply of 3 aruguments (2 defaulter)",c1.multiply(5))
print("multiply of 3 aruguments((1 defaulter)",c1.multiply(10,5))
print("multiply of 3 aruguments((0 defaulter)",c1.multiply(2,4,6))

'''
print("=" * 40)
print("Q 6:")
print("=" * 40)

'''
class Animal:

    def speak(self):
        return "Animal Speak."

class Dog(Animal):

    def speak(self):
        return "Dog Speak Bhow... Bhow..."

class cat(Animal):

    def speak(self):
        return "Cat Speak Meow... Meow..."

animals = [Dog(), cat()]
for animal in animals:
    print(animal.speak())

'''
print("=" * 40)
print("Q 7:")
print("=" * 40)


print("=" * 40)
print("Q 8:")
print("=" * 40)
'''
class Vehicle:

    def start(self):
        print("Start Vehicle....")

class bike(Vehicle):

    def start(self):
        print("Start Bike......")

class Car(Vehicle):

    def start(self):
        print("Start Car......")

vehicles = [bike(), Car()]

for veh in vehicles:
    veh.start()
'''

print("=" * 40)
print("Q 9:")
print("=" * 40)
'''
class Printer:
    def print_data(self, arg1=None, arg2= None):
        if arg1 is not None and arg2 is not None:
            print(f"Both: {arg1} and {arg2}")
        elif arg1 is not None:
            if isinstance(arg1, str):
                print(f"String: {arg1}")
            elif isinstance(arg1, int):
                print(f"Integer: {arg1}")
        else:
            print("No arguments provided")

p = Printer()
p.print_data("Hello")
p.print_data(45)
p.print_data("Age", 21)
'''

print("=" * 40)
print("Q 10:")
print("=" * 40)
'''
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

result = issubclass(Student, Person)
print(f"Is Student a subclass of Person := {result}")
'''

print("=" * 40)
print("Q 11:")
print("=" * 40)
'''
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
        print(f"Employee Initialized: {self.name}, Salary Initialized: {self.salary}")

class Manager(Employee):

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
        print(f"Manager initialized for department: {self.department}")

mgr = Manager("Alice", 90000 , "IT")
'''

print("=" * 40)
print("Q 12:")
print("=" * 40)
'''
class Grandparent:

    def display(self):
        print("Grandparent display.")

class Parent(Grandparent):

    def display(self):
        print("Parent display.")

class Child(Parent):

    def display(self):
        print("Child display.")

print(f"Is subclass Relationship : {issubclass(Child, Parent)}")
print(f"Is subclass Relationship : {issubclass(Child, Grandparent)}")
print(f"Is subclass Relationship : {issubclass(Parent, Grandparent)}")
'''

print("="*40)
print("Q-13")
print("="*40)

"""
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        print(f"User profile created for: {self.username}")

class Admin(User):
    def __init__(self, username, email, access_level):
        # Call the parent User constructor
        super().__init__(username, email)
        self.access_level = access_level
        print(f"Admin level set to: {self.access_level}")

# Testing the code
admin_user = Admin("john_doe", "john@example.com", "Full Access")
"""



















































































































    




























