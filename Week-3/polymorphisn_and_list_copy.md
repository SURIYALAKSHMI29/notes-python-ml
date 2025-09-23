
# Polymorphism, List Copy

## Table of Contents
- [Polymorphism](#polymorphism)
- [Encoding](#encoding)
- [Copy Lists](#copy-lists)

---

# Polymorphism

## Method Overriding (Runtime Polymorphism)

- Same interface, different implementations  
- Child class that inherited the base class overwrites the method present in base class  
- Based on the **object instance**, the corresponding method is executed  

```python
class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

a = Animal()
d = Dog()

for obj in (a, d):
    obj.sound()
# Output:
# Some sound
# Bark
````

---

## Operator Overloading (Compile-time Polymorphism)

* Based on the **operand type**, operator works differently
* Python uses **special methods** (`__add__`, `__sub__`, etc.) internally

### Built-in Example:

```python
print(3 + 5)              # addition
print("suriya " + "m")    # string concatenation
```

### Custom Class Example:

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

v1, v2 = Vector(1,2), Vector(3,4)
v3 = v1 + v2
print(v3.x, v3.y)  # 4 6
```

---

## Duck Typing (Runtime Polymorphism)

* Python is a **dynamically typed language**
* Duck typing = runtime polymorphism **without inheritance**
* It only checks if the object has that method at runtime; Based on the object, corresponding method is executed

```python
class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I can quack too!")

def make_it_quack(obj):
    obj.quack()

d = Duck()
p = Person()

make_it_quack(d)  # Quack!
make_it_quack(p)  # I can quack too!
```

**Purpose:** Functions can work with any object that has the required behavior, not just a fixed type → makes code **flexible and generic**

---

# Encoding

* Python stores text in **Unicode**, but files and network streams are **bytes**
* Types:

  * `str` → Unicode text
  * `bytes` → Binary data
* **Encoding:** `str → bytes`
* **Decoding:** `bytes → str`

```python
text.encode("utf-8")   # str → bytes

encoded.decode("utf-8")  # bytes → str
```

**Note:** Always specify encoding when handling files:

```python
with open("file.txt", "w", encoding="utf-8") as f:
    f.write("Hello 🌍")
```

---

# Copy Lists

## Assignment

* Using `=` operator
* Not a real copy → both variables point to the same list object
* Just a reference

```python
original = [1, 2, 3]
copy1 = original
copy1.append(4)
print(original)  # [1, 2, 3, 4] → original also affected
```

---

## Shallow Copy

* Creates a **new list object**, but elements are references to the same objects

### Methods:

1. **Using `list.copy()`**

```python
original = [1, 2, 3]
copy2 = original.copy()
copy2.append(4)
print(original)  # [1, 2, 3]
```

2. **Using slicing**

```python
copy3 = original[:]
```

3. **Using `list()` constructor**

```python
copy4 = list(original)
```

⚠️ **Caveat with nested lists:**

```python
original = [[1,2], [3,4]]
shallow = original.copy()
shallow[0].append(99)
print(original)  # [[1, 2, 99], [3, 4]] → inner list affected
```

---

## Deep Copy

* Recursively copies **all nested objects**
* Changes in the copy don’t affect the original

```python
import copy

original = [[1,2],[3,4]]
deep = copy.deepcopy(original)
deep[0].append(99)
print(original)  # [[1,2],[3,4]] → original stays safe
```

---
