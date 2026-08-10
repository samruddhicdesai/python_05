class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def  __str__(self):
        return f"person({self.name}, {self.age})"

    def __repr__(self):
        return f"person(name = {self.name},age = {self.age})"
p = person("Sam",30)

print(str(p))
print(repr(p))
print(p)