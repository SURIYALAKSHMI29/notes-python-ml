from dataclasses import dataclass


## Frozen Data Class
@dataclass(frozen=True)
class Point:
    x: int
    y: int


p = Point(3, 6)
print(p)  # Point(x=3, y=6)
# p.x = 4  # dataclasses.FrozenInstanceError: cannot assign to field 'x'
