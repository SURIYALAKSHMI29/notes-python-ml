"""

Single Inheritance

Create a class Animal with a method sound().
Create a child class Dog that inherits from Animal and overrides the sound() method to print "Bark".
Then, create a Dog object and call sound().

"""


class Animal:

    def __init__(self, name):
        self.name = name

    def sound():
        return "woosh"


class Dog(Animal):
    def sound(self):
        return "barks"


dog = Dog("Puppy")
print(dog.sound())
