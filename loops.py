#while loop

# print 1 to 5

i=1
while i<=5:
    print(i)
    i+=1

print("===================")
#print 5 to 1
i=5
while i >= 1:
    print(i)
    i-=1
    
print("===================")

#for loop

#print 1 to 5

for i in range(1,5):
    print(i)

print("===================")

#print 5 to 1

for i in range (5,0,-1):
    print(i)
print("===================")

name = "Pal"

for i in name:
    print(i)
print("===================")

fruits = ["Apple","Banana","Mango"]

for items in fruits:
    print(items)
print("===================")

for i in range(5):
    print(i)

print("===================")

for i in range(0,11,2):
    print(i)

print("===================")

for i in range(10,0,-1):
    print(i)
print("===================")

n = int(input("Enter a Number :"))

for i in range(1,11):
    print(f"{n} X {i} :",n*i)

print("===================")

# in list find x value

list = [1,16,25,36,49,65,75,89,91,100]
print("Guess a number and check is exits in list or not ,number between 1 to 100")
x=int(input("Check a Number Exits in List :"))

for i in list:
    if i == x:
        print(f"Yes, {x} This Number are Exits in list  :",i)
        break
    elif i != x:
        print(f"Oops, {x} You Guess Wrong Number ! only this number are extis in list : {i} ")

print("===================")

