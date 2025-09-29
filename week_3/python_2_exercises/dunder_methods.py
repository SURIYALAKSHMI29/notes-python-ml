class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __str__(self):
        return f"Vector(x, y) where x is {self.x} and y is {self.y}"

    def __repr__(self):
        return f"Vector({self.x!r} , {self.y!r})"


v1 = Vector(2, 3)
v2 = Vector(1, 4)

print(v1)  # user-friendly, readable
print(repr(v1))  # developer friendly, unambiguous
print("Addition:", repr(v1 + v2))
