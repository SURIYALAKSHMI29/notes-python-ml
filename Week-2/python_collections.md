# Python Data Structures

## Table of Contents
- [List](#list)
- [Tuple](#tuple)
- [Set](#set)
- [Dictionary](#dictionary)

---

## List:

- **Mutable non-homogeneous ordered** data structure
- Elements can be stored in columns of a single-row or multiple rows
- Iterable and it uses square brackets [ ]
- **list()** function is used to create a list
    
```python
list_1 = ["suriya", 29, True, False, True]

# using list() constructor
list_2 = list((1, 2, 30, 13))

# To access
print(list_1[1])  # print 29

# Common methods
list_1.append(99.98)  # Add at end
list_1.insert(1, "new")  # Insert at specified index
list_1.remove(True)  # Remove first occurrence
list_1.pop()  # Remove last element
list_1.reverse()  # Reverse order
print(len(list_1))  # Length of list

# sorts works only if all elements are of same type
list_2.sort()  # sorts in ascending order
list_2.sort(reverse=True)  # sorts in descending order
````

---

## Tuple:

* **Immutable non-homogeneous ordered** data structure
* Elements can be stored in columns of a single-row or multiple rows
* Uses open brackets ( )
* **tuple()** is used to create tuples

```python
tuple_1 = ("suriya", 29, True, False, True)

# using tuple() constructor
tuple_2 = tuple((1, 2, 30, 13))

# To access
print(tuple_1[-2])  # print False

# Common Methods
print(tuple_1.count(True))  # Count occurrences
print(tuple_1.index(29))  # Find index of first match
print(len(tuple_1))  # Length of tuple
```

---

## Set:

* **Mutable non-homogeneous unordered** data structure
* Stores unique elements in a single row
* Uses curly brackets { }
* **set()** function is used to create sets

```python
set_1 = {"suriya", 29, True, False, True}
# duplicate values will be removed (i.e) here True is duplicate

set_2 = set((1, 2, 30, 13))  # using set() constructor

# To access - sets are unordered and do not support indexing
for item in set_1:
    print(item)  # order not guaranteed

# Common methods
set_1.add(99.98)  # Add element
set_1.remove(True)  # Remove element, raises KeyError if not found
set_1.discard(100)  # Remove element if found, does not raise error
set_1.pop()  # Remove and return an arbitrary element
set_1.update([1, 2, 3])  # Add multiple elements from iterable
print(len(set_1))  # Length of set

# Set Operations
A = {"suriya", "raji", "karthiga"}
B = {"suriya", "arav", "sahira"}

print(A.union(B))  # Elements in A or B or both
print(A.intersection(B))  # Elements in both A and B
print(A.difference(B))  # Elements in A but not in B
print(A.symmetric_difference(B))  # Elements in A or B but not both
```

---

## Dictionary:

* **Mutable non-homogeneous data structure** that **stores key-value pairs**
* Uses curly braces { }
* Doesn’t allow duplicate keys
* **dict()** function is used to create a dictionary

```python
dict_1 = {"name": "arav", "age": 3, "city": "madurai"}

# using dict() constructor
dict_2 = dict(name="sahira", age=1)  # here keys are not in quotes

# To access
# used when we are sure key exists, otherwise raises KeyError
print(dict_1["name"])  # print arav

# used when we are not sure if key exists, returns None if not found or default value provided
print(dict_2.get("age"))  # print 1
print(dict_2.get("city", "not found"))  # returns "not found"

# Common methods
dict_1["country"] = "India"  # Update value if key exists, else adds new key-value pair
dict_2.update({"city": "madurai", "age": 2})  # Update multiple pairs
print(len(dict_2))  # Length of dictionary

# Iteration
for key, value in dict_1.items():
    print(key, value)

for key in dict_2.keys():  # print only keys
    print(key)

for value in dict_2.values():  # print only values
    print(value)

# Keys, values, items
print(dict_2.keys())    # dict_keys(['name', 'age', 'city'])
print(dict_2.values())  # dict_values(['sahira', 2, 'madurai'])
print(dict_2.items())   # dict_items([('name', 'sahira'), ('age', 2), ('city', 'madurai')])
```

---

