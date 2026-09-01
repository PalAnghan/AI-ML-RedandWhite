import math

print("--- Attributes and Methods of the Math Module ---")
math_contents = dir(math)

print(math_contents[:15], "... and more.")



class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self):
        return f"{self.name} is studying."


student_obj = Student("Pal Anghan", 21)

print("\n--- Attributes and Methods of the Custom Student Object ---")
object_contents = dir(student_obj)
print(object_contents)