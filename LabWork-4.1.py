# Q 1 :

f_name = input("Enter Your First Name : ")
l_name = input("Enter Your Last Name : ")

print(f"Hello, {l_name} ,{f_name}!")

print("= " * 15)

# Q 2:

#item = {}
#price = {}
# print(f"This price of {item} is {price} dollers.")
item = "apple"
price = 5.50
print(f"This price of {item} is {price} dollers.")

print("= " * 15)

# Q 3 :

a = input("Name : ")
print("".join(reversed(a)))

word = a[::-1]

print("Palindrome :",a == word)

print("= " * 15 )

# Q 4 :

n = input("Enter Your Name : ")
print("Upper Case : ",n.upper())
print("Lower Case : ",n.lower())
print("Title Case : ",n.title())

print("= " * 15)

# Q 5 :

print("Machine Learning and AI are trending ")

ai = " Artificial Intelligence "
print(f"Machine Learning and{ai}are trending ")

data = "data data mining and big data"
print("data count :",data.count("data"))

print("= " * 15)

# Q 6 :
a = "apple banana  grapes"
print(a.split())

w =["Python" , "is" , "awesome"]
sen = " ".join(w)
print(sen)

multi = """Python
is
Awesome """

for line in multi.splitlines():
    print(line)

print("= " * 15)

# Q 7 :

n = "Hello World!"
print(n.startswith("Hello") and n.endswith("World!"))

t = "Data123#Science!"
c = ""

for ch in t:
    if ch.isalpha():
        c += ch

print(c)

a = "Python"
print(a)
result = a[::-1]
print(result)
