# Arbitryary Aruguments (*args)

# Write a Python function that accept any number of arguments and return their sum.

def addtion(*args):
    total = 0

    for i in args:
        total += i

    return total

print("Total :",addtion(1,20,15,24,2))

# Keyword Arguments (**kwargs)

# Write a Python function that accept student information using keyword arguments and prints all student details.

def student(**kwargs):
    print("Student Details")

    for key,value in kwargs.items():
        print(f"{key} : {value}")

student(name = "vivek" , age = 25 , city = "surat" , course = "Python")

# doc (Documentation String)

# Write a function to calculate the area of a rectangle and display its Documentation.

def rectangle(length , width):
    """
  Function Name : reactangle

    Purpose:
        Calculate rectangle area.

    Parameter:
        length : int
        width : int
        
    Return:
        Area of rectangle
    """
    return length * width

print("Area : ", rectangle(10,20))
print(rectangle.__doc__)

#Lambda with map()

numbers = [10,15,20,25,30,35]

even = list(map(lambda x:x ** 2 ,numbers))

print(even)


# Lambda with filter()

numbers = [10,15,20,25,30,35]

even = list(filter(lambda x:x % 2 !=0 ,numbers))

print(even)

# Lamda with sorted()

students = [("Vivek" , 85), ("Shrey",2),("Pal",20), ("Raj" , 50)]
print(students)

result = sorted(students , key = lambda x:x[1])
print(result)

# Lambda with reduce()

from functools import reduce

numbers = [1,2,3,4,5]

product = reduce(lambda x, y:x * y , numbers)

print(product)

# Global Keyword in Python

total = 0

def increment():
    global total
    total += 2

increment()
increment()
print(total)

# Global vs Local Variables
name = "python"
def demo():
    global name
    name = "javascript"

    print(name)
demo()
print(name)

# Multiple return Values

def calculation(a,b,c):

    total = a + b + c
    average = total / 3
    maximum = max(a,b,c)
    minimum = min(a,b,c)

    return total, average, maximum, minimum

total, average, maximum, minimum = calculation(10,20,30)
print(total)

#Return multiple values(student result)

def result(m1,m2,m3):
    total = m1 + m2 + m3
    percentage = total/3

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    else:
        grade = "Fail"

    return total,percentage,grade

total,percentage,grade = result(90,90,95)

print(total)
print(percentage)
print(grade)


