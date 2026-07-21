print("=" * 20 )
print("Q 1:")
print("=" * 20 )

from array import *
numbers = array("i",[10,20,30,40,50])
# print(numbers)
for i in numbers:
    print(i)


print("=" * 20)
print("Q 2:")
print("=" * 20 )


numbers = array("i",[10,15,20,25,30])
sum = 0
for i in numbers:
    sum += i
print("Sum of Number is",sum)


print("=" * 20)
print("Q 3:")
print("=" * 20 )


n = array("i",[5,10,15,20,25])
print("Starting Array Elements :",n)

n.insert(30,35)
print("Using insert :",n)

n.append(40)
print("Using append :",n)


print("=" * 20)
print("Q 4:")
print("=" * 20 )

n = array("i",[5,10,15,20,25])
print("Original Array :",n)
n.remove(10)
print("Remove 1 index After Array :",n)

print("=" * 20)
print("Q 5:")
print("=" * 20 )

num = array("i",[0,2,3,4,5])
print("Original Array :",num)
num[0] = 1
print("After Update Value :",num)

print("=" * 20)
print("Q 6:")
print("=" * 20 )

def item(a,b):
    if b in a:
        return a.index(b)
    return -1

numbers = [10,20,30,40,50]
print(item(numbers,20))

print("=" * 20)
print("Q 7:")
print("=" * 20 )

arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
print("First Array :",arr1)
print("Second Array :",arr2)
result = arr1 + arr2
print("Concateenate of two Array :",result)


