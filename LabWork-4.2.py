# Q 1:
print("===================")
fruits = ["apple", "banana", "chiku"]
print(fruits)
print(type(fruits))

fruits.append("mango")
print(fruits)

fruit = fruits.pop(0)
print(fruits)

fruits.sort()
fruits.reverse()
print(fruits)

# Q 2:
print("===================")

num = (1,2,3,4,5)
print(type(num))
print(num[2])
#num[2]= 3
print("'tuple' object does not support item assignment")

# Q 3:
print("===================")

num1 = [1,2,3]
num2 = (1,2,3)
print(num1,num2)
num1[0]=8

print(num1,"'tuple' object does not support item assignment")

# Q 4:
print("==================")

numbers = [1,2,3,4,5,6,7,8,9,10]

for num in numbers:
    print(f"Square: {num * num}" )

num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for i in num:
    if i%2==0:
        print(i,"Even")
    else:
        print(i,"odd")

sub = ["hello","WORLD","PyThOn"]
print(sub)
lowercase = [x.lower() for x in sub]
print(lowercase)
