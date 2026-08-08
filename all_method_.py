class student:
    school = "ABC College"

    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        return f"{self.name}:{self.age}"

    @classmethod
    def change_school(cls,new_school):
        cls.school = new_school

    @staticmethod
    def is_age(age):
        return age >=19

s1 = student("Sam", 85)

print(s1.display())
student.change_school("XYZ College")
print(student.is_age(85))