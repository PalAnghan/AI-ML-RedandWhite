print("=" * 30)
print("Q 1:")
print("=" * 30)

from array import *
"""
matrix = []

for i in range(3):
    row = list(map(int,input(f"Enter Rows {i+1} :").split()))
    matrix.append(row)

print("matrix :")

for row in matrix:
    for value in row:
        print(value, end = " \t")
    print()

print(matrix)
"""
print("=" * 30)
print("Q 2:")
print("=" * 30)
"""
matrix = []

for i in range(2):
    rows = list(map(int,input(f"Enter Rows {i + 1}: ").split()))
    matrix.append(rows)

print("Matrix:")

for rows in matrix:
    for value in rows:
        print(value,end="\t")
    print()
print(matrix)
"""
print("=" * 30)
print("Q 3:")
print("=" * 30)
"""
rows = int(input("Enter Rows: "))
cols = int(input("Enter Colums: "))

matrix = []

for i in range(rows):
    row = list(map(int,input(f"Enter Rows {i+1}: ").split()))
    matrix.append(row)
print(matrix)

total = 0

for row in matrix:
    for value in row:
        total += value

print("sum :",total)
"""  
print("=" * 30)
print("Q 4:")
print("=" * 30)
'''
rows = int(input("Enter Rows : "))
cols = int(input("Enter Colums : "))

matrix = []

for i in range(rows):
    row = list(map(int,input(f"Enter Rows {i+1}: ").split()))
    matrix.append(row)
print("Matrix:")

min_val = min(num for row in matrix for num in row)
max_val = max(num for row in matrix for num in row)
print("Minimum Number of the Matrix is",min_val)
print("Maximum Number of the Matrix is",max_val)
'''

print("=" * 30)
print("Q 5:")
print("=" * 30)

'''
arr = list(map(int,input("Enter array elements: ").split()))
arr.sort()
print(arr)

'''
print("=" * 30)
print("Q 6:")
print("=" * 30)
'''
list_stu = [
    ("Pal",99),
    ("Shrey",75),
    ("Nihar",92),
    ("Vastal",85),
    ("Dixit",80)
]

sort_marks = sorted(list_stu,key = lambda x : x[1] )
print(sort_marks)
'''
print("=" * 30)
print("Q 7:")
print("=" * 30)
'''
list_person =[
    {"Name":"Pal","age":21},
    {"Name":"Shrey","age":20},
    {"Name":"Max","age":4},
    {"Name":"Jacksen","age":45}
]

store_person = sorted(list_person,key = lambda x : x["age"])
print(store_person)
'''
print("=" * 30)
print("Q 8:")
print("=" * 30)

list_stu=[10,23,13,53,23]
use_sort = list_stu.sort()
print("using sort:",use_sort)

use_sorted = sorted(list_stu)
print("using sorted:",use_sorted)
