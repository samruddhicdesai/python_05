class person:
    def __init__(self,name):
        self._name = name

    def get_name(self):
        return self._name 

    def set_name(self,new_name):
        self._name = new_name

p = person("alice")
print(p.get_name())

p.set_name("Bob")
print(p.get_name())
    