class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(9, 8)
v2 = Vector(1, 98)

print(v1 + v2)  # Vector(10, 106)
