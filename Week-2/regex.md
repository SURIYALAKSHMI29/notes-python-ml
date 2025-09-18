# Regular Expressions in Python

## Table of Contents
- [Common Functions](#common-functions)
- [Examples](#examples)
- [Case Sensitivity](#case-sensitivity)
- [Walrus Operator](#walrus-operator)
- [Exercises](#exercises)

---

## Introduction
- Regex is a way to search, match, and manipulate strings based on patterns
- In Python, the **re** module is used

## Common Functions
- **re.match(pattern, string)**  
  Checks if the pattern matches at the start of the string
- **re.search(pattern, string)**  
  Searches anywhere in the string for the pattern
- **re.findall(pattern, string)**  
  Returns a list of all matches in the string
- **re.split(pattern, string)**  
  Splits the string based on the pattern
- **re.sub(pattern, replacement, string)**  
  Replaces all matches of the pattern with the given replacement

## Quantifiers (Repetition)
- `*` → zero or more repetitions  
- `+` → one or more repetitions  
- `?` → zero or one repetition  
- `{m}` → exactly m repetitions  
- `{m,n}` → between m and n repetitions  

## Anchors (Position)
- `^` → matches the start of the whole string  
- `$` → matches the end of the whole string (or just before newline)  

## Character Sets
- `[...]` → matches any character listed  
- `[^...]` → negated set, matches any character not listed  

## Predefined Character Classes
- `\d` → decimal digit (0–9)  
- `\D` → not a decimal digit  
- `\s` → whitespace character (space, tab, newline)  
- `\S` → not a whitespace character  
- `\w` → word character (letters, digits, underscore)  
- `\W` → not a word character  

## Special Symbols
- `.` → any character except a newline  
- `A|B` → matches either A or B  
- `(...)` → capturing group (can reference later with `group(n)`)  
- `(?:...)` → non-capturing group (just for pattern logic, no capture)  

## Examples

```python
import re

text = "Hello, my name is Suriya. Contact: suriya123@example.com or call 9876543210."

# Check if sentence starts with "Hello"
if re.match(r"Hello", text):
    print("Sentence starts with Hello")

# Search for a word anywhere
if re.search(r"Suriya", text):
    print("Found the name Suriya")

# Find all numbers in the text
numbers = re.findall(r"\d+", text)
print("Numbers found:", numbers)

# Split text by spaces, commas, or periods
words = re.split(r"[ ,\.]+", text)
for word in words:
    print(word)

# Replace email with placeholder
new_text = re.sub(r"[\w+\.-]+@([a-zA-Z][\w-]*\.){1,2}(com|edu|gov|in|nry|org)", "[email]", text)
print("After replacing email:", new_text)

# Extract email using groups
email_match = re.search(r"([\w\.-]+)@(\w+)\.(gov|com|edu|net|org)", text)
if email_match:
    print("Full email:", email_match.group(0))
    print("Username:", email_match.group(1))
    print("Domain:", email_match.group(2))
    print("Extension:", email_match.group(3))

# Non-capturing group example
sentence = "I like banana pie"
pattern = r"(?:apple|banana) pie"
match = re.search(pattern, sentence)
if match:
    print(match.group(0))

# Email validation function
def check_email_validity(email):
    pattern = r"^[\w\.-]+@([a-zA-Z][\w-]*\.)*(com|edu|gov|in|net|org)$"
    return re.search(pattern, email)
````

**Explanation:**

* `[\w\.-]+` → username

* `@` → literal @

* `([a-zA-Z][\w-]*\.){1,2}` → domain (handles cs50.harvard)

* `(com|edu|gov|in|nry|org)` → extension

* `$` → end of string

* Inside `[ ]`, `.` is literal

* `(?=.*[0-9])` → lookahead, ensures a digit exists

## Case Sensitivity

* Regex are **case sensitive** by default
* Flags:

  * `re.IGNORECASE` → case insensitive
  * `re.MULTILINE` → `^` and `$` match start/end of each line
  * `re.DOTALL` → `.` matches newline characters

## Walrus Operator

* Assignment expression introduced in Python 3.8
* Allows assignment inside expressions
* Example:

```python
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
```

* Assigns `matches` and evaluates `if` in a single line

## Exercises

1. **Validating email address**

```regex
^([a-zA-Z][\w.-]*)@(\w+\.)?\w\.(com|edu|in|gov|net|org)$
```

2. **Extract HashTags from a tweet**

```python
pattern = r"#[\w]+"
hashtags = re.findall(pattern, tweet)
```

3. **Extract phone numbers in formats like**

* 9876543210
* (0452) 234567
* +91-98765-43210

```regex
(?:\d{10}|\(\d{4}\)\d{6}|\+\d{2}-\d{5}-\d{5})
```

4. **Validate Strong Password**

* At least 8 characters
* At least one uppercase, one lowercase, one digit, one special char (@#\$%^&\*!)

```regex
^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$%^&*!]).{8,}$
```

5. **Extract Twitter Username from URL**

* URLs:

  * `https://twitter.com/suriya_123`
  * `http://www.twitter.com/DavidMalan`
  * `twitter.com/python_dev`

```python
pattern = r"^(?:https?://)?(?:www\.)?twitter\.com/(.+)$"
matches = re.search(pattern, url)
print(matches.group(1))
```

Alternative using `re.sub`:

```python
pattern = r"(https?://)?(www\.)?twitter\.com/"
user_name = re.sub(pattern, "", url)
print(user_name)
```
