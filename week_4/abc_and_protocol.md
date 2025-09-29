# Abstract Classes and Protocols

## Table of Contents
1. [Abstract Class](#abstract-class)
2. [Abstract Base Classes (ABC)](#abstract-base-classes-abc)
3. [Protocols (typing.Protocol)](#protocols-typingprotocol)
4. [ABC vs Protocol](#abc-vs-protocol)

---

# Abstract Class

- A class that cannot be instantiated on its own and is designed to be a blueprint for other classes
    - Trying to instantiates them returns *TypeError*
- Used when
    - Define a common interface for all subclasses
    - Provide shared functionality while still requiring subclasses to implement specific behavior

## Abstract Base Classes (ABC)

- **Nominal Typing** → a class must explicitly inherit from the ABC
- Enforces at runtime: if abstract methods are not implemented → TypeError
- Ensures that the sub-classes follow a consistent structure
- Python provides the *abc module* to define ABCs
- A helper class that has ABCMeta as its Metaclass → so abstract base class can be created by simply deriving from ABC

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Cat(Animal):
    def sound(self):
        return "Meow"

cat = Cat()
print(cat.sound())   # Meow
````

### Abstract Methods 
* Defined in an abstract class but do not have an implementation

### Concrete Methods
* Methods that have full implementations in an abstract class

### Abstract properties

* work like abstract methods but are used for properties
* Declared with @property decorator and marked as abstract

```python
from abc import ABC, abstractmethod
class Animal(ABC):
    @property
    @abstractmethod
    def species(self):
        pass

class Cat(Animal):
    @property
    def species(self):
        return "Felis Catus"
cat = Cat()
print(cat.species)     # Felis Catus
```

# Protocols (typing.Protocol)

* Define structural typing or “**duck typing**” within the language
* A Protocol is like an interface: it defines a set of methods/attributes a class must have**, without requiring inheritance**
* defined using the typing.protocol class or the typing.Protocol decorator
* **Usage**:

  * Used in type hints for APIs and libraries
  * Python stdlib uses them
* No runtime check → only type checkers enforce it
* A class is called an explicit subclass of a protocol if it includes the protocol in its MRO (Method Resolution Order)
* If a class defines all the protocol’s required members (with type-compatible signatures) without inheriting from it, that class is said to implement the protocol implicitly (i.e. structural compatibility
* Default method bodies in protocols can be inherited only by explicit subclasses, not by structurally compatible ones

```python
from typing import Protocol

# defining a protocol
class Flyer(Protocol):
    def fly(self) -> None:
        ...

class Bird:
    def fly(self):
        print("Flap flap!")

def make_it_fly(f: Flyer):
    f.fly()

make_it_fly(Bird())      # Flap flap!

# Will work, because it implement .fly()
```

# Runtime Checkable Protocols

* By default, Python protocols do not suppor*t isinstance()* or *issubclass()* checks. That’s because protocols are about static type compatibility, not runtime enforcement

  * But can opt in using ***@runtime_checkable*** to allow those checks

```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class Flyer(Protocol):
    def fly(self) -> None:
        ...
```

# ABC vs Protocol

* Use **ABC** → when **strict enforcement at runtime** is concerned

  * Example: frameworks, libraries where breaking the contract must raise an error.
* Use **Protocol** → when **flexibility** is concerned and rely on **static type checkers** to catch mistakes.

  * Example: utility functions, API contracts, libraries using duck typing

