print("=" * 40)
print("Q 1:")
print("=" * 40)

#file = open("sample.txt", "x") # not use
#file.close()

file = open("smaple.txt", "w")
file.write("Python is a versatile programming language")
file.close()


print("=" * 40)
print("Q 2:")
print("=" * 40)

file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()

file = open("sample.txt", "w")
file.write("Learning file handling in Python is fun!")
file.close()

print("=" * 40)
print("Q 3:")
print("=" * 40)

file = open("sample.txt","r")

for line in file:
    print(line, end="")

file.close()

print("\n"+ "=" * 40)
print("Q 4:")
print("=" * 40)

file = open("notes.txt", "w")

file.write("Line 1: Python is easy to learn.\n")
file.write("Line 2: It has numerous libraries.\n")
file.write("Line 3: File handling is one of its features.\n")

file.close()

print("=" * 40)
print("Q 5:")
print("=" * 40)

file = open("notes.txt", "a")

file.write("Line 4: Python supports multiple modes of file handling.\n")

file.close()

print("=" * 40)
print("Q 6:")
print("=" * 40)

file = open("notes.txt", "rb")

content = file.read()

print("Binary content:")
print(content)

file.close()

print("=" * 40)
print("Q 7:")
print("=" * 40)

file = open("notes.txt", "r")

content = file.read()

file.close()

words = content.split()
word_count = len(words)

character_count = len(content)

line_count = len(content.splitlines())

print("Total Words:", word_count)
print("Total Characters:", character_count)
print("Total Lines:", line_count)

print("=" * 40)
print("Q 8:")
print("=" * 40)

file = open("notes.txt" , "r+")

print(file.read())

file.write("\nthis is append line.")

file.close()

print("=" * 40)
print("Q 9:")
print("=" * 40)
'''
word = input("Enter word:")
file = open("notes.txt" , "r")

line_no = 1

for line in file:
  if word in line:
    print("Word found at line:" , line_no)
  line_no += 1
file.close()

print("=" * 40)
print("Q 10:")
print("=" * 40)

file1 = open("notes.txt" , "r")

data = file1.read()

file1.close()

file2 = open("newFile.txt" , "x")

file2.close()

file2 = open("newFile.txt" , "w")

file2.write(data)

file2.close()

print("Content copied from source.txt to backup.txt successfully.")
'''

print("=" * 40)
print("Q 11:")
print("=" * 40)

file = open("modes.txt", "r")
content = file.read()
print("r mode:")
print(content)
file.close()

file = open("modes.txt", "w")
file.write("Content written using w mode.\n")
file.close()

print("w mode completed.")

file = open("modes.txt", "a")
file.write("Content added using a mode.\n")
file.close()

print("a mode completed.")

file = open()







































