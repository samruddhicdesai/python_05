class student:
    def __init__(self , name , age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student : {self.name} , Age : {self.age}"

s = student("sam",20)
print(s)