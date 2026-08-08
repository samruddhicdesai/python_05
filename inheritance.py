class animals:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(self.name,"is eating")

class dog(animals):
    pass

dog1 = dog("Tom")
print(dog1.name)
dog1.eat()