class circle:
    def __init__(self ,radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius
    @property
    def area(self):
        return 3.14*self._radius*self._radius

c1 = circle(5.5)

print(c1.radius)
print(c1.area)