# Fluent Python - Chapter 1: Fundamental Language Constructs

# Table of Contents
1. [Fundamental Language Constructs](#fundamental-language-constructs)
2. [Dunder Methods (Magic methods)](#dunder-methods-magic-methods)
3. [Special Methods Usage](#special-methods-usage)
4. [Collections](#collections)
   - [Card Example](#here-card-can-be-created-in-2-ways)
   - [Deck Example](#example)
5. [Doctest](#doctest)
6. [Emulating Numeric Types](#emulating-numeric-types)
7. [String Representation](#string-representation)
   - [%r and !r](#r-and-r)
8. [Boolean Value of a Custom type](#boolean-value-of-a-custom-type)
9. [Collection ABC](#collection-abc)

# Fundamental Language Constructs

- Collections
- Attribute access
- Iteration (including asynchronous iteration using async for)
- Operator overloading
- Function and method invocation
- String representation and formatting
- Asynchronous programming using await
- Object creation and destruction
- Managed contexts using the with or async with statements

## Dunder Methods (Magic methods)

- Python invokes special methods called dunder methods to perform basic object operations
- Dunder - Double Underscore before and after
- Example: `obj[key]` is returned by the `__getitem__` special method
    - `my_collection[key]`, the interpreter calls `my_collection.__getitem__(key)`

## Special Methods Usage

- Special methods are meant to be called by interpreter, not manually
- Built-in types (`list`, `str`, `bytearray`) are **variable-sized C collections** with a ***PyVarObject*** struct
    - *PyVarObject* has an `ob_size` field storing number of items.
    - `len(obj)` reads `ob_size` field directly, which is faster than calling `obj.__len__()`
- **Iteration**: `for i in iterable:` → invokes `iter(iterable)` → uses `iterable.__iter__()` if available, or uses `iterable.__getitem__()`
- `__init__()` is the most commonly used special method, often called to initialize the superclass.

## Collections

- To construct a simple class that has attributes with no custom methods, like a database record, we can use ***collections.namedtuple***

```python
import collections

Card = collections.namedtuple(ClassName, [list of field names])
````

### Here Card can be created in 2 ways

```python
# Using namedtuple
Card = collections.namedtuple("Card", ["rank", "suit"])

# Using a normal class
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
```

1. **Using namedtuple**

   * **Immutable**: Once created, cannot change its field attributes
   * Fields are accessible by names or index
   * Very little memory overhead compared to normal class
   * Used for simple, fixed data structures
2. **Using normal class**

   * **Mutable**: Can change its field attributes
   * Flexible: Can add methods, validation, or computed properties
   * Slightly heavier than namedtuple
   * Used when behavior, methods, or mutability are required

### Example

```python
# deck.py
import collections

Card = collections.namedtuple("Card", ["rank", "suit"])

class Deck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = ["Spades", "Diamonds", "Clubs", "Hearts"]

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        """returns number of Card in a Deck"""
        return len(self._cards)

    def __getitem__(self, position):
        """return Card in the specified position in a deck"""
        return self._cards[position]

# len() and indexing([]) are not built-in for user-defined classes
# Only native sequences like list, tuple, str, set, etc., have them implemented internally
# automatically supports slicing, because of __getitem__
```

```python
from random import choice
from deck import Deck

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    """
    Give unique ranks to each card
    Cards with the same value get the same base value, with the suit value added to distinguish them
    """
    rank_value = Deck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

deck_of_cards = Deck()

print("\nSorted deck:")
for card in sorted(deck_of_cards, key=spades_high):
    print(card)

print(f"\nRandom card taken: {choice(deck_of_cards)}")
```

* Here, Deck cannot be shuffled because it is immutable, while shuffling requires in-place modification of elements.

## Doctest

* A module that allows writing examples in docstrings and then Python can test them automatically
* Running `doctest.testmod()` will check if the function’s output matches

```python
def add(a, b):
    """
    >>> add(2, 3)
    5
    """
    return a + b
```

### Ellipsis (…) in doctests

* Sometimes output is too long or variable; we cannot type all items in the doctest
* At such cases, ellipsis (…) is used to skip parts of the output

### # doctest: +ELLIPSIS directive

* Tell doctest to allow … in the expected output

```python
def numbers():
    """
    >>> numbers()  # doctest: +ELLIPSIS
    [0, 1, 2, ..., 97, 98, 99]
    """
    return list(range(100))
```

* Without `+ELLIPSIS`, doctest would fail because it expects the exact output.

## Emulating Numeric Types

* Making the Python class behave like built-in numeric types (int, float, complex, etc.) by implementing special methods such as:

  * `__add__`  : addition  `+`
  * `__mul__` : multiplication `*`, when object is on the left-hand side
  * `__rmul__` : multiplication `*`, when object is on the right-hand side
  * `__sub__` : subtraction
  * Similarly: `__floordiv__`, `__mod__`, `__pow__`, etc.

```python
import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector(x,y) where x={self.x} and y={self.y}"

    def __repr__(self):
        return f"Vector({self.x!r}, {self.y!r})"

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        x = self.x * scalar
        y = self.y * scalar
        return Vector(x, y)

    def __rmul__(self, scalar):
        x = scalar * self.x
        y = scalar * self.y
        return Vector(x, y)

    def __abs__(self):
        return math.hypot(self.x, self.y)

v1 = Vector(2, 4)
v2 = Vector(1, 3)

print(f"Addition: {v1 + v2}")
print(v1)
print(f"Multiplication: {v1*v2}")
print(repr(v1))
```

## String Representation

* `__str__` : Description of the object in human-readable format
* `__repr__`: Developer-oriented string of the object

### %r and !r

* `%r` → classic formatting, calls `repr()`
* `!r` → f-strings / str.format(), calls `repr()`

```python
name = 'Suriya'
print('Hello, %r!' % name)         # Hello, 'Suriya'!
print(f"Hello, {name!r}!")         # Hello, 'Suriya'!
print("Hello, {!r}!".format(name)) # Hello, 'Suriya'!
```

> Interactive console, debuggers, and `%r` / `!r` call `repr()` automatically.
> `__str__` is called by the `str()` built-in and implicitly by the `print` function.
> If `__repr__` is defined but `__str__` is not, then `__str__ = __repr__`.

## Boolean Value of a Custom type

* By default, `bool(obj)` calls `obj.__bool__()` → if not present then invokes `obj.__len__()`.
  If `__len__` returns 0, `bool` returns `False`. Otherwise `True`.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __bool__(self):
        return bool(self.x or self.y)
```

## Collection ABC

* Python collections are built around **abstract base classes (ABCs)** in `collections.abc`
* Top-level ABCs (Python 3.6+):

  * Collection → unifies `Iterable`, `Sized`, `Container`

    * Iterable → supports **for** loops, **unpacking**
    * Sized → supports **len()**
    * Container → supports **in**
* Specialized ABCs:

  * Sequence → list, str; reversible, ordered
  * Mapping → dict, defaultdict; key-value interface
  * Set → set, frozenset; supports infix operators like `&` (intersection)

> Python does not require explicit inheritance from ABCs; implementing the required special methods is sufficient. Python is **duck-typed**.
