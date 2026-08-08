class animal:
    def speak(self):
        print("Sounds aof animals")

class dog(animal):
    def speak(self):
        print("Woof!")

dog1 = animal()
dog1.speak()