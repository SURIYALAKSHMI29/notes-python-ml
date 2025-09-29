# Python: sys, argparse, and Slice

## sys

- A module that allows to take arguments at the command line
- **argv** - a list within the *sys* module that records what the user typed on the command line
- **argv[0]** - has file name
- **sys.exit()** - exits the program
- Checking Command line arguments using:
    - *try / except* - catches the error after it happens
    - *if + sys.exit()* - prevents the error by checking before accessing
        - *sys.exit(0)* - success (normal termination)
        - *sys.exit(1)* or any non-zero - error
    
```python
import sys

print("File name :", sys.argv[0])

# using try/except
try:
    print("Hello " + sys.argv[1])
except IndexError:
    print("Command line argument missing")

# using if + sys.exit()
if len(sys.argv) < 2:
    sys.exit("Command line argument missing")

print("Second argument is " + sys.argv[1])
````

---

## argparse

* A module designed for parsing command line arguments with descriptions, types, defaults
* Import, create parser, add arguments, parse the inputs from cmd line, then access
* Arguments:

  * positional arguments: must be provided
  * optional arguments: may or may not be provided in cmd line

```python
# Syntax
parser.add_argument(
    name_or_flags,        # e.g., "name" (positional) or "-a"/"--age" (optional)
    action=None,          # what to do with the argument (e.g., 'store', 'store_true')
    nargs=None,           # number of command line args to consume (e.g., '?', '*', '+', int)
    const=None,           # constant value for some actions
    default=None,         # default value if argument not provided
    type=None,            # type conversion (e.g., int, float, str)
    choices=None,         # restricts values (e.g., [10, 20, 30])
    required=False,       # only for optional args (must be given if True)
    help=None,            # help message shown in --help
    metavar=None,         # name shown in usage/help
    dest=None             # attribute name (defaults to argument name)
)
```

* **action** - tells *argparse* how to handle the argument when it appears

  * *store* - store the value given
  * *store\_true* - store True if the flag is present
  * *store\_false* - store False if the flag is present
  * *append* - append multiple values to a list if the option is repeated

    * usually if we give 2 values for the same flag, it will get overwritten
  * Flags are optional boolean switches (e.g., --verbose)

    * short (begins with `-`) or long (begins with `--`)
* **dest** - Name of the attribute where the value will be stored in *args*, defaults to argument name

```python
# argparse module

parser = argparse.ArgumentParser()
parser.add_argument("name", help="Name of the user")  # positional arg
parser.add_argument("-a", "--age", type=int, help="Age of the user")  # optional arg
parser.add_argument("-n", "--number", type=int, nargs=3, help="list of 3 numbers")
parser.add_argument(
    "-v", "--verbose", action="store_true", help="increase output verbosity"
)
parser.add_argument("color", choices=["red", "green", "blue"], help="choose a color")

args = parser.parse_args()

print(f"Hello {args.name}")
if args.age:  # optional argument if provided
    print(f"You are {args.age} years old")
print(f"Your favorite color is {args.color}")
if args.number:
    print(f"Your numbers are {args.number}")
if args.verbose:
    print("Verbose mode on")
else:
    print("Verbose mode off")
```

**Outputs**:

* If arguments are not provided:

```bash
$ python cmd_line.py
usage: cmd_line.py [-h] [-a AGE] [-n NUMBER NUMBER NUMBER] [-v] name {red,green,blue}
cmd_line.py: error: the following arguments are required: name, color
```

* If --help is executed:

```bash
$ python cmd_line.py --help
usage: cmd_line.py [-h] [-a AGE] [-n NUMBER NUMBER NUMBER] [-v] name {red,green,blue}

positional arguments:
  name                  Name of the user
  {red,green,blue}      choose a color

options:
  -h, --help            show this help message and exit
  -a, --age AGE         Age of the user
  -n, --number NUMBER NUMBER NUMBER
                        list of 3 numbers
  -v, --verbose         increase output verbosity
```

* Optional arguments example:

```bash
$ python cmd_line.py Suriya -a 20 -n 1 23 466 --verbose green
Hello Suriya
You are 20 years old
Your favorite color is green
Your numbers are [1, 23, 466]
Verbose mode on
```

---

## Slice

* Allows to extract a portion or subsequence from sequences like list, strings, tuples
* **Syntax**:

```python
sequence[start:stop:step]

start - where slicing begins (inclusive); Default: 0
end - where slicing ends (exclusive)
step - interval between the elements; Default: 1
```

* Example with sys.argv:

```python
print("Arguments:", args[1:] if len(sys.argv) > 1 else "No arguments")

# skips the file name
```

