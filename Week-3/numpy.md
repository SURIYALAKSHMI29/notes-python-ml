# NumPy 

## Table of Contents

1. [NumPy](#numpy)
2. [Arrays](#arrays)

   * [Creation](#creation)
   * [Array Attributes](#array-attributes)
   * [Indexing and Slicing](#indexing-and-slicing)
   * [Reshaping and Broadcasting](#reshaping-and-broadcasting)
   * [Mathematical Operations](#mathematical-operations)
   * [Splitting](#splitting)
   * [Search](#search)
   * [File I/O](#file-io)
3. [SciPy](#scipy)

---

## NumPy (Numerical Python)

* Implements multi-dimensional, homogeneous arrays and matrix types
* Can hold numbers as well as user-defined records
* Provides an array object **“ndarray”** that is 50x faster than python lists

  * Lists → store references to objects, scattered in memory → slower
  * NumPy arrays → **contiguous memory allocation** → 50x faster than lists
* Written partially in python and most of the parts that require fast computation are written in C or C++

---

## Arrays

### Creation

```python
import numpy as np

arr = np.array((1, 2, 3))  # 1D array from tuple
print(arr)
# Output: [1 2 3]

print(np.zeros((1, 2, 3)))  # 3D array of zeros (1x2x3)
# Output: [[[0. 0. 0.]
#           [0. 0. 0.]]]

print(np.ones((1, 2)))  # 2D array of ones (1x2)
# Output: [[1. 1.]]

print(np.full((2, 3), 13))  # 2D array filled with 13 (2x3)
# Output: [[13 13 13]
#          [13 13 13]]

print(np.arange(2, 10, 2))  # 1D array: 2,4,6,8
# Output: [2 4 6 8]

print(np.linspace(0, 1, 5))  # 1D array: 5 numbers from 0 to 1
# Output: [0.   0.25 0.5  0.75 1.  ]
```

### Array Attributes

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.shape)  # dimensions of array
# (2, 3)

print(arr.ndim)  # number of dimensions
# 2

print(arr.size)  # Total elements
# 6

print(arr.dtype)  # Data type of elements
# int64
```

### Indexing and Slicing

```python
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

print("Column 2:", a[:, 2])  # Column Slicing
# Column 2: [ 3  6  9 12]

print("Rows 0,2,3:\n", a[[0, 2, 3]])  # Select specific rows (0, 2, 3)
# Rows 0,2,3:
#  [[ 1  2  3]
#  [ 7  8  9]
#  [10 11 12]]

print("Elements > 5:", a[a > 5])  # Elements greater than 5
# Elements > 5: [ 6  7  8  9 10 11 12]
```

### Reshaping and Broadcasting

```python
a = a.reshape(3, 4)  # returns a new array, not modifies in-place
print(a)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

print(a.transpose())  # modifies row as col and col as rows, returns new array
# [[ 1  5  9]
#  [ 2  6 10]
#  [ 3  7 11]
#  [ 4  8 12]]

print(a + 5)  # allows to add a scalar to every elements
# [[ 6  7  8  9]
#  [10 11 12 13]
#  [14 15 16 17]]

print(a + a)  # combine arrays, if shapes compatible
# [[ 2  4  6  8]
#  [10 12 14 16]
#  [18 20 22 24]]
```

### Mathematical Operations

* +, -, *, /, ** → element wise operations
* sum(), mean(), std(), var(), argmax(), argmin(), min(), max()

> min(), max() - returns the min/max elements
> argmin(), argmax() - returns the index of min/max

### Splitting

* np.split(arr, n) → splits the array into n parts, throws error if array cannot be evenly distributed
* np.array_split(arr, n) → splits even if size not divisible

```python
arr = np.arange(4)
print(np.split(arr, 2))
# [array([0, 1]), array([2, 3])]

print(np.array_split(arr, 3))  # allows uneven splits
# [array([0, 1]), array([2]), array([3])]
```

### Search

* np.where(condition)   - returns indices of elements that satisfy the condition
* np.searchsorted(sorted_array, value) - finds the index where a value should be inserted to keep the array sorted

```python
arr = np.array([10, 20, 30, 40, 50])
print(np.where(arr > 25))          # (array([2, 3, 4]),)
print(np.searchsorted(arr, 25))    # 2
```

### File I/O

```python
# Save array to a text file
np.savetxt("array.txt", arr, fmt="%d")  # fmt='%d' ensures integers

# Load array from the text file
loaded_arr = np.loadtxt("array.txt")
print("Loaded 1D array from text:", loaded_arr)
# Output: [10. 20. 30. 40. 50.]

# Memory-mapped arrays (large datasets)
# Create a large array
large_arr = np.arange(1000000)

# Save as binary file
np.save("large.npy", large_arr)

# Load as memory-mapped array (doesn't load all into RAM)
mm_arr = np.load("large.npy", mmap_mode="r")
print("First 5 elements of memory-mapped array:", mm_arr[:5])
# Output: [0 1 2 3 4]
```

> `mm_arr = np.load("large.npy", mmap_mode="r")`

* mmap_mode="r" → memory-mapped mode, read-only
* Does NOT load the entire array into RAM
* Only reads the part accessed (slicing)
* Useful for very large datasets that don’t fit in memory

---

## SciPy

* A library written on top of NumPy, offering many scientific computing algorithms
* Fast and reliable
