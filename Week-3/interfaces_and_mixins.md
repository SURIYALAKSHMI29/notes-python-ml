# Python - doesn’t have interfaces and abstract classes by Default

- Python → Intrepreted language
- Compiled languages
    - turns code into machine language
    - At the time of compilation, the compiler checks if the arguments are passed correctly to a function
    - During runtime, nothing needs to be checked again → efficient
- Python uses late binding → when python code is executed, the intrepreter loads all the code but doesn’t do any checks.
- Only while executing the code it checks if the number of arguments is correct, but no type checks are involved
- Python → not strictly typed language, it is duck typed

# Interfaces

- Defines inputs and outputs of a thing and don’t specify the implementation
- Abstract classes → defines inputs and outputs of a thing, and implementation too
- Python doesn’t have an *interface* keyword. Instead python uses *duck typing* and *Abstract Base Classes(ABCs)* to define interfaces
- *@abstractmethod* decorator is used; It prohibits from instantiating that class

```python
from abc import ABC, abstractmethod
class DataStructure(ABC):
	@abstractmethod
	def add(self, item):
		pass
```

- Any subclass must implement ‘*add*’ methods

# Mixins

- Small implementation classes that provide extra functionality to other classes (can be combined)
- Purpose: Reuse code across different classes without creating deep inheritance hierarchies
- Class name usuallt ends with Mixin (not a rule)
- Mixin → has common functionalities → used by other classes
- Example: logging function
    
    ```python
    class LoginMixin:
    	def log(self, msg):
    		print(msg)
    
    class app(LoginMixin):
    	def __init__(self, name):
    		self.name = name
    	def open(self):
    		self.log(f"{self.name} logged")
    		print("opened")
    
    a = app("suriya")
    a.open()
    # output
    # suriya logged
    # opened
    ```
