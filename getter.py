class person:
    def __init__(self,name):
        self._name= name
    def get_name(self):
        return self._name

p = person("sam")
print(p.get_name())