class student:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def intro(self):
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")

student1 = student("Tom",21)
student1.intro()
