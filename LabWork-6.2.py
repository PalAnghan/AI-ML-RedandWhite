print("="*40)
print("Q-1")
print("="*40)

"""
def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

num = int(input("Enter a factorial Number : "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial: ", factorial(num))
"""

print("="*40)
print("Q-2")
print("="*40)

"""
def fibonacci(n):
    if n < 0:
        return "Invaild Input"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


num = int(input("Enter a fibonacci : "))

print("Fibonacci: ",fibonacci(num))
"""

print("="*40)
print("Q-3")
print("="*40)

"""
def reverse(s):
    if s == "":
        return ""
    return reverse(s[1:]) + s[0]

string = input("Enter a String: ")
print("Reversed String:", reverse(string))
"""

print("="*40)
print("Q-4")
print("="*40)

"""
def sum_number(n):
    if n < 10:
        return n
    return n % 10 + sum_number(n // 10)

num = int(input("Enter a Number: "))

if num < 0:
    print("Invaild Number")

print("Sum of Digits:", sum_number(num))
"""

print("="*40)
print("Q - 5")
print("="*40)


def is_prime(num, i=2):
    if num < 2:
        return False
    if i == num:
        return True
    if num % i == 0:
        return False
    return is_prime(num, i + 1)

def prime_number(start, end):
    if start > end:
        return

    if is_prime(start):
        print(start)

    prime_number(start + 1, end)
start = int(input("Enter Start: "))
end = int(input("Enter End: "))

print("Prime numbers are:")
prime_number(start, end)


print("="*40)
print("Q-6")
print("="*40)


number_list = [1,2,3,4,5,6,7]

result = list(map(lambda x : x * x, number_list))

print(result)


print("="*40)
print("Q-7")
print("="*40)


number_check = [1,2,3,4,5,6,7,8,9]

result = list(filter(lambda x: x%2==1,number_check))

print(result)


print("="*40)
print("Q-8")
print("="*40)


number_largest = lambda x ,y, z : max(x, y, z)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

print("number largest : ", number_largest(num1, num2, num3))


print("="*40)
print("Q-9")
print("="*40)


total = 0

print("Total before :",total)
def sum():
    global total

    total += 1

sum()
sum()
sum()
sum()

print("Total after :",total)


print("="*40)
print("Q-10")
print("="*40)


total = 0

def add_number(num):
    global total
    total = total + num

n = int(input("How many numbers? "))

for i in range(n):
    num = int(input("Enter number: "))
    add_number(num)

print("Total Sum:", total)


print("="*40)
print("Q-11")
print("="*40)


username = "Guest"

def change_name():
    global username
    username = input("Enter new username: ")

print("Before:", username)
change_name()
print("After:", username)


print("="*40)
print("Q-12")
print("="*40)


count = 0

def init():
    global count
    count = int(input("Enter Initial Value: "))
    
def increment():
    global count
    value = int(input("Enter increment value: "))
    count = count +value

init()
increment()

print("Final Value : ",count)   


print("="*40)
print("Q-13")
print("="*40)


x =100

def display():
    x =50
    print("Local x:", x)

display()

print("Global x:", x)

"""
print("="*40)
print("Q-14")
print("="*40)

def values(num):
    return sum(num), max(num), min(num)

numbers = [10, 20, 30, 40, 50, 60]

total , maximum , minimum = values(numbers)

print("Sum: ", total)
print("Maximum: ",maximum)
print("Minimum: ",minimum)


print("="*40)
print("Q-15")
print("="*40)

"""
def rectangle(length,width):
    area = length * width
    perimeter = 2 * (length * width)
    return area, perimeter

l = int(input("Enter length:"))
w =int(input("Enter width: "))

a, p = rectangle(l,w)

print("Area:", a)
print("perimeter:", p)


print("="*40)
print("Q-16")
print("="*40)


def square_cude(n):
    return n**2, n**3

number = int(input("Enter a Number : "))

square, cude = square_cude(number)

print("square:", square)
print("cude:", cude)


print("="*40)
print("Q-17")
print("="*40)


def split_string(string):
    vowels = ""
    others = ""

    for ch in string:
        if ch.lower() in "aeiou":
            vowels += ch
        else:
            others += ch

    return vowels , others
        
string = input("Enter a string: ")

v, o = split_string(string)

print("Vowels: ", v)
print("Other: ", o)



print("="*40)
print("Q-18")
print("="*40)


def separate(words):
    vowels = []
    consonants = []

    for word in words:
        if word[0].lower() in "aeiou":
            vowels.append(word)
        else:
            consonants.append(word)

    return vowels, consonants

words = ["Apple", "Ball", "Orange", "Cat", "Umbrella"]

v, c = separate(words)

print("Vowel Words:", v)
print("Consonant Words:", c)

