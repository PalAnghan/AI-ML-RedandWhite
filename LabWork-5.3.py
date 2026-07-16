# Q 1 :

num = {1,2,3,4,5}
print(num)

num.add(6)
print("Add 6 Number : ",num)

num.remove(3)
print("Remove 3 Number : ",num)

print("Is 2 Present ?" , 1 in num)

print(num)

print("= " * 25)
# Q 2 :

set_a = {1,2,3,4}
set_b = {3,4,5,6}

print(set_a)
print(set_b)

print("Union : ",set_a.union(set_b))
print("Intersection : ",set_a.intersection(set_b))
print("Difference : ",set_b.difference(set_a))
print("Difference : ",set_a.difference(set_b))

print("= " * 25)

# Q 3 :
student = {
    "name" : "Pal",
    "age" : 20,
    "grade" : "A"
    }
for key in student.keys():
    print("Key :",key)
for value in student.values():
    print("Value :",value)

print(student['name'])

student["city"] = "Delhi"

student["age"] = 21

print(student)

del student["grade"]

print(student)

print("= " * 25)

# Q 4 :

keys = ['id' , 'name' , 'email']
values = [11 , 'Pal' , 'Pal@gmail.com']

user = {}

for i in range(len(keys)):
    user[keys[i]] = values[i]

print(user)

print("= " * 25)

# Q 5 :

num ="123"

print(type(num))

nums = int(num)

print(type(nums))

list_1 = [1 , 2 , 3 , 4]

tuple_1 = tuple(list_1)

print(tuple_1)

pairs = [(1 , "A") , (2 , "B")]

print(dict(pairs))

print("= " * 25)

# Q 6 :
fruits = ['apple', 'banana', 'cherry']
print("Before Delete :",fruits)
del fruits[2]
print("After Delete :",fruits)

