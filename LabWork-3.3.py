# Q 1 :
'''
num = None

while num != 0:
    num = int(input("Enter a number: "))
'''

num = None

while num != 0:

    num = int(input("Enter a number (0 to stop): "))
    
    if num != 0:
        print(f"You entered: {num}")

print("Loop was Stop because you entered 0.")

print("----------------------------")
# Q 2:

for i in range(1,11):
    print(i*i)
    
print("----------------------------")

# Q 3 :

i = 1
while i<=50:
    if i%2==0:
         print("Even Number 1 to 50 :",i)
    i+=1
    
print("----------------------------")

# Q 4 :

for i in range(1,21,2):
    print("Odd Number :",i)

print("----------------------------")

# Q 5 :

for i in range(5,51,5):
    print(i)
      
print("----------------------------")

# Q 6 :

for i in range(10,0,-1):
    print(i)

print("----------------------------")

# Q 7 :

for i in range(1,51):
    if i%2==0 and i%3==0 and i%5==0:
        print("This Number is Divisible by 2,3and5 :",i)
    elif i%2==0 and i%3==0:
        print("This Number is Divisible by 2,3 :",i)
    elif i%2==0 and i%5==0:
        print("This Number is Divisible by 2,5 :",i)
    elif i%3==0 and i%5==0:
        print("This Number is Divisible by 3,5 :",i)
    elif i%2==0:
        print("This Number is Divisible by 2 :",i)
    elif i%3==0:
        print("This Number is Divisible by 3 :",i)
    elif i%5==0:
        print("This Number is Divisible by 5 :",i)

