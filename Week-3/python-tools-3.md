---

# Table of Contents

* [Pytest](#pytest)
* [Pylint](#pylint)
* [DVC](#dvc)

---

# Pytest

- Run all the test methods and shows failed methods
- Didn’t stops execution when an error is encountered, checks the next function

## Testing

- **Unit test:**
    - Tests small piece of code to ensure implementation correctness
    - Example: Checking whether add function is working fine as expected under all conditions
- **Behaviour Test**
    - Integration or functional test
    - Tests user-facing functionality
    - Example: For a chatbot, checking whether it responses as expected

### To run in terminal :

- *pytest file_name* - tests the given file
- *pytest -v* → runs all the test files in the cwd in verbose mode

### To Save as reports

```python
pytest -v --junitxml=report.xml     # XML report (CI/CD use)
pytest -v --html=report.html --self-contained-html   # Requires pytest-html
```

- **JUnit format:** Standard format many CI/CD tools understand
- **self-contained-html:** the report has all CSS/JS embedded inside the html file

## Conftest.py

- A special file that has shared fixtures/config
- No need to import manually, pytest automatically finds it

## Mock Objects

- Used for Simulating the external dependencies(API, DB, etc)
- ***Mock()*** - returns a fake object that can pretend to have any methods or attributes we need
- We can pre-define the return values of the methods going to get tested
    - Example
    
    ```python
    mock_api = Mock()
    mock_api.get.return_value = {"result": "success"}
    ```
    
    - When mock_api.get() is called, it returns the defined values

```python
from unittest.mock import Mock
	
def fetch_data(api):
	return api.get("url")

def test_fetch_data():
	mock_api = Mock()
	mock_api.get.return_value = {"result": "success"}
	assert fetch_data(mock_api) == {"result": "success"}
```

## Catch Raised Exceptions

- To test whether the exceptions are raised correctly in our code,
    
    ```python
    with pytest.raises(Exception):
    	    # code
    ```
    
    - If error occurs as expected, then test case is passed, else fails

# Pylint

## Linting / Static code analysis

- Checking the code without running it, for error like syntax errors, code style, potential bugs
- **Warning types:**
    - **C** = convention (style issue)
    - **W** = warning
    - **E** = error
    - **R** = refactor suggestion
- ***pylint filename -*** used to run pylint

### Skip / ignore an error

- To skip an error(s) in a file, we can add a comment line as
    
    ```python
    def divide_numbers(a, b):
    		x = 10        **# pylint: disable=invalid-name, unused-variable**
        return a / b  **# pylint: disable=zero-division**
    ```
    

### Skip a file from being checked

- By adding ***# pylint: skip-file*** at the top of the file

## pylintrc file

- Configuration file for Pylint
- Can define rules, ignores, formatting, error levels, naming conventions
- example:
    
    ```python
    [MASTER]
    ignore=tests,migrations   # files/folders to skip
    load-plugins=
    
    [MESSAGES CONTROL]
    disable=C0114,C0115,C0116  # disable specific warnings
    
    [REPORTS]
    output-format=colorized
    
    [FORMAT]
    max-line-length=100
    
    ```
    
- To create a pylintrc
    
    ```python
    pylint --generate-rcfile > pylintrc 
    ```
    

# DVC

- Data Version Control - open source command-line tool, that extends Git’s capabilities to handle large datasets, models and pipelines
- **It stores them in external storage(like cloud services) while keeping lightweight references in Git**
- Version Control system - manage changes to source code;
- Data Version Control - manage changes to models and datasets

## Basic Commands

### **Initialization**

```bash
dvc init          # Initialize DVC in project
git commit -m "Initialize DVC"
```

### **Add a dataset**

```bash
dvc add data/raw_data.csv
**# Updates .gitignore automatically**

git add data/raw_data.csv.dvc .gitignore
git commit -m "Add raw data tracked by DVC"
```

### **Configure remote storage**

```bash
dvc remote add -d myremote s3://mybucket/myfolder
```

### **Push and pull data**

```bash
dvc push          # Upload data to remote
dvc pull          # Download data from remote
```

- DVC automatically adds large files (datasets/models) to .gitignore
- **Git tracks only the .dvc pointer file and .gitignore**
- Ensures large files are not committed to Git, keeping repo lightweight

## Pipeline

- the sequence of stages / steps that transform the raw data into final results, with DVC tracking dependencies, outputs and commands
- Pipelines are reproducible, automatic and consistent
    - Dependency tracking
    - recomputes automatically if input changes
- **Stage:** one step in a data or ML workflow
    - Each stage has three key components:
        1. Command - what to run
        2. Dependencies - input files or scripts required
        3. Outputs - files or datasets generated
    - Stages are recorded in dvc.yaml, which defines the pipeline of the project

- **example**:
    
    ```python
    dvc run -n preprocess -d data/raw_data.csv -o data/processed.csv python preprocess.py
    ```
    
    - dvc run - create a stage in a pipeline
    - -n preprocess
        - -n or —name → name of the stage
        - here, stage name is preprocess
    - -d data/raw_data.csv
        - - d or —deps → dependencies of the stage
        - DVC tracks the files, whenever the dependency changes, DVC re-run this stage
    - -o data/processed.csv
        - -o or —outs → outputs of the stage
        - DVC tracks these file after the command runs
        - Outputs are stored in DVC cache and linked to Git via .dvc files
    - Finally cmd to get executed when dependencies changes
    - .dvc file - pointer file. It contains
        - Hash of the output
        - Path to the file
        - Metadata needed to retrieve it from cache or remote
    - .gitignore is updated to ignore processed.csv
    
- **Share Pipeline + Data**
    
    ```bash
    git push
    dvc push
    ```
    
    - Git tracks *.dvc* pointer files and *.gitignore*
    - DVC pushes large data/model files to remote storage
