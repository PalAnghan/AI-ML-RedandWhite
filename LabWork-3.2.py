# Q 1:

print("|------Q1------|")

a = 55
b = 10
c = 40
print(f"First Number is : {a} , Second Number is : {b} , Third Number is : {c}")

if  a :
    pass
    if a >= b and a >= c :
        print("First Number is Maximum Number")
    elif b >= c and b >= a :
        print("Second Number is Maximum NUmber")
    elif c >= a and c >= b :
        print("Third Number is Maximum Number")
else :
    print("INVALID NUMBER")

# Q 2 :

print("|------Q2------|")

a = 55
b = 10
c = 40
print(f"First Number is : {a} , Second Number is : {b} , Third Number is : {c}")
if  a :
    pass
    if a <= b and a <= c :
        print("First Number is Minimum Number")
    elif b <= c and b <= a :
        print("Second Number is Minimum NUmber")
    elif c <= a and c <= b :
        print("Third Number is Minimum Number")
else :
    print("INVALID NUMBER")

# Q 3 :

print("|------Q3------|")

num1 = 10
num2 = 16
num3 = 12
num4 = 5
print(f"First Number is : {num1} , Second Number is : {num2} , Third Number is : {num3} , Forth Number is : {num4}")

if  num1:
    pass
    if num1 >= num2 and num1 >= num3 and num1 >= num4 :
        print("First Number is Maximum Number")
    
    elif num2 >= num3 and num2 >= num4 and num2 >= num1 :
        print("Second Number is Maximum Number")
        
    elif num3 >= num4 and num3 >= num1 and num3 >= num2 :
        print("Third Number is Maximum Number")

    elif num4 >= num1 and num4 >= num2 and num4 >= num3 :
        print("Fouth Number is Maximum Number")
else :
    print("INVALID NUMBER")

# Q 4 :

print("|------Q4------|")

user1 = int(input("Enter a First Number :"))
user2 = int(input("Enter a Second Number :"))

print("Choose What Operation You can Perform. Enter Sign (+, -, *, /): ")
oper = input()

match oper :
    case "+" :
        print("Addition Between a Two Numbers :",user1 + user2)
    case "-" :
        print("Subtraction Between a Two Numbers :",user1 - user2)
    case "*" :
        print("Multiplication Between a Two Numbers :",user1 * user2)
    case "/" :
        print("Divison Between a Two Numbers :",float(user1 / user2))
    case _:
        print("INVALID NUMBER")

# Q 5 :
print("|------Q5------|")

#press1 = int(input("Press 1 to order a Sandwich : "))
#press2 = int(input("Press 2 to order a Pizaa : "))
#press3 = int(input("Press 3 to order a Burger : "))

pizza = {
    "item": "Pizza", 
    "1": "Thin Crust Pizza", 
    "2": "Cheese Burst Pizza", 
    "3": "Fresh Dough Pizza"
}

print("Press 1 for SandWich, Press 2 for Pizza, Press 3 for Buger")
menu = input("Choose What Order You Want (press 1, 2, 3): ")

#a = "Thin Crust Pizza"
#b = "Cheese Burst Pizza"
#c = "Fresh Dough Pizaa"

match menu :
    case "1" :
        print("SandWich  Order Was Place!")
        
    #case "2" | "a" | "b" | "c" :
    #case {"item": "Pizza" , "Thin Crust Pizza":th} | {"item": "Pizza" , "Cheese Burst Pizza":ch} | {"item": "Pizza" , "Fresh Dough Pizza":fr} :     
    #case {"item": "Pizza" , "Thin Crust Pizza":th , "Cheese Burst Pizza":ch , "Fresh Dough Pizza":fr} :
    case "2" :
        print("\n--- Choose Pizza Variety ---")
        print("Press 1 for Thin Crust")
        print("Press 2 for Cheese Burst")
        print("Press 3 for Fresh Dough")

        var = input("choose 1,2,3 :")

        if var == "1" :
            print("Thin Crust Pizza was Order Place")
        elif var == "2" :
            print("Cheese Burst Pizza was Order Place")
        elif var == "3" :
            print("Fresh Dough Pizza was Order Place")
        
    case "3" :
        print("Buger order Was Place!")
        
    case _:
        print("Invalid nuber")

# Q 6 :

print("|------Q6------|")

print("Press 1 for English , Press 2 for Hindi , Press 3 for Gujarati")
sub = int(input("\nChoose What Subjest You Want :"))

match sub:
    case 1:
        print("You Select English!")
    case 2:
        print("You Select Hindi!")
    case 3:
        print("You Select Gujarati!")
 

























