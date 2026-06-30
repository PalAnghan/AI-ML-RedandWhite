#nested loops

for i in range(1,5):
    for j in range(1,4):
        print(j, end="")
    print()

print("====================")

fruits = ["Apple", "Banana", "Mango"]

for idx , fruit in enumerate(fruits):
    print(idx,fruit)
print("===================")

for name in reversed([1,2,3]):
    print(name)

print("===================")

for i in range(1,6):
    if i == 4:
        break
    print(i)
print("===================")

for i in range(1,6):
    if i == 2:
        continue
    print(i)
print("===================")

for i in range(1,6):
    pass
