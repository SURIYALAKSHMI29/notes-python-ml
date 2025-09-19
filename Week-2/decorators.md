# Table of Contents
- [Raise](#raise)
- [Decorators](#decorators)
  - [Property Decorator](#property-decorator)
  - [Setter](#setter)
  - [Example: Uppercase Decorator](#example-uppercase-decorator)
- [Property](#property)
  - [Decorators Using Property](#decorators-using-property)
  - [Usage](#usage)

# Raise

- Used to manually trigger an exception
- Stops the program unless caught in a try-except block
- Can be used in class constructors, for example, if user-given arguments need validation before creating the object

# Decorators

- Functions that modify the behavior of other functions or methods and modify or enhance it, returning a new function
- Prefixed with **@**

## Property Decorator

- **@property**: Turns a method into a **getter** for an attribute, allowing controlled access to the attribute.

## Setter

- **@<property>.setter**: Defines a method that is called whenever the property is assigned a value, allowing validation or preprocessing.
- Use case:
    - Encapsulation: protects the internal attributes from being modified directly
    - Validation: can perform validation before assigning, if invalid can raise Error
    - Clearer syntax; safe and maintainable

## Example: Uppercase Decorator

```python
def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper

@uppercase
def greet():
    return "hello"

print(greet())  # prints "HELLO"
````

* `@uppercase` transforms `greet` into `uppercase(greet)`
* `uppercase(greet)` returns `wrapper`
* In Python, the `@decorator_name` syntax is shorthand for:

```python
greet = uppercase(greet)
```

* Decorators **wrap a function** and can modify input/output or behavior.
* Decorators are executed at definition time

```python
def uppercase(func):
    return func().upper()  # calls func immediately
```

* Without a wrapper, `greet` becomes `"HELLO"` (a string), not a function
* By using a wrapper, `uppercase` returns a function, so `greet = wrapper` and `greet()` can be called

# Property

* A special kind of function that acts like an attribute
* Validates or computes attributes on access
* Provides controlled access to class attributes:

  * Getter - read the value
  * Setter - validate or modify before setting
* Allows encapsulation without changing how users access the attribute: `obj.name` instead of `obj.get_name()`
* **@property** is itself a decorator

## Decorators Using Property

```python
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

@property
def name(self):
    return self._name

@name.setter
def name(self, name):
    if not name:
        raise ValueError("Invalid name")
    self._name = name

@property
def house(self):
    return self._house

@house.setter
def house(self, house):
    if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
        raise ValueError("Invalid house")
    self._house = house
```

## Usage

* Naming convention: use `_attribute` (ex: `_house`) for the actual storage to indicate it should not be accessed directly
* Users interact with properties like regular attributes:

```python
student = Student("Harry", "Gryffindor")
print(student)          # Harry from Gryffindor
print(student.house)    # Calls getter
student.house = "Slytherin"  # Calls setter
```
