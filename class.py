class student:
    college = "AB college"

    @classmethod
    def change_college(cls,name):
        cls.name = name

student.change_college("ABC college")
print(student.college)