student = {"name": "Alice","age": 25, "grade":"A","major":"Computer Science"}

print(student.keys())

print(student.values())

print(student.items())

print(student.get("name"))
print(student.get("grade","not Found"))

major = student.pop("major")
print(major)
print(student)

last_item = student.popitem()
print(major)
print(student)

student.clear()
print(student)