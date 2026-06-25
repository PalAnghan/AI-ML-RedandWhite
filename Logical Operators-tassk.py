#1. Check if number is between 1–100

num1 = int(input("Write number :"))

if num1 <= 100 :
    print("Numer is under 100 ")
elif num1 >= 100 :
    print("Number is Greater 100 ")
else :
    print("INVALID NUMBER")

print("--------------------")

#2. Login system (username + password)

use = str(input("Write Your UserName : "))
pas = str(input("Write Your Password :"))

if use == pas :
    print(" login succsefully ")
else :
    print(" Recheck ")

print("--------------------")

#3. Check leap year (multiple conditions)

year = int(input("Enter A Year :"))

if year%4==0:
    print("This Year is Leap Year")
else :
    print("This Year is not Leep Year")
    
print("--------------------")

#4. Check if number is divisible by 3 AND 5
num = int(input("Write a number to check divide by 3&5 :"))

if num%3==0 and num%5==0 :
    print("This Number is Divisible by 3 and 5 ")
else :
    print("This Number is Not Divisible by 3 and 5 ")

print("--------------------")

#5. Validate input (age > 18 AND city == "Surat")

age = int(input("Write Your Age :"))
city = input("Write Your City :")

if age >= 18 :
    if city == "surat" :
        print("You Are Adult and You Live in surat ")
    else :
        print("You Are Adult but not live in surat ")
elif age <= 18 :
    if city == "surat" :
        print("You Are Not  Adult and You Live in surat ")
    else :
        print("You Are not Adult but live in surat ")
else :
    print("INVALID NUMBER")
    
