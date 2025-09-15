# Python: Variables and Functions

## Table of Contents
1. [Variables](#variable)
2. [Strings](#strings)
3. [Integers and Floats](#integers-or-int)
4. [Type Checking](#type)
5. [Comments](#comments)
6. [Functions](#functions)
7. [Function Arguments](#arguments-passed)
8. [Return Values](#return-values)

---

## Variable:

- Container used to store values
- snake_case is used

### Strings:

- Immutable; Sequence of text; *str*
- Python 3 strings are Unicode by default
- String formatter:
    
    ```python
    print(f”Hello, {var_name}”)
    # f -> format specifier
    ```
    
- To remove leading and trailing white spaces in a string: **strip()**
    - ***Syntax**: var_name.strip()*
    - **lstrip()** - removes left side
    - **rstrip()** = removes right side
- To Capitalize first letter of each word: **title()**
    - ***Syntax**: var_name.title()*
    
    ```python
    name = input("What is your name? ").strip().title()
    print("Welcome", name)
    ```
    
- To capitalize first letter of a string: **capitalize()**
- **str.split(), rsplit(), join()**
    - **Purpose:** Split string into parts / join parts into string
    
    ```python
    s = "a,b,c"
    print(s.split(","))    # ['a', 'b', 'c'] → split from left
    print(s.rsplit(",", 1))# ['a,b', 'c'] → split from right, max 1 split
    lst = ['a', 'b', 'c']
    print(",".join(lst))   # "a,b,c"
    ```
    

### Integers or int:

- *input()* considers the input as *str*
- *int(x)* → converts x into *int* data type
    - Note: the above conversion is called as **Casting**

### Float:

- Real Number that has a decimal point; *float()* is used
- Here, float ****is a **double-precision floating-point number** internally
- Round to a nearest value:
    - **Syntax**: *round(number[, ndigits])*
        - number - required field, the num needs to be rounded is gn
        - [, ndigits ] - optional field, if not given, rounds to nearest integer value
    
    ```python
    """
    Exploring round() func 
    """
    x = 1001.5213897
    print(x)               # 1001.5213897   
     
    # rounds to nearest integer
    print(round(x))        # 1002
    
    # rounds to 4 decimal places
    print(round(x, 4))     # 1001.5214
    
    # formatted string literals (f-strings); rounds to 2 decimal places
    print(f"{x:.2f}")      # 1001.52
    
    # adds commas as thousand separators
    print(f"{x:,}")        # 1,001.5213897
    
    # combines both formatting options
    print(f"{x:,.2f}")     # 1,001.52
    
    # Rounding to tens using negative ndigits
    print(round(x, -1))    # 1000.0
    ```
    
    - Rounds **halfway values to the nearest even number** (banker’s rounding):
    
    ```python
    print(round(2.5))  # Output: 2
    print(round(3.5))  # Output: 4
    ```
    

### **Type():**

- Used to check variables’s type
- For debugging, `print(f"{var=}")` shows both variable name and value

```python
# type() function

def check_type(var):
    # print(f"The type of {var} is {type(var)}")
    print(f"{var=} is of type {type(var)}")
    print()

check_type(10)
# var=10 is of type <class 'int'>

check_type(10.5)
# var=10.5 is of type <class 'float'>

check_type("Hello")
# var='Hello' is of type <class 'str'>

check_type(True)
# var=True is of type <class 'bool'>

check_type([1, 2, 3])
# var=[1, 2, 3] is of type <class 'list'>

check_type((1, 2, 3))
# var=(1, 2, 3) is of type <class 'tuple'>

check_type({1, 2, 3})
# var={1, 2, 3} is of type <class 'set'>

check_type({"a": 1, "b": 2, "c": 3})
# var={'a': 1, 'b': 2, 'c': 3} is of type <class 'dict'>

check_type(None)
# var=None is of type <class 'NoneType'>

check_type(lambda x: x + 1)
# var=<function <lambda> at 0x7bc19f393740> is of type <class 'function'>
````

---

## Comments:

* Used to explain code
* Improve readability and maintenance
* Ignored by intrepreters
* Single line comment → #    (begins with hash symbol)
* Multi-line comment → “””    (triple quotes)

---

## Functions:

* Actions; block of code that performs a specific task
* Write Once, and call it whenever needed →  resusable
* **print()** - is a function, that outputs the gn content on the terminal screen

  * By default, automatically create a line break
  * Can be modified by using ‘end’. For example,

  ```python
  print(”Hello “, end=” “)
  print("Suriya")
  # it doesn't creates a new line
  # Expected Output: Hello Suriya

  # if end is not given, then output will be like
  # Hello
  # Suriya
  ```

  * **flush**:

    * flush = True → forces Python to immediately write output from its internal buffer to the terminal (or file)
    * flush = False (default) → output may stay in a buffer for a little while before actually appearing
    * It is False by default due to performance reason; Writing to console/file is relatively slow
    * flush = True will be opted when we need Real-time output (e.g., progress bars, logs, live updates).
    * Terminal: auto-flush on \n (interactive mode).
    * Files: flush only when buffer full/closed
* **input()** - used to get input from user

  * By default, inputs are treated as *str*

### Syntax:

```
def function_name(parameters):
        """
        Optional: Docstring that describes the function
        """
        # Code block
        return value  # optional
```

**Note**: Everything under *def* is indented

* Default parameters can be given,

  ```python
  def say_hello(var1 = “Guest”):
     print( f”Hello, {var1} “)
  ```

  * Here,  *say\_hello(”Suriya”)* prints, Hello, Suriya
  * *say\_hello()* prints, Hello, Guest

---

## Arguments Passed:

* Arguments are usually passed by “assignment” (or object reference)
* This behaves like,

  * Immuable Objects (str, float, bool,..) :

    * Copy of Reference is passed   (Pass by Value)
    * Original object will not get affected
  * Mutable Objects (list, dist, set,..) :

    * Reference to the object is passed   (Pass by Reference)
    * Changes inside the func, affects the orginal value also

1. **Positional Arguments:**

   * Values are assigned to parameters in the order they appear
2. **Keyword Arguments:**

   * Values are assigned explicitly to parameter names, so order doesn’t matter
3. **Mixed Arguments:**

   * Positional arguments must come first, then keyword arguments
4. **Variable-length positional arguments (tuple) :**

   * * is used before the variable name
   * Collects extra positional arguments into a tuple
5. **Variable-length keyword arguments (dict) :**

   * \*\* is used before the variable name
   * Collects extra keyword arguments into a dictionary.

```python
def demo_func(a, b=10, *numbers, c=0, flag=True, **data):
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"numbers = {numbers}")
    print(f"c = {c}")
    print(f"flag = {flag}")
    print(f"data = {data}")
    print()

# 1. Positional Arguments
demo_func(29, 13)

# 2. Keyword Arguments
demo_func(a=5, b=15)

# 3. Mixed Arguments
demo_func(10, c=99, flag=False)

demo_func(1)
demo_func(5, 15, 20, 25, 30)
demo_func(3, 33, 44, 55, flag=False)
demo_func(7, 77, 88, 99, flag=True, name="Suriya", city="Madurai")
```

* **Note:** c=0, flag=True → these come after \*numbers → keyword-only arguments
* **Note:** \*\*data catches extra keyword arguments into a dictionary

---

## Return Values:

* **Passing back of value** to the caller
* A func may or may not return a value
* Multiple return values:  Allows returning tuples from a function

```python
# Multiple Return Values
def get_coordinates():
    return (10, 20)

x, y = get_coordinates()
print(x, y)  # 10 20
```
