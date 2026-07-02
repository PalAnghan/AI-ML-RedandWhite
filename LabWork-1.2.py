# Q 1 :
print("Using 'sep' ")
print("Apple" , "Banana" , "Mango" )
print("Apple" , "Banana" , "Mango" , sep="-")
print("Apple" , "Banana" , "Mango" , sep="\n")

print("\nUsing 'end'")
print("Apple" , "Banana" , "Mango" )
print("Apple" , "Banana" , "Mango" , end="-")
print("Apple" , "Banana" , "Mango" , end="...")

# Q 2 :
name = input("\n\nEnter Your Name :")
age = int(input("Enter Your Age :"))
hobby = input("Enter Your Hobby: ")

print(f"Hello,{name}! At {age},enjoying {hobby} sounds fun!")

# Q 3 :
a = float(input("\nEnter First Number: "))
b = float(input("Enter Second Number: "))


print("\nAddition: ", a+b)
print("Subtraction: ",a-b)
print("Multiplication: ",a*b)
print("Divison: ",a/b)
print("Floor Divison: ",a//b)
print("Module: ",a%b)

# Q 4 :
num = 10
pi = 3.14
name = "Pal"
boo = True

print(f"\ninteger : {type(num)}, ", num)
print(f"floating : {type(pi)}, ", pi)
print(f"string : {type(name)}, ", name)
print(f"boolean : {type(boo)}, ", boo)

# Q 5 :
n = input("\nEnter Your Name :")
height = float(input("Enter Your Height :"))
weight = float(input("Enter Your Weight :"))

print(f"\nHello, {n} , Your Height is {height}, Your Weight is {weight}")

# Q 6 :
a = input("\nEnter True or False for A: ").strip().lower() == "true"
b = input("Enter True or False for B: ").strip().lower() == "true"

print()

print(f"A and B : {a and b}")
print(f"A or B  : {a or b}")
print(f"not A   : {not a}")

# Q 7 :
number = 10
print(f"\nInitial value: {number}")

number += 5
print(f"After += 5:   {number}")

number -= 3
print(f"After -= 3:   {number}")

number *= 2
print(f"After *= 2:   {number}")

number /= 4
print(f"After /= 4:   {number}")




