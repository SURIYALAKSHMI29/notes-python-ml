# Table of Contents
- [Return values](#return-values)
- [Class](#class)
  - [Namespace](#namespace)
  - [Instantiation](#instantiation)
  - [Attributes](#attributes)
  - [Classes as Instances of type](#classes-as-instances-of-type)
  - [Adding Methods to a Class at Runtime](#adding-methods-to-a-class-at-runtime)
  - [Descriptors](#descriptors)
  - [Attribute lookup order](#attribute-lookup-order)
  - [Method Binding](#method-binding)
  - [Slots](#slots)
  - [Dunder/Magic Methods](#dundermagic-methods)
 
# Return values

- As tuples:
    - return (a, b)
    - Immutable: once returned, the values cannot be changed directly
    - Useful for: safe, defensive coding when we don’t want the caller to accidentally modify the values
- As list:
    - return [a, b]
    - Mutable: values can be modified after being returned.
    - Useful when: we want the calling function to update the returned data
- As Dictionary:
    - return { “name”: name, “house”: house}
    - Indexed by keys, not positions
    - Values can be modified
    - Useful when: returning structured data with meaningful keys, easy to access

# Class

- Way of bundling data and functionality together, creating new object types
- In Python, classes are not just blueprints for creating objects; they are themselves objects - instances of the metaclass type.
- Class Definition:
    
    ```python
    class ClassName:
    	<statement>
    ```
    
- This creates a new **namespace,** and the class object is bound to *ClassName*
    - Calls the metaclass (by default *type*) with *(name, base, namespace)* to create a class object.
    - Binds that class object to the name after ***class***  in the surrounding scope.

## Namespace:

- Mapping between names and objects in python;
- A container that keeps track of all identifiers(variables, functions, classes,..) and what they refer to in memory

### Different Types of Namespaces

1. **Built-in namespace:** contains all built-in names like len, print, int, etc
2. **Global namespace:** Created for each file/module, contains all the names (variables, functions, classes) defined outside any function/class
3. **Local namespace:** Created when a function is called
4. **Class namespace:** Created when we define a class (also attr and methods names)

## Instantiation:

```python
obj_name = ClassName()
```

Here Class_name() internally calls **`type__call__`** which does

- **`__new__`**
    - Allocates memory and returns a new empty instance of **ClassName**
- **`__init__`**
    - Takes that raw instance and initializes it with the data specified in class constructor call
- Returns a fully prepared object

## Attributes

- **Class attributes** are get stored in ClassName.`__dict__`  and it is shared by all instances of the class
- **Instance attributes** are ****unique to each object; defined in `__init__` with self
- **Private and Protected Attributed:**
    - **_attr**
        - protected; python doesn’t prevent access; it’s just a signal to other developers
    - **__attr**
        - private , to avoid accidental access
        - Double underscores triggers *name mangling;* python internally renames the variable to *_*ClassName*__var*
- **Accessing an attribute or method** (a.greet()) → calls a.`__getattribute__`('greet') → normal lookup → if not found, `__getattr__` is called.
- **Setting an attribute** (a.var1 = 42) → calls a.`__setattr__`('var1', 42) → use object.`__setattr__`(self, ‘var1’, 42) inside to actually store the value.

## Classes as Instances of type

### type():

1. *type(object)* - returns the type of the given object
2. *type(name, base, namespace)* - creates a new class dynamically.
    - name : A string representing the name of the new class.
    - bases : A tuple containing the base classes from which the new class will inherit.
    - *namespace* : A dictionary defining the attributes and methods of the new class.
    
    **Example:**
    
    ```python
    MyClass = type('MyClass', (object,), {'x': 5})
    ```
    
    - ‘MyClass’ : The name of the new class.
    - (object,): A tuple with a single element, indicating that MyClass inherits from the base class object
    - {'x': 5}: A dictionary defining an attribute x with the value 5 for instances of MyClass.

## Adding Methods to a Class at Runtime

Since classes are objects, methods can be added by using *setattr()*

```python
def greet(self):
    return f"Hello from {self.__class__.__name__}!"

**# setattr(MyClass, 'method_name', method_function)**
setattr(MyClass, 'greet', greet)

# or
MyClass.greet = greet
```

This adds a *greet()* method to *MyClass*. 

**Using *setattr()* is advantageous when:**

- The method name is determined dynamically at runtime.
- You need to add methods to classes that you don't have direct access to modify.

## Descriptors

- A descriptor is any object with at least one of these methods:
    - **`__**get**__`**(self, instance, owner)
    - **`__**set**__`**(self, instance, value)
    - **`__**delete**__`**(self, instance)
- Function in a class is a descriptor as it has a `__get__` method
- A descriptor is just an object that controls **attribute access**

Two types:

- **Data descriptor** (has `__set__`  or  `__delete__`) → takes precedence over instance attributes.
- **Non-data descriptor** (only `__get__`) → checked after instance attributes.

Python data descriptor → controls how attributes are accessed/modified, dynamic.

Java private → controls who can access, static visibility only.

### Attribute lookup order

1. **Check obj.`__class__`.`__dict__`**
    - If there’s a data descriptor (`__get__` + `__set__` / `__delete__`)
        - immediately use it (skips obj.__dict__)
2. **Check obj.`__dict__` (instance attributes)**
    - If found → return it.
3. **Check obj.`__class__`.`__dict__` again**
    - If it’s a **non-data descriptor** (`__get__` only) → call its `__get__`.
    - If it’s a plain value (non-descriptor) → return it
4. Follow MRO(Model Resolution Order) with same rules
    - MRO - bottom to top; most derived(cls of the obj) to the base class(ancestors)
5. If still nothing → *AttributeError*

### Method Binding

- Function in a class is a descriptor
- When instance of a class, calls a method it internally executes
    - *ClassName.method_name.`__get__`(instance, ClassName)* - returns a bound method
    - Bound method:  remembers the instance
        - *`__self__`* → the instance (instance)
        - *`__func__`* → the original function (ClassName.method_name)
- Class access - access a method directly by using its’ ClassName returns a raw function; Not bound to any instance

```python
class X:
	def greet(self):
		return f"hello {self}"
		
x = X()
m = x.greet     # returns bounded function

print(type(m))       # <class 'method'>
print(m.__self__ is x)  # True

**# m.__func__ - points to the orginal function**
**# m.__self__ - points to the instance**
```

## Slots

- By defining **__slots__**, we can restrict which attributes an instance can have
- Attributes not in `__slots__` cannot be added
- Saves memory by avoiding `__dict__` of each class

```python
class X:
**slots** = ['a', 'b']  # only 'a' and 'b' allowed

x = X()
x.var3 = 2   # throws an error
```

## Dunder/Magic Methods:

- Special methods with double underscores at the start and end(eg: `__str__`, `__add__`) and allows to customize how python behaves with your objects
1. `__str__` → defines what is shown to a user when you print an object
2. `__repr__` → defines a developer-friendly representation, often used in debugging
3. `__add__` → defines behavior for + operator 
4. `__len__` → called by len(obj)
5. `__getitem__` → called by obj[key]

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"A circle with radius {self.radius}"
    
    def __repr__(self):
		    return "Circle"
 
circle = Circle(5)
print(circle)     **# python internally calls circle.__str__()** 
# prints 'A circle with radius 5'

circle       # python calls circle.__repr__() in console
# prints "Circle"

# p1 + p2 -> calls p1.__add__(p2)

```
