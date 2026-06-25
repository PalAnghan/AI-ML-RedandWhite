#1. Check greater number between two inputs

val1 = int(input("Enter First Number : "))
val2 = int(input("Enter Second Number : "))

print("First Number is Greater : ",val1>val2)
print("Second Number is Greater : ",val2>val1)

print("-------------------------")

#2. Check if number is equal or not

num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))

#print("First Number andd Second Number are  :",num1 == num2)

if num1 == num2 :
    print("Both Numbers are Equal ")
else :
    print("Both Numbers not Equal ")

print("-------------------------")

#3. Voting eligibility (age ≥ 18)

age = int(input("Write Your Age :"))

if age >= 18 :
    print("You are Eligiable for VOTE ")
else :
    print("You are Not Eligiable for VOTE ")
    
print("-------------------------")

#4. Find largest of 3 numbers

a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))
c = int(input("Enter Third Number : "))

if a >= b and a >= c:
    print(" firsr number is Large  number ")
elif b >= c and b >= a:
    print("Second number is Large number ")
elif c >=a :
    print("Third numbr is Large number ")
else:
    print("INVALID NUMBER ")
print("-------------------------")

#5. Check pass/fail based on marks

mark = int(input("Write Your Marks : "))

'''
if mark >= 85 and mark <=100:
    grade = "A"
elif mark >= 75 and mark < 85:
    grade = "B"
elif mark >= 65 and mark < 75:
    grade = "C"
elif mark >= 33 and mark < 65:
    grade = "D"
else:
    grade = "FAIL"

print("Your Grade is : ",grade)
'''
if mark >= 33:
    print("You Are PASS ")
else :
    print("You Are FAIL ")


