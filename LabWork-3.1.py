print("=========Q1=========")
num = int(input("Enter a Number :"))

if num %2==0 :
    print(f"Your Number is {num} Even")
else :
    print(f"Yout Number is {num} Odd")

print("=========Q2=========")
age = int(input("Enter Your Age :"))

if age<=12 :
     print(f"You are child, because Your age is {age}")
elif age >=13 and age <=19 :
    print(f"You are in Teenager, because Your age is {age}")
elif age >=20 and age<=59 :
    print(f"You are in Adult, because Your age is {age}")
elif age >=60 :
    print(f"You are in Senior, because Your age is {age}")
else :
    print("Inavlid Number ")

print("=========Q3=========")

a = int(input("Enter First Number :"))
b = int(input("Enter Second Number :"))
c = int(input("Enter Third Number :"))

if a >= b and a >=c :
    print(f"First Number is Largerest Number {a}")
elif b >=c and b>=a :
    print(f"Second Number is Largerest Number {b}")
elif c >=a and c>=b :
    print(f"Third Number is Largerest Number {c}")

print("=========Q4=========")

n = int(input("Enter a Number :"))

'''
if n == 0 :
    print(f"This Number is {n} is Neutral Number ")
else :
    print(f"This Number is {n} is Not Neutral Number ")
'''

match n:
    case n if n == 0 :
        print(f"This Number is {n} is Neutral Number ")

    case _:
        print(f"This Number is {n} is Not Neutral Number")
