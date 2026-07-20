print("=" * 20)
print("Q 1 :")

number = [30,20,10,40,50]

print("Length of List is",len(number))
print("Maximum Number in List is",max(number))
print("Minimum Number in List is",min(number))
print(sorted(number))
print("Sum of List is",sum(number))
print("Type is",type(number))

print("=" * 20)
print("Q 2:")

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

print(factorial(int(input("Enter a number to find Factorial :"))))

print("=" * 20)
print("Q 3:")

def square():

    number = [10,20,30]

    result = [i * i for i in number]
    return result
print(square())

print("=" * 20)
print("Q 4:")

def frequency(input_string):
    frequencys = {}
    for i in input_string:
        if i in frequencys:
            frequencys[i] += 1
        else:
            frequencys[i] = 1
    return frequencys

string = "banana nenno"
result = frequency(string)
print(result)

print("=" * 20)
print("Q 5:")

def cude(num):
    cude_list = []

    return [ nm * 3 for nm in num]

list_num = [1, 2, 3, 45, 4, 5]

result = cude(list_num)

print("Original List = ", list_num)
print("Cude List = ", result)

print("=" * 20)
print("Q 6:")

def sum_mul(*args):
    if len(args) == 0:
        return 0

    sum_product = 0
    for i in args:
        sum_product += i

    product = 1
    for i in args:
        product *= i

    return sum_product,product

sum_product,product = sum_mul(2, 4, 3, 1)
print(f"1 Test sum:{sum_product} | and Product: {product}")

sum_result, result_product = sum_mul(2, 40, 44, 55, 46)
print(f"1 Test sum:{sum_result} | Product: {result_product}")

print("=" * 20)
print("Q 7:")

def Student_list(*args):

    if not args:
        print("No Student Provide Name. list is empty.")
        return

    for num in args:
        print(num)

Student_list("Akash", "Birjesh", "Rohan", "Pal")
Student_list()

print("=" * 20)
print("Q 8:")

def mixed_args(*args):

    strings = ()
    numbers = ()
    
    for i in args:
        if type(i) == str:
            strings += (i,)
        elif type(i) == int or type(i) == float:
            numbers += (i,)

    return strings , numbers

string , number = mixed_args("AI-ML",20,"IOS-Devloper",15,"Machine Learning",30)

print("Strings tuple: ",string)
print("Numbers tuple:", number)

print("=" * 20)
print("Q 9:")

def Student_store(**kwargs):
    print("Student Details")

    for key,value in kwargs.items():
        print(f"{key} : {value}")


Student_store(name="Raj", age = 19 , city = "surat")

print("=" * 20)
print("Q 10:")

def Product(**kwargs):
    total = kwargs["price"] * kwargs["quantity"]

    return f"Product: {kwargs['name']}\nTotal Cost: {total}"

result = Product(name ="Iphone 17Pro", price=75000, quantity = 2)

print(result)

print("=" * 20)
print("Q 11:")

def employee(**kwargs):
    if "name" not in kwargs:
        print("Name is missing")
    if "department" not in kwargs:
        print("department is missing")
    if "salary" not in kwargs:
        print("salary is missing")
    if "name" in kwargs and "department" in kwargs and "salary" in kwargs:
        print("Employee Details")
        print("Name :", kwargs["name"])
        print("Department  :", kwargs["department"])
        print("Salary :", kwargs["salary"])

employee(name="Lalit",department="BCA",salary=15000)

print("=" * 20)
print("Q 12:")

def rectangle(length, width):
    '''
    Calculate the area of a rectangle.

    Parameters:
    length : Length of the rectangle
    width  : Width of the rectangle

    Returns:
    Area of the rectangle
    '''
    return length * width

area = rectangle(10, 5)
print("Area =", area)

print("\nDocstring:")
print(rectangle.__doc__)

print("=" * 20)
print("Q 13:")

def fibonacci(n):
    '''
    Function Name : fibonacci Seriers 

    Purpose:
        Returns the Fibonacci sequence up to the given number.

    Parameter:
        n : Integer
            The maximum limit for the Fibonacci sequence.

    Return:
        A list containing Fibonacci numbers up to n.
    '''

    a = 0
    b = 1

    while a <= n:
        print(a, end=" ")
        c = a + b
        a = b
        b = c

n = int(input("Enter a number: "))
fibonacci(n)

print("\n\nDoc string")
print(fibonacci.__doc__)

     
    

