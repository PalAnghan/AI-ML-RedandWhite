#if statement
age = int(input("Write Your Age :"))

if age >= 18:
     print("You Are Adult")
else:
    print("You Are not Adult")

print("------------------------")

#if-else statement

num = int(input("Enter Your Favourite Number :"))

if num>=0:
    print("Positive Number")
else:
    print("Negative Number")
    
print("------------------------")

#if-elif-else statement

marks = int(input("Enter Your Marks:"))
grade =  ""

if marks >=90:
    grade = "Grade A"
elif marks >=75:
    grade = "Grade B"
elif marks >=60:
    grade = "Grade C"
else:
    grade = "Fail"
print("You Have Recive:",grade)

print("------------------------")

#match-case statement


ope = input("What day is it today? Write :")

match ope:
    case "monday":
        print(f"Today is {ope}, Have nice day")
        
    case "tuesday":
        print(f"Today is {ope}, Have nice day")
        
    case "wednesday":
        print(f"Today is {ope}, Have nice day")
        
    case "thursday":
        print(f"Today is {ope}, Have nice day")
        
    case "friday":
        print(f"Today is {ope}, Have nice day")

    case "saturday":
        print(f"Today is {ope}, Have nice day")

    case "sunday":
        print(f"Today is {ope}, Have nice day")
        
    case _:
        print("Check Your Spelling")

print("------------------------")

char = input("Write Your Name First character :")

match char:
    case "a"|"e"|"i"|"o"|"u" :
        print("The first character of your name is a vowel ")
    case _:
        print("The first character of your name is NOT vowel ")
