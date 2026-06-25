#1. Increment and decrement a number

num1 = int(input("Write A Number :"))

inc_num = num1 + 1
print("Increment After:", inc_num)

dec_num = num1 - 1
print("Decrement After:", dec_num)

print("------------------------------")

#2. Use +=, -=, *= in calculations

a = int(input("Write a First Number :"))
b = int(input("Write a Second Number :"))

a+=b
print("use += first value",a)
print("use += second value",b)
a-=b
print("use -= first value",a)
print("use -= second value",b)
a*=b
print("use *= first value",a)
print("use *= second value",b)

print("------------------------------")

#3. Create running total (add numbers step by step)

number = [1, 2, 3, 4, 5]
curr_total = 0

for num in number:
    curr_total += num
    print(f"Added {num}, running total is now: {curr_total}")

print("------------------------------")

#4. Salary increment calculation

curr_sal = 50000
increment_percentage = 10  

raise_am = curr_sal * (increment_percentage / 100)
new_sal = curr_sal + raise_am

print("Your current salary is:", curr_sal)
print("Your raise amount is:", raise_am)
print("Your new salary will be:", new_sal)

print("------------------------------")

#5. Discount calculation using assignment operators

price = 150.0
discount = 15  

multiplier = 1 - (discount / 100)

price *= multiplier  

print("Final price after 15% off:", price)



