print(" ====== Q.1 ======")
'''
try:
    a = float(input("Enter a first number: "))
    b = float(input("Enter a second number: "))

    result = a/b
    print("Result: ",result)
    
except ZeroDivisionError:
    print("Error : Cannot Divsiable with 0")
'''

print(" ====== Q.2 ======")
'''
try:
    numbers = [10,20,30,40,50]
    index = int(input("Enter list index: "))
    print("Element: ", numbers[index])
except IndexError:
    print("Error: Index Error")
except ValueError:
    print("Error: Value Error")
'''

print(" ====== Q.3 ======")
'''
try:
    filename = input("Enter file name: ")
    file = open(filename, "r")
    content = file.read()
except FileNotFoundError:
    print("Error: File was not found.")
except PermissionError:
  print("Error:Permission denied.")
except OSError:
  print("Error:File could not be opened.")
else:
  print("File Content")
  print(content)
  file.close()
'''   

print(" ====== Q.4 ======")
'''
try:
    name = "Pal Anghan"
    print(name)

    index = int(input("Enter a index number: "))
    result = name[index]
    print(result)


except ValueError:
    print("Error: ValueError")
except IndexError:
    print("Error: Index Error ")
'''
print(" ====== Q.5 ======")
'''
file = None
try:
    filename = input("Enter Filename: ")
    file = open(filename, "r")
    print("File Content:")
    print(file.read())
except FileNotFoundError:
    print("Error : file not found.")

except PermissionError:
    print("Error : File does not exist.")

finally:
    if file is not None:
        
        file.close()

    print("File Operation Completed.")    
'''
print(" ====== Q.6 ======")
'''
try:
    num1 = float(input("Enter a first number: "))
    num2 = float(input("Enter a second number: "))

    result = num1/num2
    print("Result: ",result)
except ZeroDivisionError:
    print("Error: Zero cannot")
except ValueError:
    print("Error: ValueError")
finally:
    print("Calculate completed")
    
'''
print("======= Q.7 =======")    

while True:
    try:
        number = int(input("Enter a positive number: "))
        
        
        if number < 0:
            raise ValueError("Negative numbers are not allowed!")
            
        square = number * number
        print("Square: ", square)
        break

    except ValueError as e:
        print("Error: ", e)
        print("Please try again...\n") 


    






















