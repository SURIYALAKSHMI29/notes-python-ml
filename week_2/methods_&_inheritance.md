# 📑 Table of Contents
---

## 1. Class Methods  

## 2. Static Methods  

## 3. Inheritance  
- Types of Inheritance  
- Examples  

## 4. Operator Overloading  

---

# Class Methods

- Methods that belongs to the class, not instances  
- Defined by using **@classmethod** and replacing *self* with *cls*  
- Method is called on the class, not on an instance  

```python
# hat.py

import random

class Hat:

    houses = ["Gryffindor", "Hufflepuff", "Slytherin", "RavenClaw"]

    @classmethod
    def house(cls):
        return random.choice(cls.houses)
````

```python
# student.py

from hat import Hat

class Student:

    def __init__(self, name, house):
        self.name = name
        self.house = house

    @classmethod
    def get_student(cls):
        name = input("Name: ")
        if not name:
            raise ValueError("Missing Name!")
        house = Hat.house()
        return cls(name, house)
```

```python
# main.py

from student import Student

def main():
    student = Student.get_student()
    print(f"{student.house} is the chosen house for {student.name} ")

if __name__ == "__main__":
    main()
```

---

# Static Methods

* Utility functions grouped together for organizational purpose
* Cannot access class or instance attributes
* Behave as a normal functions defined outside the class
* Logically grouped under a class based on related functionality, improving readability and maintainability

```python
class Arithmetic:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b
   

result = Arithmetic.add(3, 4)
print(result)
```

* Grouped methods with arithmetic operations together

---

# Inheritance

* Allows a child class to inherits the attributes, variables, and methods from base class

## Types of Inheritance:

1. **Single Inheritance:**

   * A child class inherits from one parent class

2. **Multiple Inheritance**

   * A child class inherits from multiple parent classes
   * Python uses MRO (Method Resolution Order) to decide which parent’s method is used first.
   * MRO - left to right, bottom to top
   * **C** inherits from **A** and **B**

3. **Multilevel Inheritance**

   * A child inherits from a parent, and another child inherits from that child.
   * **B** inherits from **A, C** inherits from **B**

4. **Hierarchical Inheritance**

   * Multiple child classes inherits from a single parent
   * **B** inherits from **A**, **C** also inherits from **A**

5. **Hybrid Inheritance**

   * A combination of 2 or more types of inheritance

---

### Example 1: Multiple Inheritance

```python
"""
Multiple Inheritance

Create two classes:
Father with method hobby() that prints "Reading books".
Mother with method hobby() that prints "Gardening".

Create a class Child that inherits from both.
Check which hobby() is called when you create a Child object and call hobby() (MRO test).
"""

class Father:
    def hobby(self):
        return "Reading Books"

class Mother:
    def hobby(self):
        return "Gradening"

class Child(Father, Mother):
    pass

child = Child()
print(child.hobby())  # prints "Reading Books"
```

---

### Example 2: Hierarchical Inheritance

```python
"""
Hierarchical Inheritance

Create a base class Shape with method area().
Create child classes Square and Rectangle that inherit from Shape.
Square should calculate area = side × side.
Rectangle should calculate area = length × breadth.
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
```

---

**Note:**

```python
print(ClassName.mro())   # used to check MRO order
```

---

# Operator Overloading

* In Python, operators (+ , - , \* , < , ==, etc.) are just methods with special names (called **dunder** methods).
* These methods can be overrided to define custom behavior of the class

