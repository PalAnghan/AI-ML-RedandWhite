#1. Simple calculator (+, -, *, /)

print("Simple calculator (+, -, *, /)")
a=int(input("Write First Number : "))
b=int(input("Write Second Numbeer : "))

print("Adition :",a+b)
print("Subtraction :",a-b)
print("Multiplication :",a*b)
print("Divison :",a/b)

print("-----------------------")

#2. Find remainder using %

print("Remainder ")
rem = int(input("Write First Number :"))
rem1 = int(input("Write Second Number :"))
print("Remainder: ", rem%rem1)

print("-----------------------")

#3. Calculate area of rectangle/circle

print("Area of Rectangle/Circle")
l = int(input("Write First Number :"))
b = int(input("Write Second Number :"))
pi=3.14

area = pi * (b ** 2)

print("Area of Rectangle : ", l*b)
print("Area of Circle : ",area)

print("-----------------------")

#4. Calculate simple interest

print("Simple Interest")

p = 10
r = 20
t = 10

total = (p*r*t)/100 
print("Simple Interest :",total)

print("-----------------------")
