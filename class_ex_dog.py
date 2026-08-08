class Dog:
    species = "Canis familiaris"

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(self.name, "says woof!")


dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Lucky", "Labrador")

print(dog1.name)
print(dog2.breed)

dog1.bark()
dog2.bark()

print(Dog.species)