import dataclasses
from dataclasses import dataclass


## Custom __post_init__
@dataclass
class Person:
    name: str
    age: int
    email: str

    def __post_init__(self):
        if self.age < 18:
            raise ValueError(f"Age must be >= 18, got {self.age}")


p1 = Person("suriya", 20, "suriya@gmail.com")
# p2 = dataclasses.replace(p1, age=17)  # ValueError: Age must be >= 18, got 17
p3 = dataclasses.replace(p1, age=21)

print(p1)  # Person(name='suriya', age=20, email='suriya@gmail.com')
print(p3)  # Person(name='suriya', age=21, email='suriya@gmail.com')
