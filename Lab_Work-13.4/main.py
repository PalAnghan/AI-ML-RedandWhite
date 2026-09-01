import math_utils
'''
num1 = 10
num2 = 5

print(f"Addition: {math_utils.add(num1, num2)}")
print(f"Subtraction: {math_utils.subtract(num1, num2)}")   
print(f"Multiplication: {math_utils.multiply(num1, num2)}")
try:
    print(f"Division: {math_utils.divide(num1, num2)}")
except ValueError as e:
    print(e)
'''

import string_utils
'''
sample_text = "Hello, World!"
vowel_count = string_utils.count_vowels(sample_text)
print(f"Number of vowels in '{sample_text}': {vowel_count}")
'''

import greet

import helper
'''
print("This is the main program starting up.")
result = helper.useful_function()
print(f"Result from helper: {result}")
'''

from shapes import circle
from shapes import rectangle

'''
r = 5
print("--- Circle Operations ---")
print(f"Radius: {r}")
print(f"Area: {circle.area(r):.2f}")
print(f"Circumference: {circle.circumference(r):.2f}\n")

l, w = 10, 4
print("--- Rectangle Operations ---")
print(f"Dimensions: {l}x{w}")
print(f"Area: {rectangle.area(l, w)}")
print(f"Perimeter: {rectangle.perimeter(l, w)}")
'''

from utilities import file_utils, date_utils
'''
print("--- File Operations ---")
test_file = "sample.txt"
text_to_write = "Hello! This file was created using my custom package."

print(file_utils.write_file(test_file, text_to_write))

read_content = file_utils.read_file(test_file)
print(f"Read Content: '{read_content}'\n")


print("--- Date Operations ---")
start_date = "2026-01-01"
end_date = "2026-09-01"

days = date_utils.days_between(start_date, end_date)
print(f"Start Date: {start_date}")
print(f"End Date:   {end_date}")
print(f"Days between dates: {days} days")
'''

import geometry

c_area = geometry.circle_area(7)
print(f"Circle Area: {c_area:.2f}")

t_area = geometry.triangle_area(10, 5)
print(f"Triangle Area: {t_area}")

