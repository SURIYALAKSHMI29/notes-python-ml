# Data Classes and NamedTuple

## Table of Contents
1. [Data Class Module](#data-class-module)
   - [Module Contents](#module-contents)
2. [NamedTuple](#namedtuple)
   - [Operations on NamedTuple](#operations-on-namedtuple)

---

# Data Class Module

- Introduced in python 3.7 → utility tool to make structured classes specially for storing data
- Implemented by using *decorators* with classes and attributes are declared using *Type Hints*
- Provides an in-built `__init__()` constructor to classes which handle the data and object creation for them
- Also implements `__repr__()`

### Checking equality

- == between 2 objects → checks for the same memory location
- Where DataClass objects checks for the equality of data present in it
- Implements `__eq__` method → checks for data equality

## Module Contents

### dataclass

@dataclasses.**dataclass**(***, *init=True*, *repr=True*, *eq=True*, *order=False*, *unsafe_hash=False*, *frozen=False*, *match_args=True*, *kw_only=False*, *slots=False*, *weakref_slot=False*)

- `__init__()` → is generated
- `__repr__()` → Returns a string that have class name and the name and repr of each field, in order they defined in the class
- `__eq__()` → compares instances field by field, in order of declaration, just like comparing tuples; Both instances in the comparison must be of the identical type
- order
    - if true,`__lt__()`, `__le__()`, `__gt__()`, `__ge__()` methods will be generated
    - If the class already defines any of these methods, then *TypeError* is raised
    - If order is True, but eq is False, then *ValueError* is raised
- unsafe_hash
    - Forces dataclass to create `__hash__()` even if it is not safe
    - If eq and frozen are True, hash() will generate a `__hash__()` methods
    - Defining explicitly `__hash__()` and again setting unsafe_hash as True will results in *TypeError*
    - Having a `__hash__()` implies that instances of the class are immutable
- frozen
    - If True, assigning to fields will generate an exception; Emulates read-only frozen instances
    - If `__setattr__()` or `__delattr__()` is defined and frozen is true → *TypeError* is raised
    - dataclasses will add `__setattr__()` or `__delattr__()` methods to the class, when invoked → raises FrozenIntsanceError
- match_args → `__match_args__` tuple will be created from the list of non-keyword-only parameters to the generated __init__() method
- kw_only → If True, All the fields will be marked as keyword-only

> keyword-only fields are not included in `__match_args__`
> 

### field

dataclasses.**field**(***, *default=MISSING*, *default_factory=MISSING*, *init=True*, *repr=True*, *hash=None*, *compare=True*, *metadata=None*, *kw_only=MISSING*)

- each field properties can be set individually as required
- *field(default_factory=some_callable) →* call the factory function each time a new instance is created, otherwise mutable objects will be shared among all the instances

```python
from dataclasses import dataclass, field

@dataclass
class Student:
    name: str
    roll: int
    grades: list[float] = field(default_factory=list)
    # call the factory function each time a new instance is created

    def avg_grade(self):
        if not self.grades:
            return 0.0
        return round((sum(self.grades) / len(self.grades)), 2)

s1 = Student("laksh", 101)
s2 = Student("Arav", 102, [90, 80, 95])

print(s1.avg_grade())  # 0.0
print(s2.avg_grade())  # 88.33
```

### Make Data class

dataclasses.**make_dataclass**(*cls_name*, *fields*, ***, *bases()*, *namespace=None*, *init=True*, *repr=True*, *eq=True*, *order=False*, *unsafe_hash=False*, *frozen=False*, *match_args=True*, *kw_only=False*, *slots=False*, *weakref_slot=False*, *module=None*)

### dataclasses.replace(obj, /, **changes)

- Copy, with some modifications
- Creates a new object of the same type as *obj,* replacing fields with values from changes
- If obj is not a DataClass or if key in changes are not field names of the given dataclass→ raises *TypeError*
- if a field is defined with init=False, then it won’t be copied form the source object, but rather initialised in __post_init__()

# NamedTuple

- Used to create simple, light-weight data structures similar to a class
- Instances are Immutable
- Does not support inheritance
- They contain keys that are hashed to a particular value; Supports both access from key-value and iteration
- **Syntax**
    
    ```python
    from collections import namedtuple
    
    **# NamedTuple Syntax:**
    namedtuple(typename, field_names)
    ```
    

## Operations on NamedTuple

### Create a NameTuple

```python
Card = namedtuple("Card", ["rank", "suite"])
ranks = [str(n) for n in range(2, 11)]
ranks.extend(["J", "Q", "K", "A"])    # extend -> performs in-place, so returns None
suites = ["spade", "hearts", "diamonds", "clubs"]

class Deck:
    def __init__(self):
        self.card = [Card(rank, suite) for rank in ranks for suite in suites]

deck = Deck()
```

### Access Operations

- Access by index
- Access by keyname
- Access Using getattr()

```python

# here card -> namedtuple
card = deck.card[0]  # spade 2

# Accessing
# by index
print(card[1])    # spade

# by keyname
print(card.rank)    # 2

# by getattr()
print(getattr(card, "suite"))    # spade
```

### Conversion

- Using _make() → return a namedtuple from the iterable passed as argument
- Using _asdict() → returns the OrderedDict()
- Using “**” (double star) operator   → converts dictionary into the namedtuple()

```python
# Conversion
# using _make()
l1 = ["4", "spade"]
t1 = ["A", "hearts"]

print(card._make(l1))     # Card(rank='4', suit='spade')
print(card._make(t1))     # Card(rank='A', suit='hearts')

# using _asdict()
print(card._asdict)       # <bound method Card._asdict of Card(rank='2', suit='spade')>

# using **
dic1 = {"rank": "K", "suit": "clubs"}
print(Card(**dic1))       # Card(rank='K', suit='clubs')

# using *
print(Card(*l1))          # Card(rank='4', suit='spade')
```

### Others

- **_fields -** used to get all the key names of the namespace declared
    
    ```python
    print(Card._fields)  # ('rank', 'suit')
    ```
    
- **_replace() -** Creates a new instance with some fields changed
    
    ```python
    # _replace() -> returns a new Card obj
    print(card._replace(rank="20"))  # Card(rank='20', suit='spade')
    print(card)  # Card(rank='2', suit='spade')
    ```
    
- **`__new__()`**
    - Creates a new instance of the namedtuple
    - It is called before `__init__`, and it returns the instance
    - Card( ”A”, ”spades” ) → calls `__new__` internally
- **`__getnewargs__()` -** returns namedtuple as a plain tuple
    
    ```
    # `__getnewargs__()`
    t2 = card.`__getnewargs__()`
    print(t2)  # ('2', 'spade')
    ```
