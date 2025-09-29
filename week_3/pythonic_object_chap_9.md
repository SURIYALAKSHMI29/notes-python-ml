# Fluent Python - Chapter 9

## Table of Contents
1. [Object Representations](#object-representations)
2. [Class Method](#class-method)
3. [Static Method](#static-method)
4. [Formatting](#formatting)
5. [Private Variable](#private-variable)  
   - [Name Mangling](#name-mangling)  
   - [@property Decorator](#property-decorator)  
6. [Positional Matching](#positional-matching)
7. [__slots__](#__slots__)

---

## Object Representations

- `repr()` - developer friendly; unambiguous
- `str()` - user friendly
- `bytes()` - analogous to `__str__`; calls `__bytes__` to get object represented in byte sequence
- `format()` - used by f-strings, by built-in function `format()` → displays the objects using special formatting codes

> - `__bytes__` → return a byte sequence  
> - `__repr__`, `__str__`, `__format__` → return Unicode strings (type `str`)

---

## Class Method

- Method that belongs to the class, can be called directly on class without creating instances
- Takes class as the first argument
- It can modify the class state that would apply across all the instances of the class. For ex, modifying the class variable that will be applicable to all the instances
- **UseCase:** Used as alternative constructors

```python
@classmethod
def frombytes(cls, octets):
    typecode = chr(octets[0])
    memv = memoryview(octets[1:]).cast(typecode)
    return cls(*memv)   # calls the org constructor here
````

---

## Static Method

* A plain function inside the class, just grouped together based on common functionality
* Encapsulation
* Doesn’t take class argument; bound to a class and not the object of the class
* Can’t access or modify the class state

```python
class Demo:
    @classmethod
    def clsmeth(*args):
        return args     # (<class '__main__.Demo'>,)

    @staticmethod
    def statmeth(*args):
        return args     # ()
```

---

## Formatting

* `format(obj, fmt_spec)` → calls `obj.__format__(fmt_spec)`

```python
format(42, "b")   # '101010' (binary)
```

* **F-strings**

  * Translates into `format()`
  * Can even have math operations, conditions, functions in the placeholder

---

## Private Variable

* No “Private” instance variable in Python
* Convention: name prefixed with `_` indicates non-public part of the code
* Can combine **name mangling** and **@property decorator**

### Name Mangling

* By using exactly two leading underscores (with zero or one trailing underscore), the attribute becomes `_classname__varname`
* **It is about safety, not security**
* This allows the sub-classes to override the methods without breaking intraclass method calls

```python
class Vector:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

v1 = Vector(2, 4)
print(v1.x)          # throws AttributeError
print(v1._Vector__x) # 2
```

### @property Decorator

* Defining a property makes the attribute read-only

```python
class Vector:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

v1 = Vector(2, 4)
print(v1.x)           # 2
print(v1._Vector__x)  # 2

v1.x = 4  # throws AttributeError
```

> By this way, variables can be used as private.
> To change them, we can implement `@x.setter`.

---

## Positional Matching

* Python needs to know which attributes correspond to each position
* Using `__match_args__`, it defines the order of attributes

```python
class Vector:
    __match_args__ = ('x', 'y')

# Now we can match as,
match v:
    case Vector(_, 0):
        # code...
```

---

## **slots**

* Holds a sequence of attribute names → stored in a hidden array of references (less memory than a dict)
* Static type method; no dynamic `__dict__`
* Trying to set an attribute not listed in `__slots__` raises `AttributeError`
* `__slots__` of superclasses are added to subclass unless subclass defines its own
* Memory and time efficient
* Classes using `__slots__` cannot use the `@cached_property` decorator, unless `__dict__` is explicitly named in `__slots__`

```python
class Vector2d:
    __slots__ = ('x', 'y')  # only these attributes allowed
    def __init__(self, x, y):
        self.x = x
        self.y = y

v = Vector2d(3, 4)
v.z = 3  # throws AttributeError
```

> `__slots__ = ('x', 'y')`
> positions → `x` at 0, `y` at 1

```

