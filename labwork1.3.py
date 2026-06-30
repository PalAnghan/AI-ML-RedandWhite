# Q 1 :
print("====Q1====")
n = int(input("Enter Number :"))

text = str(n)
text1 = float(n)
text2 = bool(n)

print(type(text),text)
print(type(text1),text1)
print(type(text2),text2)

# Q 2 :
print("====Q2====")
num = float(input("Enter a Number :"))

text = int(num)

print(type(text),text)
print(f"The intger number in no any point value ex: 2,3 & In float have point value ex:2.0 , 3.0")
#


# Q 3 :
print("====Q3====")
num = bool(input("Enter a Number :"))

text = int(num)
text1 = float(num)
text2 = str(num)



print(type(text),text)
print(type(text1),text1)
print(type(text2),text2)

#Q 4 :
print("====Q4====")

integer = 10
flo = 10.0
name = "Pal"
bo = True
fruits = ["Apple", "Banana", "Mango"]
tup = (1,4,6,10)
dic = {"python",1,"java",2}

print(type(integer),id(integer),integer)
print(type(flo),id(flo),flo)
print(type(name),id(name),name)
print(type(bo),id(bo),bo)
print(type(fruits),id(fruits),fruits)
print(type(tup),id(tup),tup)
print(type(dic),id(dic),dic)

# Q 5 :
print("====Q5====")

a = 10
b = 10

print(id(a))
print(id(b))

c = 10
d = 11
print(id(c))
print(id(d))
