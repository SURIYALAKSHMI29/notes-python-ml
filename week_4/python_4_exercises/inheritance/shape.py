"""

Hierarchical Inheritance

Create a base class Shape with method area().
Create child classes Square and Rectangle that inherit from Shape.

Square should calculate area = side × side.

Rectangle should calculate area = length × breadth.

Take user input and compute both areas.

"""


class Shape:
    def area(self, length, breadth):
        return length * breadth


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return super().area(self.side, self.side)


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return super().area(self.length, self.breadth)


square = Square(4)
print(f"Area of Square of side {square.side} is, {square.area()}")


rect = Rectangle(4, 6)
print(
    f"Area of Rectangle of length {rect.length} and breadth {rect.breadth} is, {rect.area()}"
)
