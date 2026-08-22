class animal:
    def sound(self):
        print("Animal sound")

class dog(animal):
    def sound(self):
        print("Brak")

d = dog()
d.sound()