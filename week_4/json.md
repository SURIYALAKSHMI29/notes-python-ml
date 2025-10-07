# Table of Contents

- [JavaScript Object Notation](#javascript-object-notation)
  - [Writing JSON](#writing-json)
  - [Reading JSON](#reading-json)
  - [Prettify JSON](#prettify-json)
  - [To validate a JSON file](#to-validate-a-json-file)
  - [Minify JSON](#minify-json)

# JavaScript Object Notation

- Using python’s json module
    - Can convert Python data types to a JSON-formatted string with *json.dumps()*
    - Write them to files using *json.dump()*
    - Can read JSON data from files using *json.load()*
    - Parse JSON strings with *json.loads()*
- Standard for data Interchange
- Key-value pairs; white-spaces doesn’t matter in JSON
- **JSON Data type**
    - object → collection of key-value pairs inside curly braces **{ }**
    - array → list of values wrapped inside square brackets **[ ]**
    - string → Text wrapped in **double quotes**
    - number → Integers or floating-point numbers
    - boolean → either **true** or **false** without quotes
    - null → represents a **null** value
- *JSON Lint* and *JSON Formatter* → online tools for validating JSON
- Doesn’t allow comments, trailing commas, or single quotes for strings

> Human JSON (Hjson) → gives freedom to use comments, trailing comments between properties, or create quoteless strings

JSONC → JSON with comments; allows to use comments and trailing commas
> 

## Writing JSON

**Serialization →** converting data into the JSON format

### **.dumps()**

- Converts python data into a JSON object
- returns a python str
- When you convert a dictionary to JSON, the dictionary keys will always be strings in JSON
- Python values → JSON values
    - dict → object
    - list, tuple → array
    - int, float → number
    - str → string
    - True, False, None → true, false, null
- Dictionaries, List, Tuple cannot be keys in JSON, if used → TypeError is raised
    - By providing **skipkeys = True,** prevent getting a TypeError, instead skips the keys that are not supported.
    
    ```python
    import json
    
    available_nums = {(1, 2): True, 3: False}
    **# print(json.dumps(available_nums))
    # throws TypeError**
    # TypeError: keys must be str, int, float, bool or None, not tuple
    
    print(json.dumps(available_nums, skipkeys=True))  # {"3": false}
    ```
    
    - Can sort the dictionary keys by setting the sort_keys = True
        
        ```python
        dic1 = {4: "suriya", 3: "raji", 5: "karthiga"}
        dic1_json = json.dumps(dic1, sort_keys=True)
        print(dic1_json) # {"3": "raji", "4": "suriya", "5": "karthiga"}
        ```
        

### **.dump()**

- Write a JSON file with python
- Has two required function arguments → data object and file

```python
# json -> file
with open("json_data.json", "w") as file:
    json.dump(dic1, file)
# python obj, file_name    
```

## Reading JSON

**Deserialization →** Decoding data from the JSON format back into a usable form within Python

### .loads()

- Used to deserialize a string, bytes, or byte array instances
- Deserialization is not the exact reverse of the serialization process → JSON keys are always strings, and not all python data types can be converted to JSON data types
    
    ```python
    dic1_py = json.loads(dic1_json)
    print(dic1_py)  # {'3': 'raji', '4': 'suriya', '5': 'karthiga'}
    
    print(dic1 == dic1_py)  **# False -> keys' types are changed**
    
    ```
    

### .load()

- used to open an external JSON file with python
- Argument for the load() function must be either a text file or binary file
- JSON file → deserialize → python object, then
- The file must contain valid JSON syntax, otherwise will receive JSONDecodeError

```python
# json file -> python obj
with open("json_data.json", "r") as file:
    data = json.load(file)
    print(data)  # {"3": "raji", "4": "suriya", "5": "karthiga"}
```

## Prettify JSON

- ***indent -*** default value is None; can be specified to prettify the json content
- used with json.dumps() and json.dump()

## To validate a JSON file

- ***json.tool -*** can be used

```
$ python -m json.tool file_name

# file_name -> json file that needs to be validated
# by default, prints with indent=4
# if invalid -> error will be shown otherwise entire file content will be displayed
```

- indent can be modified by,
    
    ```
    python -m json.tool file_name --indent n
    ```
    
- Adding indent → increase file size

## Minify JSON

- To remove any white space between the key-value pairs —compact can be used

```
$ python -m json.tool in_file.json out_file.json --compact
```

- If in_file is present → overwrites it, otherwise creates a new file as out_file
- It even removes the white space between the key and its value
