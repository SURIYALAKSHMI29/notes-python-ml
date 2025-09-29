from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    @property
    @abstractmethod
    def species(self):
        pass


class Cat(Animal):
    def sound(self):
        return "Meow"

    @property
    def species(self):
        return "Felis Catus"


cat = Cat()
print(cat.sound())
print(cat.species)
