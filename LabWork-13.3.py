print("===== Q.1 =====")
"""
import uuid

random_uuid = uuid.uuid4()
print("Random UUID:", random_uuid)

# Generate a UUID using a namespace and a name
namespace = uuid.NAMESPACE_DNS
name = "example.com"

name_uuid = uuid.uuid5(namespace, name)
print("UUID using namespace and name:", name_uuid)
"""
print("===== Q.2 =====")
'''
import uuid

student_uuids = {}

student_ids = ["S101", "S102", "S103", "S104", "S105"]

for student_id in student_ids:
    student_uuids[student_id] = str(uuid.uuid4())

print("Student IDs and their UUIDs:")

for student_id, student_uuid in student_uuids.items():
    print(student_id, ":", student_uuid)
'''

print("===== Q.3 =====")
'''
import uuid

uuid1 = uuid.uuid4()
uuid2 = uuid.uuid4()

if uuid1 == uuid2:
    print("uuid are match!...")
else:
    print("uuid are not match")
'''

print("===== Q.4 =====")
'''
import uuid

class E_commerce:

    def __init__(self):
        self.order = {}
        
    
    def display(self, item_name):
        order_id = uuid.uuid4()
        self.order[order_id] = item_name
        return order_id
    
system = E_commerce()
placed_id = system.display("laptop")
print(f"Generated Order ID: {placed_id}")
'''

print("===== Q.5 =====")
'''
numbers = [5, 2, 9, 1, 7]

ascending_order = sorted(numbers)
print("Ascending order:", ascending_order)

decending_order = sorted(numbers, reverse=True)
print("Decending order:", decending_order)
'''
print("===== Q.6 =====")
'''
words = ["apple", "banana", "kiwi", "cherry",  "grape"]

sorted_words = sorted(words,key=len)
print("Words sorted by length:", sorted_words)

soretd_by_last_letter = sorted(words, key=lambda word: word[-1])
print("Words sorted by last letter:", soretd_by_last_letter)
'''

print("===== Q.7 =====")
'''
students = [
    {"name": "A", "age": 22},
    {"name": "B", "age": 19},
    {"name": "C", "age": 25},
    {"name": "D", "age": 20}
]

sorted_students = sorted(students, key=lambda student: student["age"])
print("Students sorted by age:")
print(sorted_students)
'''

print("===== Q.8 =====")
'''
words = ["python", "data science", "uuid", "lambda"]

upper_case_words = list(map(str.upper, words))
print("Words in uppercase:", upper_case_words)
'''

print("===== Q.9 =====")
'''
number = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x*x, number))
print("Squared numbers:", squared_numbers)
'''

print("===== Q.10 =====")
'''
prices = [100.00, 49.99, 10.00, 250.50]
final_prices = list(map(lambda price: round(price * 1.18, 2), prices))
print("Original prices:", prices)
print("Final prices after 18% tax:", final_prices)
'''

print("===== Q.11 =====")
'''
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)
'''

print("===== Q.12 =====")
'''
words = ["python", "ai", "machine", "data", "learning", "code", "development"]
long_words = list(filter(lambda word: len(word) > 5, words))

print("Original words:", words)
print("Words with more than 5 characters:", long_words)
'''

print("===== Q.13 =====")
'''
students = [{"stu1": 98}, {"stu2": 35}, {"stu3": 42}, {"stu4": 80}, {"stu5": 88}]

pass_student = list(filter(lambda student: list(student.values())[0] >= 40, students))
print("Students who passed (score >= 40):", pass_student)
'''

print("===== Q.14 =====")
'''
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print("Product of all numbers:", product)
'''
print("===== Q.15 =====")
'''
from functools import reduce
words = ["apple", "banana", "watermelon", "kiwi", "cherry"]

logest_word = reduce(lambda x,y : x if len(x) > len(y) else y, words)
print("Longest word:", logest_word)
'''

print("===== Q.16 =====")
from functools import reduce
words = ["apple", "banana", "watermelon", "kiwi", "cherry"]

sentence = reduce(lambda x, y: x + " " + y, words)
print("Concatenated sentence:", sentence)
