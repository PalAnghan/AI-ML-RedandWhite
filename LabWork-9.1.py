#Q 1:
print("=" * 40)
print("Q 1:")
print("=" * 40)
'''
class Person:

    def __init__(self, name, age, gender):

        self.name = name
        self.age = age
        self.gender = gender

    #method

    def User_Deatils(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")

        print(f"Hi my self {self.name} , I am {self.age} years old , My gender was {self.gender}")
        
      
p1 = Person("Pal Anghan" , 20 , "Male")
p1.User_Deatils()
'''

# Q 2:
print("=" * 40)
print("Q 2:")
print("=" * 40)
'''
class Count_Number:
    
    def __init__(self):
        self.count = 0
        
    def increment(self):
        self.count += 1

    def Display(self):
        print(f"Current count: {self.count}")

count1 = Count_Number()
count1.increment()
count1.increment()
count1.Display()
'''

# Q 3:
print("=" * 40)
print("Q 3:")
print("=" * 40)
'''
class Experiment_self_keyword:

    def With_Self(self):
        print("Hello World!")
        
    def Witout_Self():
        print("Hello World!")

self1 = Experiment_self_keyword()
self1.With_Self()
#self1.Witout_Self()
'''
"""
error : TypeError: Experiment_self_keyword.Witout_Self() takes 0 positional arguments but 1 was given
so without self we can try so its error in case we can differnt method we use 
"""

# Q 4:
print("=" * 30)
print("Q 4:")
print("=" * 30)
'''
class Book:
    def __init__(self):
        
        self.__title = ""
        self.__author = ""

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

my_book = Book()

my_book.set_title("To Kill a Mockingbird")
my_book.set_author("Harper Lee")

print("Book Title:", my_book.get_title())
print("Book Author:", my_book.get_author())
'''
# Q 5:

print("=" * 30)
print("Q 5:")
print("=" * 30)

'''
class Account:

    def __init__(self , name , balance):

        self.name = name
        self.__balance = balance

    def deposit(self, amount):

        if amount > 0:

            self.__balance += amount
            print(f"{amount} deposit sucessfully!....")

        else:
            print(f"{amount} shold be greter than 0")

    def withdraw(self,amount):

        if self.__balance > amount:
            self.__balance -= amount
            print(f"{amount} was withdraw!....")

        else:
            print("Not sufficient acmount!...")


    def display(self):

        print(f"Name is{self.name}, your balance is{self.__balance} ")

    
user1 = Account("Pal Anghan" , 10000)

while True:

     print("""
    1. deposit
    2. withdraw
    3. display
    4. exit
    """)

     choice = int(input("Enter a number : "))

     match choice:

         case 1:
             amount = int(input("Enter your deposit amount: "))
             user1.deposit(amount)
         case 2:
             amount = int(input("Enter your withdrw amount: "))
             user1.withdraw(amount)
         case 3:
             user1.display()
         case 4:
             print("visiting again!.....")
             break
         case _:
             print("Enter number between 1 to 4")

'''

# Q 6:

print("=" * 30)
print("Q 6:")
print("=" * 30)
'''
class student_age:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Setter
    def set_age(self):
        self.age = int(input("Enter New Age : "))

    # getter
    def get_age(self):
        if self.age > 0:
            print(f"Name : {self.name} | Age : {self.age}")
        else:
            print("Invaild age plese enter a valid age!...")

name = input("Enter Your Name : ")
age = int(input("Enter Your Age : "))

Student = student_age(name , age)

Student.get_age()
Student.set_age()
Student.get_age()
'''

# Q 7:

print("=" * 30)
print("Q 7:")
print("=" * 30)

class Student:

    def __init__(self, name , marks1,marks2,marks3):
        self.name = name
        self.__marks = [marks1, marks2, marks3]
     
        
    def average(self):
        total = 0
        for value in self.__marks:
            total += value
        print("hi",self.name,"your avg score is",total/3)

    def display(self):

        avg = sum(self.__marks) /len(self.__marks)
        
        if avg >= 90:
            grade = 'A'
        elif avg >= 80:
            grade = 'B'
        elif avg >= 70:
            grade = 'C'
        elif avg >= 60:
            grade = 'D'
        else:
            grade = 'F'

        print(f"Your Grade: {grade}")
        
name = input("Enter Your Name : ")
marks1 = int(input("Enter your first subject marks:"))
marks2 = int(input("Enter your second subject marks:"))
marks3 = int(input("Enter your third subject marks:"))

stu1 = Student(name,marks1,marks2,marks3)
stu1.average()
stu1.display()






















    











    






















    









