class person:
    def __init__(self,name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,new_name):
        self._name = new_name

p = person("alice")
print(p.name)
p.name = "TOM"
print(p.name)