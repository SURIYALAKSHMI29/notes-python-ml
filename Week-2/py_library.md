# Python Libraries, Packages, Random, Statistics, and APIs

## Table of Contents
1. [Libraries](#libraries)
2. [Packages](#packages)
3. [Random](#random)
4. [Statistics](#statistics)
5. [API](#api)
   - [Requests](#requests)
   - [JSON](#json)
6. [Own Libraries](#own-libraries)

---

## Libraries:

- Functions or features that can be shared as “modules”
- Can be included by,
    
```python
# Syntax
import library_name
from library_name import function
# can also give alias name
import lib_name as alias
````

---

## Packages:

* third-party libraries implemented as a folder
* PyPI - Python Package Index

  * a repository or directory of all available third-party packages
* PIP - Python package manager

---

## Random:

* Used for generating random numbers and making random selections

### **Common functions**

#### 1. Random numbers

```python
random.random()        # float between 0.0 and 1.0
random.randint(1, 10)  # integer between 1 and 10 (inclusive)

# randrange syntax
# random.randint(start, stop, step)

random.randrange(0, 10, 2)   
# picks randomly from (0, 2, 4, 6, 8); stop is not included
```

#### 2. Random choice

* choice() and sample() is used to pick random element(s) from a list of elements
* choice()

  * elements can be picked multiple times
  * By default k is 1, optional parameter
* sample()

  * element can only be picked once
  * k is mandatory parameter

```python
items = ["apple", "banana", "cherry"]
random.choice(items)  # randomly selects one element
random.choices(items, k=2)  # selects 2 elements (with replacement)

random.sample(items, 2)      # selects 2 elements without replacement
```

#### 3. Shuffling

* Shuffles the list in-place

```python
deck = [1, 2, 3, 4, 5]
random.shuffle(deck)
```

#### 4. Random float in a range

```python
random.uniform(1.5, 3.5)  # float between 1.5 and 3.5
```

#### 5. Setting a seed

* By default, *random* generates different random values on each run based on the system time or other sources
* Using a seed makes the random numbers **deterministic**
* Setting the same seed once gives the same random numbers every run
* Useful in debugging or testing

```python
import random 

random.seed(42)  # makes results reproducible
random.random()  # always return same result
```

---

## Statistics:

* Used for statistical computation like mean, median, mode, variance, etc.

### Commonly Used Functions and its usecase:

* Mean :  Average word length, avg sentence length
* Median : finding middle word / sentence length (less sensitive to outliers)
* Mode: Most frequent word or character
* Variance: how spread out sentence lengths or word lengths are

  * variance is average of how far each point is from the center
* Standard deviation: measures dispersion in sentence length, word counts

  * Dispersion - how spread out or scattered the data is
  * **Sentence length:** If all sentences are roughly the same length, dispersion is low; if some are very short and some very long, dispersion is high.
  * **Word frequency counts:** If a few words dominate and most occur rarely, the frequency distribution is highly dispersed.

---

## API

* Application Programming Interface - allows to connect to the code of others

### Requests:

* Requests - allows the program to behave as a web browser; used to make HTTP requests
* It returns a response object that contains the data, status code, headers, etc
* **Optional Arguments in requests:**

  * params - In GET requests, query parameters can be passed
  * headers - to send custom headers
  * data / json - send data in POST requests

```python
requests.post(url, data={"key": "value"})
requests.post(url, json={"key": "value"})
```

* response.json() - converts the HTTP response body into json or py dictionary format

```python
import sys
import requests

# 2 -> file name, pokemon name
if len(sys.argv) != 2:    
    print("Usage: python package.py <pokemon_name>")
    sys.exit(1)

# fetching the response from url
response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{sys.argv[1].lower()}")

# if fetched successfully
if response.status_code == 200:
    # .json() method converts the response to a dictionary
    data = response.json()
    print(f"Name: {data['name']}")
    print("Abilities:")
    for ability in data["abilities"]:
        print(f"- {ability['ability']['name']}")
else:
    print("Pokemon not found")
```

* **Timeouts and exceptions** - using try/except

  * If the server doesn’t respond in n seconds, python raises a *requests.exceptions.Timeout*
  * Can also give separate timeouts  for connect and read

    * *timeout(3, 7)* means 3 sec to connect, 7 sec to wait for data
  * Useful to prevent program from prolonged waiting if server is slow or unreachable

```python
# try to fetch the given url within 5 seconds
try:
    response = requests.get(url, timeout=5)  
except requests.exceptions.Timeout:
    print("Request timed out")
```

---

### json

* a built-in library or python module
* Used to parse JSON strings into python objects and vice versa

**Common Functions:**

* *json.loads()* - converts json strings into python dict / lists

  * response.json() does the same
* *json.dump()* or j*son.load()* - read/write json from files
* *json.dumps()* - convert python dict/lists into json strings
* **Syntax**:

```python
json.dumps(obj, indent = N)

# obj -python dict or list
# indent = N - adds N spaces for indentation for each level 
```

```python
import json

# same code as above
print(json.dumps(response.json(), indent=2))
```

* Here json.dumps() - makes the response more readable by converting the python dictionary / list into a json-formatted string

**requests and JSON:**

* requests gives the response in text
* Most APIs return JSON-formatted responses

---

## Own libraries:

* Module : A single .py file containing reusable functions or classes
* Package: A folder of modules with an **init**.py file
* Importing:

  * import module - can access all functions as module.func()
  * from module import func - access directly via func()
* By this way, code can be reused, organized and functionalities can be shared with others


