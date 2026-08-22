class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def intro(self):
        print(f"My name is {self.name} and My age is {self.age}")

s1 = student("Sam",18)
s2 = student("Tom",21)
s1.intro()
s2.intro()