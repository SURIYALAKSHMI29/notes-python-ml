# Fluent Python - Chapter 2: Array of Sequences

## Table of Contents

1. [Built-in Sequences](#built-in-sequences)

   * [Types](#types)

     * [Container Sequences](#container-sequences)
     * [Flat Sequences](#flat-sequences)
   * [Based on Mutability](#based-on-mutability)

     * [Mutable Sequences](#mutable-sequences)
     * [Immutable Sequences](#immutable-sequences)
2. [Slicing](#slicing)
3. [List Comprehension](#list-comprehension)
4. [Generator Expressions](#generator-expressions)
5. [Using + and \* with Sequences](#using--and--with-sequences)
6. [Augmented Assignment with Sequences](#augmented-assignment-with-sequences)
7. [Sorting Lists](#sorting-lists)
8. [Tuple](#tuple)
9. [Pattern Matching (Python ≥ 3.10, PEP 634)](#pattern-matching-python-≥-310-pep-634)
10. [Arrays](#arrays)
11. [Memory Views](#memory-views)

---

## Built-in Sequences

### Types

#### Container Sequences

* Can hold items of different types, including nested containers.
* Examples: `list`, `tuple`, `collections.deque`
* Holds references to the objects it contains.

#### Flat Sequences

* Hold items of one simple type.
* Examples: `str`, `bytes`, `array.array`
* Stores the value of its content in its own memory space.

**Example**

![tuple - Left side; Array - Right side](attachment:668eff87-9d55-4927-8ece-742ac2c1421e\:image.png)

* tuple: has an array of references to its items; each item is a separate Python object
* array: a single object holding array values

> Every Python object in memory has a header with metadata. Holding the raw values (array) is much more compact than using tuple of objects.

### Based on Mutability

#### Mutable Sequences

* Can be modified; examples: `list`, `array.array`, `bytearray`

#### Immutable Sequences

* Cannot be modified; examples: `set`, `str`, `tuple`

---

## Slicing

* Slicing and range exclude the last item.
* When only stop is given → length = stop value.
* When start and stop are given → length = stop - start.
* Multidimensional slicing: `seq[m:n, k:l]`

**Use case:**

1. Extract information from sequences.
2. Change mutable sequences.

```python
l = list(range(10))
l[2:5] = [14]
```

---

## List Comprehension

* Used to build new lists from iterables with filtering and transforming items.

### Local Scope

* Normal comprehension: loop variable disappears after execution.

```python
x = 'ABC'
codes = [ord(c) for c in x]
print(c)  # NameError
```

* Using walrus operator `:=` retains variable in enclosing scope.

```python
codes = [last := ord(c) for c in 'ABC']
print(last)  # 67
```

---

## Generator Expressions

* Initialize tuples, arrays, or other sequences.
* Memory-efficient; yields results one by one.

```python
gen = (x*x for x in range(10))
```

---

## Using + and \* with Sequences

* `+` and `*` create new objects; operands unchanged.

```python
l = [1, 2, 3]
print(l * 2)  # [1,2,3,1,2,3]
```

* `*` creates shallow copies; mutable elements share references.

```python
l2 = [1,2,3,[4,5]]
l3 = l2 * 2
l3[3].append(6)
```

* Safer with nested list: list comprehension.

```python
board = [['_']*3 for i in range(3)]
```

---

## Augmented Assignment with Sequences

* `+=` → in-place addition (`__iadd__`)
* `*=` → in-place multiplication (`__imul__`)
* Mutable sequences: changed in-place; immutable: new object created.

```python
t = (1,2,[30,40])
t[2] += [50,60]
```

---

## Sorting Lists

1. `list.sort()` → sorts in-place, returns None
2. `sorted(list)` → returns new sorted list

**Optional keyword arguments:**

* `reverse=True` → descending
* `key=function` → sorting key

```python
fruits = ['grape','raspberry','apple','banana']
fruits.sort(reverse=True)
```

> Use arrays or deque for memory efficiency and optimal operations.

---

## Tuple

* Immutable sequences; defined by commas.
* Single-element tuple: `(1,)`
* Can hold records; mutable objects inside can change.

```python
a = (10,'alpha',[1,2])
b = (10,'alpha',[1,2])
b[-1].append(99)
```

* Use `hash()` for fixed-value tuple.

---

## Pattern Matching (Python ≥ 3.10, PEP 634)

* `match/case` allows destructuring sequences.

```python
match message:
    case ['LED', ident, red, green, blue]:
        set_color(ident, red, green, blue)
```

**Rules:**

1. Subject must be sequence.
2. Same number of items.
3. Items match.

* `_` matches anything but unbound
* `as` binds part of match
* Type checks possible

---

## Arrays

* Mutable numeric sequences; typecode defines underlying C type.
* Supports integers (1,2,4,8 bytes) and floats.
* Sorting: `sorted(array)`
* Keep sorted: `bisect.insort(array,value)`

---

## Memory Views

* `memoryview` → access memory of objects without copying.
* Modifying view reflects in original.

```python
data = bytearray(b'hello world')
mv = memoryview(data)
mv[0:5][0] = 72  # modifies original
```

* `.cast(new_format)` → reinterpret memory type; shares memory between views.
