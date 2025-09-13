# **tmux (Terminal Multiplexer)**

- Split one terminal into multiple panes  
- Multiple terminal splits inside a window  
- Sessions run in the background → can detach & reattach  

**Basic tmux commands:**

- Start session: `tmux` or `tmux new -S mysession`  
- Detach: `Ctrl+b d`  
- List sessions: `tmux ls`  
- Reattach: `tmux attach -t mysession`  
- Kill: `exit` or `Ctrl+D` (current pane) / `tmux kill-session -t mysession` (session)  

**Pane management:**

- Create pane vertically: `Ctrl+b %`  
- Create pane horizontally: `Ctrl+b "`  
- Switch panes: `Ctrl+b` + arrows  
- New window: `Ctrl+b c`  
- Next window: `Ctrl+b n`  
- Previous window: `Ctrl+b p`  
- Rename window: `Ctrl+b ,` (or `Ctrl+b` + new window name)  
- Rename session:  
  - Within session: `Ctrl+b &` → type new name  
  - Outside session: `tmux rename-session -t oldname newname`  

---

# **Virtual Environment**

- An isolated environment on the computer where you can run and test Python projects  
- Allows managing project-specific dependencies without interfering with others  
- Each environment has its own Python interpreter, installed packages, and settings  

### **Importance**
- Prevents package version conflicts  
- Makes projects portable and reproducible  
- Allows testing with different Python versions  

**Options:** create, activate, deactivate, delete  

---

# **Virtualenv**

**Overview**
- Third-party package for creating isolated Python environments  
- Works with older Python versions  
- Provides extra features compared to `venv`  

**Creating a Virtual Environment**
- Using venv: `python -m venv projectName`  
- Using virtualenv: `virtualenv projectName` (install `virtualenv` first)  

**Activating / Deactivating / Deleting**
- Activate: `source projectName/bin/activate`  
- Deactivate: `deactivate`  
- Delete: `rm -rf projectName`  

---

# **PIP (Python Install Package)**

**Overview**
- Package manager for Python packages  
- Contains all files needed for a module  

**Module:** single Python `.py` file that can be reused  
**Package:** collection of modules in a folder (with `__init__.py`)  

**Common Commands**
- `pip list` → show installed packages  
- `pip install packageName` → install package  
- `pip uninstall packageName` → remove package  

---

# **Python Package Index (PyPI)**

- Default repository for pip packages  
- Can also install from GitHub or other sources  

**Installing Multiple Packages**
- `pip install -r requirements.txt`  
- Example `requirements.txt`:  
  ```txt
  numpy==1.23
  pandas==1.5.3

# **Python Requirements File**

**Create requirements file:**
```bash
pip freeze > requirements.txt
```

--
Here’s your content properly formatted as a clean Markdown (`.md`) file:

```markdown
# **Package Manager Overview**

Tools that download, install, update, and manage software packages.

---

## **Examples**

- **Python:** pip  
- **JavaScript:** npm, yarn  
- **Java:** Maven, Gradle  

---

## **Repositories**

- **Python:** PyPI, Anaconda, GitHub  
- **Java:** Maven Central  
- **JavaScript:** npm registry  

---

## **Python Package Structure**

```

my-project/               # root folder
  my-package/           # actual Python package folder
    **init**.py
    greetings.py
  setup.py              # metadata and install instructions
  README.md
  requirements.txt      # optional dependencies

````

**Nested Packages Purpose:**

- Avoid naming conflicts in `site-packages`  
- `__init__.py` → marks folder as a package  
- `setup.py` → defines metadata (name, version, dependencies, etc.)  

**Example :**
```python
import from my_package import requests
````

# **Installing Packages**

* Using `requirements.txt`:

```bash
pip install -r requirements.txt
```

* Using `setup.py`:

```bash
pip install .
```

(dot = current directory)

* Editable install (during development):

```bash
pip install -e .
```

* Creates link to development directory
* Changes in source code reflected immediately

**When to Use:**

* `requirements.txt` → shared environments
* `setup.py` → distribution of packages

**Fix pip issues:**

```bash
python -m ensurepip --upgrade
# Or
get-pip.py
```

---

# **Distribution Formats**

* **Wheel (.whl):** pre-built, fast install
* **Source Distribution (.tar.gz, .zip):** build & install from source
* **Egg (.egg):** older, mostly deprecated

---

# **Dependency Conflicts**

**Example:**

* Package A → needs C >= 2.30
* Package B → needs C < 2.15
* Conflict: only one version of C can be installed

**Resolution:**

* Use different virtual environments
* Upgrade/downgrade versions
* Use tools like poetry, pipenv, conda

---

# **Conda**

* Open-source package & environment manager
* Installs Python + non-Python dependencies
* Good for ML, data science, and scientific computing

**Anaconda vs Miniconda:**

* Anaconda → large, preinstalled packages
* Miniconda → minimal, lightweight

**Common Conda Commands:**

* **Create environment:**

```bash
conda create --name myenv python=3.x
```

* **Activate environment:**

```bash
conda activate myenv
```

* **Set environment variables:**

```bash
conda env config vars set varName=varValue
```

* **Deactivate environment:**

```bash
conda deactivate
```

* **Install package:**

```bash
conda install packageName
```

(Fallback: use `pip install` inside the environment if package not found in conda repos)

* **List installed packages:**

```bash
conda list
```

* **Export environment:**

```bash
conda env export > environment.yml
```

* **Remove package:**

```bash
conda remove packageName
```

* **Remove environment:**

```bash
conda remove --name envName --all
```

* **Update conda:**

```bash
conda update conda
```


