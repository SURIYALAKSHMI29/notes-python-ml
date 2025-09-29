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
print(child.hobby())
