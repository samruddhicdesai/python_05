class dog:
    def sound(self):
        print("Brak")

class cat:
    def sound(self):
        print("Meow")

animals = [dog(),cat()]

for animal in animals:
    animal.sound()