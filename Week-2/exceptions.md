# Python Exceptions & Loops

## Table of Contents
- [Exceptions](#exceptions)
  - [Common Built-in Exceptions](#common-built-in-exceptions)
  - [Keywords: try, except, else, finally, raise](#keywords-try-except-else-finally-raise)
- [Loops](#loops)

---

## Exceptions:

- Errors detected during execution - runtime errors
- Has built-in exceptions and user-defined exceptions
- Can be handled by using try-except blocks
- Python has a  **Exception class -** which acts as a base class and catch all exceptions:
    
    ```python
    except Exception as e:
        # code
    ```
    

### **Common Built-in Exceptions**

- ValueError → invalid value
- TypeError → wrong type
- ZeroDivisionError → division by 0
- FileNotFoundError → missing file

### Keywords: try, except, else, finally, raise

### try:

- Code that might throw an error is enclosed within a try block
- If an error occurs, it will be caught by the corresponding except block

### except:

- Multiple except blocks can be used
- Each block handles a specific exception and contains the code to execute if that exception occurs.

### else:

- Executed only if no exception occurs in the *try* block
- If an exception occurs before reaching *else*, this block is skipped.

### finally:

- Always executed, regardless of whether an exception occurred or not.
- Mostly used for cleanup, such as closing files or releasing resources

```python
'''
Syntax:

try:
    ...
except ExceptionType:
    ...
else:
    # Runs only if no exception occurred
    ...
finally:
    # Always runs, used for cleanup
    ...
'''

def division():
    try:
        numerator = float(input("Enter numerator:"))
        denominator = float(input("Enter denominator:"))
        result = numerator / denominator
    except ValueError:  # Occurs when conversion to float fails
        print("Invalid input. Please enter numeric values.")
    except ZeroDivisionError:  # Occurs when denominator is zero
        print("Error: Division by zero is not allowed.")
    else:
        print(f"The result is: {result: .2f}")
    finally:
        print("Execution completed.")

division()
````

### raise:

* Used to manually throw an exception; can raise built-in or user-defined exceptions
* Stops execution if not caught with try-except

```python
**# Syntax:** 

raise ExceptionType("Optional custom message")
```

* ExceptionType - built-in (e.g., ValueError) or custom exception class.
* Message - optional string describing the error.

```python
**# Raising a built-in exception**
x = -1
if x < 0:
    raise ValueError("x cannot be negative")
print "Hello"      # This line will NOT run if exception is not caught

# NOTE: if not caught then it displays the error and stop executing the program
# Output: ValueError: x cannot be negative

**# Catching the raised exception**
try:
    x = -1
    if x < 0:
        raise ValueError("x cannot be negative")
except ValueError as e:
    print("Handled:", e)
print "Hello"     # This line runs because exception was caught

# Here, output will be
# Handled: x cannot be negative
# Hello						

**# Custom exceptions**

class exceptionName(Exception):
        # code
# exceptionName is gn as <ExceptionType> while raising an exception
```

---

## Loops:

### pass:

* Does nothing; More like a placeholder
* Often used in empty functions, classes and loops
* Can also be used inside an *except* block if you want to **ignore an exception**.

### continue:

* Skips the rest of the current Iteration and moves to the next iteration of the loop

### break:

* exits the loop immediately
* If you want to exit a loop and return a value, you can use *return* instead of *break* inside a function.

