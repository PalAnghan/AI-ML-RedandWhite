print("=" * 30)
print("Q 1:")
print("=" *30)

from array import *
'''
arr = array('i',[])
count = 0 
n = int(input("Enter array size: "))

for i in range(n):
    row = int(input("Enter array elements: "))
    arr.append(row)
    count += 1
#print(arr)
print("Length of an array:",count)
'''
print("=" * 30)
print("Q 2:")
print("=" * 30)
'''
arr = array('i',[])
avg = 0
total_sum = 0
n = int(input("Enter array size: "))
count = 0

for i in range(n):
    row = int(input("Enter array elements: \n"))
    arr.append(row)
    total_sum += row
    count += 1

avg = total_sum / count
print(arr)
print("Average:", avg)
'''
print("=" * 30)
print("Q 3:")
print("=" * 30)
'''
arr1 = array('i',[])
arr2 = array('i',[])
arr3 = array('i',[])

n = int(input("Enter array size: "))
print()

print("Enter array A's elements:")

for i in range(n):
    row1 = int(input(f"a[{i}] = "))
    arr1.append(row1)
print()

print("Enter array B's elements:")

for j in range(n):
    row2 = int(input(f"b[{i}] = "))
    arr2.append(row2)
print()  

for k in range(n):
    arr3.append(arr1[k] + arr2[k])


o = ", ".join(str(x) for x in arr3)

print("Output:")
print(f"Array C is: {o}")
'''
print("=" * 30)
print("Q 4:")
print("=" * 30)
'''

arr1 = array('i',[1,2,3,4,5,6,7,8,9,10])

result = [x * 2 for x in arr1]

print("Original array:", arr1)
print("Result after multiplying by 2:", result)
'''
print('=' * 30)
print("Q 5:")
print('=' * 30)
'''
arr = array('i',[10,20,30,40,50])

n = int(input("Enter a number to check if exists or not :"))

for i in range(len(arr)):
    if arr[i] == n:
        print(f"The element are found in this index {i}")
        break
else:
    print(f"The element are not found in array!")


print("Array: ",arr)

'''

print("=" * 30)
print("Q 6:")
print("=" * 30)
'''
arr = array('i',[])

n = int(input("Enter array size: "))

ev_count = 0
od_count = 0

for i in range(n):
    row = int(input("Enter array elements: "))
    arr.append(row)
    
print("-" * 30)

for j in range(n):
      if arr[j]%2 == 0:
        print(f"Even Number: {arr[j]}")
        ev_count += 1

      else:
        print(f"Odd Number: {arr[j]}")
        od_count += 1
        
print("-" * 30)    
print(arr)
print(f"Total Even Numbers: {ev_count}") 
print(f"Total Odd Numbers: {od_count}")
print("-" * 30)
'''

print("=" * 30)
print("Q 7:")
print("=" * 30)
'''
arr = array('i',[10,20,30,40,50])


print(arr)

for i in range(0,len(arr),2):
    print(arr[i])
'''
print("=" * 30)
print("Q 8:")
print("=" * 30)

arr = array('i',[])

n = int(input("Enter Array Size: "))

for i in range(n):
    row = int(input("Enter Rows elements :"))
    arr.append(row)
first = arr[0]
print("First Element: ",first)


middle = len(arr)//2
print("Middle Element: ",arr[middle])

last = arr[-1]
print("Last Element: ",last)

print(arr)













