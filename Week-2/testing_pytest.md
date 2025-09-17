# Table of Contents
- [assert](#assert)
- [pytest](#pytest)
  - [Fixtures](#fixtures)
    - [Fixture Scope](#fixture-scope)
    - [Fixture Parameters](#fixture-parameters)
  - [Parametrization](#parametrization)
  - [Grouping tests](#grouping-tests)
  - [Skipping Tests](#skipping-tests)
  - [Expected Failure](#expected-failure)
  - [Notes](#notes)

---

# assert

- *assert* command is used to test if a condition is true; acts as a debugging aid  
- As soon as the condition in the assert statement evaluates to False, Python immediately stops execution of the program at that line.  

**Syntax:**
```python
assert condition, optional_message
````

* condition - the boolean expression you expect to be true.
* optional\_message - an optional string that will be displayed if the assertion fails.

```python
y = -2
assert y > 0, " y should be positive"

$python assert_ex.py
Traceback (most recent call last):
  File "/home/suriya-pt7984/Documents/python-demo/src/testing/assert_ex.py", line 2, in <module>
    assert y > 0, " y should be positive"
           ^^^^^
AssertionError:  y should be positive
```

---

# pytest

* a third-party library used to unit test the program (i.e.) can test the functions within the program
* Test files should always start with `test_` or end with `_test.py`
* Test functions should start with `test_`

```bash
pytest             # discovers and runs all tests in the current directory
pytest -v          # verbose mode
pytest test_file.py   # run tests in a specific file
pytest -k "addition"  # run tests whose names contain 'addition'
```

* assert can be used to check expected behavior
* pytest gives detailed failure reports automatically

---

## Fixtures

* A reusable setup function
* Used to set up preconditions for tests; these are the functions that run before the test functions to provide setup/teardown code
* ***@pytest.fixture*** marks the function as a fixture
* When a test uses the fixture name, pytest injects its return value into the test

Mainly used for:

* Prepare data, objects, or environments for tests
* Manage resources like database connections, files, API clients, etc.
* Make tests clean and reusable

```python
import pytest

@pytest.fixture
def sample_data():
    return [1, 2, 3]

def test_sum(sample_data):
    assert sum(sample_data) == 7 
    
# shows a detailed AssertionError when pytest filename.py is executed
```

---

### Fixture Scope

* Can be reused across tests at different levels using scope; Default scope: `function`
* **function** → runs before each test function (default).
* **class** → runs once per test class.
* **module** → runs once per test file.
* **session** → runs once for the entire test run (useful for global resources).

---

### Fixture Parameters

* Can also take parameters to run tests with different setups

```python
import pytest

@pytest.fixture(params=[1, 2, 3])
def num(request):   # request is automatically passed by pytest
    return request.param  # returns curr parameter value from params
    
def test_num(num):
    assert num in [1, 2, 3]
    
# This will run the test 3 times, once for each parameter
```

---

## Parametrization

* Run the same test with multiple input sets
* Parametrize a test function directly
* Simple data-driven testing, if we have setup logic then fixture params are used

```python
import pytest

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0)
])
def test_add(a, b, expected):
    assert a + b == expected
```

---

## Grouping tests

* Related tests can be grouped together as a class

---

## Skipping Tests

* Tests can be skipped by using ***@pytest.mark.skip,*** don't execute those test functions

---

## Expected Failure

* When a test is known to fail, they can be marked as ***@pytest.mark.xfail,*** pytest will report this differently as ***XFAIL*** (not as a complete failure)

---

## Notes

* *pytest -v* → shows test names and results
* *pytest --maxfail=2* → stops after 2 failures
* *pytest --tb=short* → shorter traceback
* *pytest --html=report.html* → generates HTML report (requires pytest-html)

**Best Practices:**

* Functions should return a value if we need to test them
* Avoid `print()` inside core logic functions. Use `return` instead
* Keep I/O separate from logic
* Keep all test files in a separate folder having `__init__.py` file (even empty) so that Python considers it as a package. By this way all the test files inside a folder can be executed all at once

```
