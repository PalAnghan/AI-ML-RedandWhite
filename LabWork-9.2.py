# Q 1:

print("=" * 30)
print("Q 1:")
print("=" * 30)
'''
class Employee:

    def __init__(self,name,age):

        self.name = name
        self.age = age

        print(f"\nMy self {self.name} , i am {self.age} Years old. ")

    def display(self):
        print("\n=====Employee Details=====")
        print("\nEmployee: ",self.name)
        print("\nAge: ",self.age)
        print("=" * 26)

    def __del__(self):
        print(f"\n{self.name} you are loged out the system!....")

    def login(self):
        print(f"\n{self.name} are stay!.......")

name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))

name1 = input("\nEnter Your Name: ") 
age1 = int(input("Enter Your Age: "))

emp1 = Employee(name,age)
emp1.display()

emp2 = Employee(name1,age1)
emp2.display()

del emp1

emp2.login()
'''


# Q 2:

print("=" * 30)
print("Q 2:")
print("=" * 30)
'''
class Animal:

    def __init__(self):
        self.name = "Cat"
        self.food = "Milk"

    def display(self):
        print(f"The {self.name} was , {self.food} Drinking!.....")

A1 = Animal()
A1.display()
'''

#Q 3:
print("=" * 30)
print("Q 3:")
print("=" * 30)
'''
class Rectangle:

    def __init__(self,length = float,width = float ):
        self.length = length
        self.width = width
        self.total = 0
    def calculate_rect(self):
        self.total = self.length * self.width

    def display(self):
        print(f"Length is {self.length} and Width is {self.width} : {self.total}")
        
length = float(input("Enter Length of Rectangle: "))
width = float(input("Enter Width of Rectangle: "))
R1 = Rectangle(length,width)
R1.calculate_rect()
R1.display()    
'''

# Q 4:
print("=" * 30)
print("Q 4:")
print("=" * 30)
'''
class Employee:

    def __init__(self):
        self.name = "Pal Anghan"
        self.department = "IT"
        print(f"{self.name} was {self.department} department")

    def __del__(self):

        print(f"{self.name} GoodBye!......")


emp1 = Employee()
del emp1
'''
# Q 5:
print("=" * 30)
print("Q 5:")
print("=" * 30)

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Your name is {self.name} and you are {self.age} years old ")
        
name = input("Enter your name: ")
age = int(input("Enter your age: "))

s1 = Student(name,age)
s1.display()











































