# Fluent Python - Chapter 3

# Table of Contents
1. [Dictionaries](#dictionaries)
2. [Dict Comprehensions](#dict-comprehensions)
3. [Unpacking Mappings](#unpacking-mappings)
4. [Merging Dicts](#merging-dicts)
5. [Pattern matching (Python 3.10)](#pattern-matching-python-310)
6. [Hashable](#hashable)
7. [Mapping Types Overview](#mapping-types-overview)
8. [Inserting / Updating Values](#inserting--updating-values)
9. [Automatic Handling of Missing Keys](#automatic-handling-of-missing-keys)
10. [`__missing__` Support](#missing-support)
11. [Variations of dict](#variations-of-dict)
    - [OrderedDict](#ordereddict)
    - [ChainMap](#chainmap)
    - [Counter](#counter)
    - [shelve.Shelf](#shelveshelf)
    - [UserDict](#userdict)
    - [Immutable Mappings](#immutable-mappings)
    - [Dictionary Views](#dictionary-views)
    - [Key-Sharing Dicts (PEP 412)](#key-sharing-dicts-pep-412)
12. [Sets](#sets)
    - [Types](#types)
    - [Dictionary Views as Sets](#dictionary-views-as-sets)

---

# Dictionaries

- Python programs use dictionaries everywhere, `__builtins__.__dict__` stores all built-in types, objects, and functions
- Dictionaries (dict) are highly optimized using hash tables
- Sets(set, frozenset) are also hash-based, supporting a set theory operations like union, intersection, subsets, etc

## Dict Comprehensions

- Similar to list comprehensions but produce dictionaries.
- Example:
    
    ```python
    dial_codes = [(880,'Bangladesh'), (55,'Brazil'), (86,'China')]
    country_dial = {country: code for code, country in dial_codes}
    ```
    
- Can include sorting, filtering, transforming values:

```python
dial_codes_lt_70 = {
    code: country.upper() for country, code in sorted(country_dial.items()) 
    if code < 70
}

# {55: 'BRAZIL'}
````

## Unpacking Mappings

* ** allows unpacking dicts in function calls or literals
* *This works when keys are all strings and unique across all arguments*
* Example:

```python
def dump(**kwargs): 
	return kwargs

dump({'a':0, **{'x':1}, 'y':2, **{'z':3,'x':4}})  # {'a':0,'x':4,'y':2,'z':3}

# NOTE:  'x' is repeated twice 
# Later keys overwrite earlier keys in a literal.
```

## Merging Dicts

* **With | →** creates new dict
* **With |= →** Updates the dict in place

## Pattern matching (Python 3.10)

* can match dict-like structures
* Supports partial-matches (extra keys in dict are ignored unless captured)
* When we match dicts using *match/case*. missing keys are not created - they must exist for a match to succeed.

```python
def get_creators(record: dict) -> list:
    match record:
        case {'type': 'book', 'api': 2, 'authors': [*names]}:
            return names
        case {'type': 'book', 'api': 1, 'author': name}:
            return [name]
        case {'type': 'book'}:
            raise ValueError(f"Invalid 'book' record: {record!r}")
        case _:
            raise ValueError(f'Invalid record: {record!r}')
```

## Hashable

* An object is hashable if:

  1. It has a hash code that never changes during its lifetime (**hash** method).
  2. It can be compared to other objects (**eq** method).
  3. Objects that compare equal must have the same hash code.
* **Example**

  * **Hashable**: numbers, str. bytes. immutable containers(frozenset, tuple)
  * **Not hashable**: mutable containers(lists, dicts)
  * *Dict keys must be hashable, but dict is no hashable*

# Mapping Types Overview

Mappings are objects like dict, defaultdict, and OrderedDict

### Common Methods

* d.clear(): remove all items.
* d.**contains**(k): k in d.
* d.copy(): shallow copy.
* d.get(k, [default]): safe retrieval with fallback.
* d.items(), d.keys(), d.values(): views.
* d.**getitem**(k) / d.**setitem**(k, v): access/assign.
* d.pop(k, [default]), d.popitem(): removal.
* d.update(m, **kwargs): merge data.
* d.setdefault(k, [default]): return value at k or set to default if missing.
* d.**or**, d.**ior**: dict merge/update (|, |=) from Python ≥ 3.9.
* **OrderedDict adds move_to_end() and FIFO/LIFO behavior in popitem()**
* **defaultdict adds default_factory (callable to create missing values)**

# Inserting / Updating Values

* Using **dict.get** requires multiple lookups when updating mutable values.

  * Need to find the value of the key
  * Append new value to the key
  * Modify the value for the key in dict
* **setdefault** optimizes this by handling missing keys in a **single lookup**.

  ```python
  index.setdefault(word, []).append(location)
  ```

  is equivalent to:

  ```python
  if word not in index:
      index[word] = []
  index[word].append(location)
  ```

# Automatic Handling of Missing Keys

**Two approaches:**

1. **defaultdict**:

   * Provide a **default_factory**.

   * On missing key: calls factory → inserts value → returns it.

   * Example:

     ```python
     dd = defaultdict(list)
     dd["new"]  # → []
     ```

   * **Note**: default_factory is only used for ***getitem***, not for *.get()* or *in*
2. ****missing** method:**

   * Not in base dict, but recognized by *dict.**getitem**()* (if needed, we can implement **missing**)
   * Can be defined in subclasses to customize behavior for missing keys

# **missing** Support

Behavior differs depending on how we subclass:

1. dict subclass: ***missing*** used only for d[k].
2. UserDict subclass: ***missing*** used for d[k] and d.get(k)
3. abc.Mapping subclass (plain ***getitem***): ***missing*** not used.
4. abc.Mapping subclass (***getitem*** calls ***missing***): applies for d[k], d.get(k), and k in d.

# Variations of dict

### OrderedDict

* Keeps keys in insertion order (before python 3.6 dict did not preserve the insertion order of keys)
* Differences from regular dict:

  * Equality (==) checks order too.
  * popitem() can specify which end to pop.
  * move_to_end() moves an element efficiently.

```python
from collections import OrderedDict

od1 = OrderedDict(name="suriya", age=20)
od2 = OrderedDict(age=20, name="suriya")

print(od1 == od2)  # False, because order of keys is different

print(od2.popitem(last=False))  # pops first item
# ("age", 20)

od1.move_to_end("name")
print(od1)  # OrderedDict({'age': 20, 'name': 'suriya'})
```

* Optimized for frequent reordering (good for LRU caches)

### ChainMap

* Encapsulates many dictionaries into one unit. ChainMap is member of module “collections”
* **Access Operations:**

  * **keys()** → display all keys
  * **values()** → displays all values
  * **maps()** → displays all key-value pairs
* **Manipulating Operations**

  * **new_child() -** adds a new dictionary in the beginning
  * **reversed() -** reverses the relative ordering of dictionaries
* Updates affect only the first mapping

```python
from collections import ChainMap

dic1 = {"a": 1, "b": 2}
dic2 = {"b": 3, "c": 4}

chain = ChainMap(dic1, dic2)

print(chain.values())  # ValuesView(ChainMap({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
# returns dynamic, iterable view
# needs to iterate over it or convert to list to prints its values

print(list(chain.keys()))  # ['b', 'c', 'a']
print(chain.maps)  # [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}]

dic3 = {"d": 6, "e": 7}

print(chain.new_child(dic3))  # adds a new dict in the beginning
# ChainMap({'d': 6, 'e': 7}, {'a': 1, 'b': 2}, {'b': 3, 'c': 4})

print(chain["b"])  # 2

chain.maps = reversed(chain.maps)  # reverses teh dict order
print(chain["b"])  # 3
```

### Counter

* Holds integer counts for keys (like a multiset).
* Updating an existing key adds to its count.
* Useful methods: most_common(n), arithmetic operations (+, - ).
* Example:

  ```python
  ct = collections.Counter('abracadabra')
  print(ct) # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

  ct.update('aaaaazzz')
  print(ct) # Counter({'a': 10, 'z': 3, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

  ct.most_common(3) # [('a', 10), ('z', 3), ('b', 2)]
  ```

### shelve.Shelf

* Persistent key-value storage using string keys and pickled Python objects

  * **Pickling**: Converting a Python object (like a dict, list, or custom object) into a byte stream so it can be saved to a file or sent over a network.
  * **Unpickling**: Converting the byte stream back into the original Python object.
* Provides I/O methods like sunc() and close()

### UserDict

* Wrapper around a regular dictionary (self.data)

  * self.data → normal python dictionary; All key-value pairs are actually stored in *self.data*
* Used to create custom dictionaries with modified or new functionality.
* Easier and safer to subclass than *dict* (avoids recursion/unexpected behavior).
* Internal *dict* handles hashing and key lookups.
* Methods are easy to override.

### Immutable Mappings

* *MappingProxyType* wraps a dict to provide a **read-only but dynamic view**.
* Updates to the original dict are reflected in the proxy, but proxy itself cannot be modified.

### Dictionary Views

* *.keys(), .values(), .items()* return dynamic, read-only views (*dict_keys, dict_values, dict_items*).
* Avoid memory overhead of copying data.
* Views are iterable, implement len(), and reflect changes in the original dict

### Key-Sharing Dicts (PEP 412)

* Instances store attributes in **dict** (name → value).
* Python 3.3+ **shares keys structure** among instances of the same class.
* Each instance keeps **only its values**

```python
class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

p1 = Point(1, 2)
p2 = Point(3, 4)
```

**Key-sharing (PEP 412):**

```text
Shared keys: ['x', 'y']

p1 values: [1, 2]
p2 values: [3, 4]
```

* Keys stored once, values per instance → saves memory
* Adding a new attribute breaks sharing for that instance only

> Keys must be hashable (**hash** and **eq**)
> Item access is very fast (hash → index)
> Python 3.6+ preserves key order
> Hash table uses extra memory; empty slots improve efficiency

# Sets

* Collection of unique objects
* Uses {…} except for the empty set; empty set must be denoted as *set()*
* *Elements of the set must be hashable*
* Supports set operations like union, intersection, difference, symmetric difference ans in-place updates(for mutable sets only)

### Types

* sets → mutable
* frozenset → immutable; hashable (can be used as elements in other sets)

## Dictionary Views as Sets

* dict.keys() and dict.items() return view objects that behave like sets

* Support membership tests:

  ```python
  'a' in d.keys()
  ('a', 1) in d.items()
  ```

* Support set operations (&, |, -) with real sets and with each other:

  ```python
  d1 = {'a': 1, 'b': 2}
  d2 = {'b': 3, 'c': 4}

  d1.keys() & d2.keys()   # {'b'}
  d1.keys() | d2.keys()   # {'a', 'b', 'c'}
  ```
