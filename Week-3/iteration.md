## Table of Contents

1. [Global Variables](#global-variables)
2. [Constant](#constant)
3. [Sphinx](#sphinx)
4. [Unpacking](#unpacking)
5. [Args and Kwargs](#args-and-kwargs)
6. [Map](#map)
7. [Filter](#filter)
8. [List Comprehensions](#list-comprehensions)
9. [Dictionary Comprehensions](#dictionary-comprehensions)
10. [Enumerate](#enumerate)
11. [Iterator](#iterator)
12. [Generator](#generator)

---

## Global Variables

- A variable defined outside of any function or class; Can be accessed anywhere in the program
- To interact with a global variable inside a function, **global** keyword is used

```python
balance = 0

def main():
	print("Balance:", balance)      # prints 0
	deposit(100)
	print("Balance:", balance)      # prints 100
	
def deposit(n):
	global balance      **# using global keyword to access it**
	balance += n

main()
````

* **Alternative: Using Class**

  * Define the balance variable as property and access it as an attribute from other functions

```python
class Account:
	def **init**(self):
		self._balance = 0
		
@property
def balance(self):
    return self._balance

def deposit(self, n):
    self._balance += n
```

---

## Constant

* Constants are denoted by capital variable names and are placed at the top of the code
* Python don’t provide any feature such that it will throw an error if it is changed, just it is a signal to others that it is a constant don’t change it

---

## Sphinx

* a documentation generator for python projects
* It takes *docstrings* and additional documentation files(.rst .md) and automatically builds output in multiple formats, such as HTML pages, pdf files, and other formats (as required)

---

## Unpacking

* Unpacking a List / Tuple:

  * Allows assigning elements of a list/tuple to variables directly
  * Using \* (star operator)

```python
def add(a, b, c):
	return a + b + c
	
numbers = [1, 2, 3]
print(add(*numbers))   # 6
```

* Unpacking a Dictionary:

  * By default, unpacking a dictionary gives keys

```python
student = {"name": "Suriya", "age": 20}
a, b = student
print(a, b)   # name age
```

```
- To get values alone, **.values()** can be used
- To get as key-value pairs, **.items()**
- Can use ** operator
    
```

```python
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old")
    
student = {"name": "Suriya", "age": 20}
introduce(**student)
```

---

## Args and Kwargs

* \***args** → collects any number of positional arguments into a tuple.
* \*\***kwargs** → collects any number of keyword arguments into a dictionary.

```python
def f(*args, **kwargs):
	print("Positional:", args)
	
f(100, 50, 25)
```

Even though the function definition *looks like it has two parameters* (\*args, \*\*kwargs), they’re special catch-all containers.

* If we give only positional → they all go into args.
* If we give only keyword → they all go into kwargs.
* If we give both → Python distributes them accordingly.

---

## map

* built-in function that applies another function to every item in an iterable (like list, tuple, set)
* returns a map object, which can be converted into a list, tuple, etc
* **Syntax:**

```python
map(function, iterable)
```

* **function** → A function to apply
* **iterable** → sequence of items
* If multiple iterables passed together,map() will take one element from each at a time

  * Iteration stops at the shortest variable

```python
a = [1, 2, 3, 4]
b = [4, 5, 6]
result = map(lambda x, y: x + y, a, b)
print(list(result))   # [5, 7, 9]
```

---

## filter

* allows to return a subset of a sequence of which a certain condition is true
* **Syntax**:

```python
filter(function, iterable)
```

* **function**:  returns True (keep the item) or False (discard the item).
* **iterable**:  sequence of items

---

## List Comprehensions

* creating a list using a single line of code
* **Syntax**

```python
[expression for item in iterable if condition]

# expression - item we need to append in the list
# for item in iterable - loop through the list
# if condition - filter items
```

**example:**

```python
**# converting celsius to fahrenheit**
temps_c = [0, 10, 20, 30, 40]

**# using list comprehension**
def convert(celsius):
    return celsius * 9 / 5 + 32

temp_f = [convert(c) for c in temps_c]
print(temp_f)

**# using map**
temp_f = list(map(convert, temps_c))
print("Using map, ", temp_f)

**# using lambda + map**
temp_f = list(map(lambda c: c * 9 / 5 + 32, temps_c))
print("Using map and lambda", temp_f)

**# Select only elements greater than 10**
numbers = [5, 12, 7, 20, 33, 8, 15]

**# using list comprehension**
greater_than_10 = [num for num in numbers if num > 10]
print(greater_than_10)

**# using filter**
greater_than_10 = list(filter(lambda num: num > 10, numbers))
print("Using filter", greater_than_10)
```

---

## Dictionary Comprehensions

* **Syntax**

```python
{key_expression: value_expression for item in iterable if condition}
```

* Example:

```python
numbers = [1, 2, 3, 4, 5, 6]
even_squares = {x: x**2 for x in numbers if x % 2 == 0}
print(even_squares)     # {2:4, 4:16, 6:36}
```

---

## enumerate

* adds a counter to an iterable (like a list, tuple or string) and returns it as an enumerate object
* Use case: when we need both index and a value
* **Syntax:**

```python
enumerate(iterable, start=0)

iterable → any iterable (list, tuple,..)
start → the starting index (By default: 0)
```

* **Example**:

```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits, start=1):
		print(index, fruit)
```

---

## Iterator

* Iterator is like a pointer used to access elements one by one
* implements *`__iter__()`* and *`__next__()`* methods
* Keeps track of the current state (position) internally
* When there are no more items to return, *StopIteration* (exception) is raised, used to signal that the iteration is complete

```python
numbers = [1, 2, 3]
it = iter(numbers)     

**# it - iterator object, pointing to first element of the iterable
# next(it) -> prints the current element and moves onto the next position**

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
print(next(it))  # StopIteration raises
```

---

## Generator

* Lazy iterators, produce the values only when needed, instead of computing and storing everything in memory at once

  * **Memory efficient -** Computes one item at a time, so it used very little memory
  * **Time efficient -** Values are produced on-the-fly, so we can start processing the first items immediately without waiting for the entire collection to be computed
* During compilation, Python sees the *yield* and marks the function as a generator function, so calling the function doesn’t execute the code immediately

### yield

* yield pauses the function and returns a value to the caller
* When *next()* is called, the function resumes right after the last *yield,* keeping its internal state intact

```python
def squares(n):
	for i in range(n):
		print(i)      **# doesn't get printed until next(gen) is called**
		yield i ** 2 

gen = squares(5)   **# gen - generator object**
print(next(gen))  # 0  
print(next(gen))  # 1 
print(next(gen))  # 4
```

### **NOTE:**

* **map()** → transforms each item in a collection using a function
* **filter()** → selects only those items that satisfy a condition
* In list comprehension, \[ ] square brackets are used, whereas in dict comprehension {} curly braces are used
* *map()* returns a **map object** whereas *list comprehension* returns a **list** directly
* Iterators and Generators raise *StopIteration,* but caught internally by *for loop* , so the loop ends normally without throwing an error
