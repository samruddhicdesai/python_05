student = {
    "name":"sam",
    "age" : 20,
    "branch":"CSE"
}
print(student)

print(student["age"])

student["age"]=21
print(student)

student["city"] = "Kolhapur"
print(student)

print(student.keys())

print(student.values())

print(student.items())

student.pop("age")
print(student)

student.clear()
print(student)
