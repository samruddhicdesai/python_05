python = {"A","B","C","D"}
java = {"C","D","E","F"}

print("Students learning either language : ",java.union(python))
print("Students learning both : ",python.intersection(java))
print("Student learning python but not java:",python.difference(java))
print("student learning jave but not python : ",java.difference(python))