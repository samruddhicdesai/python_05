class animals:
    def eat(self):
        print("Eating")

class dog(animals):
    def bark(self):
        print("Woof")

dog1 = dog()
dog1.eat()
dog1.bark()