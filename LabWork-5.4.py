students = [
    {"id":"101","name":"Alice","score":85},
    {"id":"102","name":"Bob","score":78},
    {"id":"103","name":"Charlie","score":92}
    ]

for student in students:
    print(student)

print("=" * 20)

sum = 0
for student in students:
    sum += student["score"]

avg = sum/len(students)
print("Average: ",avg)

print("=" * 20)

students.append({
    "id":104,
    "name":"lucky",
    "score":70
    })
print(students)

print("=" * 20)

students[1]['score'] = 88
'''
for student in students:
    if student["id"] == 102:
        student["score"] = 88
'''
print(students)

print("=" * 20)

for student in students:
    if student["name"] == "Charlie":
        students.remove(student)
        break
print(students)

print("=" *20)

for student in students:
    if student["score"] > 80:
        print(student["name"])

print("=" * 20)

n = len(students)

for i in range(n):
    for j in range(n - i - 1):
        if students[j]["score"] < students[j + 1]["score"]:
            temp = students[j]
            students[j] = students[j + 1]
            students[j + 1] = temp

print("Students after sorting:")
for s in students:
    print(s)

print("=" * 20)

highest = students[0]

for i in students:
    if i["score"] > highest["score"]:
        highest = i

print("highest Scorer :")
print(highest)

print("=" * 20)

for s in students:
    if s["score"] > 90:
        grades = "A"
    elif s["score"] > 80:
        grades = "B"
    else:
        grades = "C"

    print(f"Name: {s['name']} | Score: {s['score']} | Grade: {grades}")


