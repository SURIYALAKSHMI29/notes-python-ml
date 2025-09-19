# Table of Contents
- [Return Values](#return-values)
- [Class](#class)
  - [Namespace](#namespace)
  - [Instantiation](#instantiation)
  - [Attributes](#attributes)
  - [Classes as Instances of type](#classes-as-instances-of-type)
  - [Adding Methods to a Class at Runtime](#adding-methods-to-a-class-at-runtime)
  - [Descriptors](#descriptors)
  - [Attribute Lookup Order](#attribute-lookup-order)
  - [Method Binding](#method-binding)
  - [Slots](#slots)
  - [Dunder/Magic Methods](#dundermagic-methods)

# Return Values

- As tuples:
    - `return (a, b)`
    - Immutable: once returned, the values cannot be changed directly
    - Useful for: safe, defensive coding when we don’t want the caller to accidentally modify the values
- As list:
    - `return [a, b]`
    - Mutable: values can be modified after being returned
    - Useful when: we want the calling function to update the returned data
- As Dictionary:
    - `return { "name": name, "house": house }`
    - Indexed by keys, not positions
    - Values can be modified
    - Useful when: returning structured data with meaningful keys, easy to access

# Class

- Way of bundling data and functionality together, creating new object types
- In Python, classes are not just blueprints for creating objects; they are themselves objects - instances of the metaclass `type`.
- Class Definition:
    
    ```python
    class ClassName:
        <statement>
    ```
    
- This creates a new **namespace**, and the class object is bound to `ClassName`
    - Calls the metaclass (by default `type`) with `(name, base, dict)` to create a class object
    - Binds that class object to the name after `class` in the surrounding scope

## Namespace

- Mapping between names and objects in Python
- A container that keeps track of all identifiers (variables, functions, classes, etc.) and what they refer to in memory

### Different Types of Namespaces

1. **Built-in namespace:** contains all built-in names like `len`, `print`, `int`, etc
2. **Global namespace:** Created for each file/module, contains all the names (variables, functions, classes) defined outside any function/class
3. **Local namespace:** Created when a function is called
4. **Class namespace:** Created when we define a class (also attribute and method names)

## Instantiation

```python
obj_name = ClassName()
````

* Internally calls **`type.__call__`** which executes:

  * **`__new__`**: allocates memory and returns a new empty instance
  * **`__init__`**: initializes the instance with the data specified
  * Returns a fully prepared object

## Attributes

* **Class attributes:** stored in `ClassName.__dict__`, shared by all instances

* **Instance attributes:** unique to each object; defined in `__init__` with `self`

* **Private and Protected Attributes:**

  * `_attr` → protected; signaling convention, not enforced
  * `__attr` → private; triggers *name mangling*: `_ClassName__attr`

* **Accessing attributes or methods:** `a.greet()` calls `a.__getattribute__('greet')`

* **Setting attributes:** `a.var1 = 42` calls `a.__setattr__('var1', 42)`

## Classes as Instances of type

### type()

1. `type(object)` → returns the type of the object
2. `type(name, bases, namespace)` → creates a new class dynamically

   * `name`: string representing the new class name
   * `bases`: tuple of base classes to inherit from
   * `namespace`: dict defining attributes and methods

```python
MyClass = type('MyClass', (object,), {'x': 5})
```

## Adding Methods to a Class at Runtime

```python
def greet(self):
    return f"Hello from {self.__class__.__name__}!"

# Add dynamically
setattr(MyClass, 'greet', greet)
# or
MyClass.greet = greet
```

## Descriptors

* Objects implementing at least one of:

  * `__get__(self, instance, owner)`
  * `__set__(self, instance, value)`
  * `__delete__(self, instance)`
* **Data descriptor:** has `__set__` or `__delete__` → takes precedence over instance attributes
* **Non-data descriptor:** only `__get__` → checked after instance attributes

## Attribute Lookup Order

1. Check `obj.__class__.__dict__` for **data descriptors**
2. Check `obj.__dict__` (instance attributes)
3. Check `obj.__class__.__dict__` for **non-data descriptors** or plain values
4. Follow MRO (Method Resolution Order) from most derived to base classes
5. If nothing found → `AttributeError`

## Method Binding

* Function in a class is a descriptor
* Calling a method on an instance returns a bound method

```python
class X:
    def greet(self):
        return f"hello {self}"

x = X()
m = x.greet  # bound method
print(m.__self__ is x)  # True
print(m.__func__ is X.greet)  # True
```

* Accessing `a.greet()` calls `a.__getattribute__('greet')`
* Setting `a.var1 = 42` calls `a.__setattr__('var1', 42)`

## Slots

* Restrict which attributes an instance can have using `__slots__`
* Saves memory by avoiding `__dict__` for each instance

```python
class X:
    __slots__ = ['a', 'b']

x = X()
x.var3 = 2  # Error
```

## Dunder/Magic Methods

* Special methods with double underscores, e.g., `__str__`, `__add__`
* Customize Python behavior

Examples:

* `__str__` → user-friendly string representation
* `__repr__` → developer-friendly representation
* `__add__` → `+` operator
* `__len__` → `len(obj)`
* `__getitem__` → `obj[key]`

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"A circle with radius {self.radius}"
    
    def __repr__(self):
        return "Circle"

circle = Circle(5)
print(circle)  # calls __str__
circle         # calls __repr__
``` 

If you want, I can also **add a smaller TOC at the top of each subsection**, so clicking it jumps to sub-subsections like descriptors, slots, etc., for faster navigation. Do you want me to do that?
```
