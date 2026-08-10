class vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __mul__(self,scalar):
        return vector(
            self.x * scalar,
            self.y * scalar
        )
    def __str__(self):
        return f"vector ({self.x},{self.y})"

v1 = vector(2,3)
v2 = v1 * 5
print(v2)