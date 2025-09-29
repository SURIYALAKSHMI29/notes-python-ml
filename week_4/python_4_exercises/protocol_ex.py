from typing import Protocol


# defining a protocol
class Flyer(Protocol):
    def fly(self) -> None: ...


class Bird:
    def fly(self):
        print("Flap flap!")


class Airplane:
    def fly(self):
        print("Whooosh!")


def make_it_fly(f: Flyer):
    f.fly()


make_it_fly(Bird())  # Flap flap!
make_it_fly(Airplane())  # Whooosh!

# Both work, because they implement .fly()
