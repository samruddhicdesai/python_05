class vector:
    def __init__(self , x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return vector(
            self.x + other.x,
            self.y + other.y
        )
    def __sub__(self,other):
        return vector(
            self.x - other.x,
            self.y - other.y
        )
    def __mul__(self,scalar):
        return vector(
            self.x * scalar,
            self.y * scalar
        )
    def __str__(self):
        return f"({self.x},{self.y})"


v1 = vector(2,3)
v2 = vector(3,4)
v3 = v1 + v2
print("Add :",v3)
v4 = v1 - v2
print("sub :",v4)
v5 = v2 * 5
print("Mul : ",v5)


