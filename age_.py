class person:
    def __init__(self,age):
        self._age = age

    def set_age(self,age):
        if age >= 0:
            self._age = age
        else:
            print("Invaild age")

    def get_age(self):
        return self._age

p = person(20)

p.set_age(25)
print(p.get_age())