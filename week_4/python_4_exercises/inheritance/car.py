"""

Multilevel Inheritance

Create a class Vehicle with method category() printing "I am a Vehicle".
Create a child class Car that inherits from Vehicle and adds method wheels() printing "I have 4 wheels".
Create another child class ElectricCar that inherits from Car and adds method fuel_type() printing "I use electricity".
Create an object of ElectricCar and call all three methods.

"""


class Vehicle:
    def category(self):
        print("I am a Vehicle")


class Car(Vehicle):
    def wheels(self):
        print("I have 4 wheels")


class ElectricCar(Car):
    def fuel_type(self):
        print("I use electricity")


electric_car = ElectricCar()
electric_car.category()
electric_car.wheels()
electric_car.fuel_type()
