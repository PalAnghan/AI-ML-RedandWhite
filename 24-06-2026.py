'''
#write your name 
print("Hello , my self Pal Anghan " )

#two number find sum
a = 5
b = 15
print("SUM is : ", a+b)

#ask user input 
name = input("Write Your Name : ")
print("Hi , ",name)


#simple mathematis
num1 = int(input("Write First Number :"))
num2 = int(input("Write Second Number :"))

print("Addition :", num1+num2)
print("Subtraction :", num1-num2)
print("Multiplication :", num1*num2)
print("Division :",num1/num2)


#print() formation using sep and end
print("Apple", "Banana" , "Cherry" ,sep="|", end="<---- of list\n")

#formating messgage from user input
name = input("Write Your Name :")
age = int(input("Write Your Age :"))
hobby = input("Write Your Hobiees :")

print(f"Hello ,{name}! you are {age} years old , Enjoying {hobby}")


#diiferent data types in python
a=10
b=3.14
c="python"
d=True

print(a,"Type:",type(a))
print(b,"Type:",type(b))
print(c,"Type:",type(c))
print(d,"Type:",type(d))
'''

sub1 = input("Write Your First Subject:")
mark1 = int(input("Write Your Marks:"))

sub2 = input("Write Your Second Subject:")
mark2 = int(input("Write Your Marks:"))

sub3 = input("Write Your Third Subject:")
mark3 = int(input("Write Your Marks:"))

total = mark1+mark2+mark3
avg = total/3


if avg >= 85 and avg<=100:
    grade = "A"
elif avg >= 75 and avg < 85:
    grade = "B"
elif avg >= 65 and avg < 75:
    grade = "C"
elif avg >= 33 and avg < 65:
    grade = "D"
else:
    grade = "FAIL"

print("--------RESULT--------")

print(f"\nTotal Marks: {total}")
print(f"Average Marks: {avg:.2f}")

print(f"Your First Subject {sub1} : Your Marks is : {mark1}")
print(f"Your Second Subject {sub2} : Your Marks is : {mark2}")
print(f"Your Third Subject {sub3} : Your Marks is : {mark3}")
print(f"Your Grade is: {grade}")





