# Python: Conditionals, Loops, Lists, and Dictionaries

## Table of Contents
1. [Conditionals](#conditionals)
2. [match](#match)
3. [Loops](#loops)
    - [While loop](#while-loop)
    - [For loop](#for-loop)
4. [List](#list)
5. [Dictionary (dict)](#dictionary-dict)

---

## Conditionals

- **if Statements:** Execute code based on a condition.
    
    **Syntax:**
    
    ```python
    if condition:
        # code to execute
    ```
    
- **elif and else:** Provide alternative conditions and default actions.
    - **elif** (else if) - allows multiple conditions.
    - **else** - provides a default action if no conditions are true.
- **Ternary Conditional:**
    - return True if condition else False

## match

- used like a switch-case to run code based on specific values
- Supported in Python 3.10+
    
```python
def http_status(status_code: int) -> str:
    match status_code:
        case 200:
            print("OK")
        case 404 | 500:    
            print("Error")
        case _:
            print("Unknown Status Code")

# vertical bar '|' - Similar to 'or' keyword, 
# this allows us to check for multiple values in the same case statement.

http_status(200)    # Ok
http_status(404)    # Error
http_status(999)    # Unknown Status Code
```

## Loops:

- Used to perform repeated tasks

### While loop:

- Terminates if the condition is met
- Works by checking the condition each iteration

```python
'''
Syntax:
while condition:
	# code to execute
'''

i = 0
while i < 3:
	print(i)
	i+=1
```

- User inputs are mostly validated using a while loop

### For loop:

- Iterates through a *list* of items

```python
for i in [1,2,..n]:    # runs n times
	# code

for i in range(3):     # runs 3 times -> 0, 1, 2
	# code

for _ in range(3):     # runs 3 times, used when iterable variable is not needed
	# code
```

Can also be done as:

```python
print("Suriya\n" * 3, end="")      

# Here end="" is used because \n is already at the end of the string
# Without end="", print() would add an extra new line after the 3rd repetition
# This prevents an additional blank line in the output

# expected Output: 
# Suriya
# Suriya
# Suriya
```

## List

- Can store mixed types; Dynamic in size
- Can be accessed by index and uses square brackets [ ]

```python
students = ["Akshaya", "Harsha", "Harshita", "Suriya"]

def print_students(students):

    for student in students:
        print(student)

    print()

    for i in range(len(students)):      # using length of the list
        print(f"{i + 1}. {students[i]} ")

print_students(students)

''' 
Expected Output:
Akshaya
Harsha
Harshita
Suriya

1. Akshaya 
2. Harsha 
3. Harshita 
4. Suriya 
'''
```

## Dictionary (dict):

- Key-value pairs; Uses curly braces { }
- Values can be accessed using keys

```python
pokemons = {
    "Ash": "Pikachu",
    "Misty": "Bulbasaur",
    "Brock": "Pidgey",
}

pokemons_list = [
    {"trainer": "Ash", "pokemon": "Pikachu", "type": "Electric"},
    {"trainer": "Misty", "pokemon": "Bulbasaur", "type": "Water"},
    {"trainer": "Brock", "pokemon": "Pidgey", "type": "Flying"},
]

def print_dict(d):
    for key in d:
        print(f"{key} has {d[key]}")
    print()

def print_list_of_dict(lst):
    for d in lst:
        print(f"{d['trainer']} has {d['pokemon']} which is of type {d['type']}")

print_dict(pokemons)
# Ash has Pikachu
# Misty has Bulbasaur
# Brock has Pidgey

print_list_of_dict(pokemons_list)
# Ash has Pikachu which is of type Electric
# Misty has Bulbasaur which is of type Water
# Brock has Pidgey which is of type Flying
```
