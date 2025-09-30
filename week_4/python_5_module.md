# Python Module: 5

## Exercises

1. **map, reduce, filter**
    1. **map**
    - applies a function to all elements of an iterable
    - returns a *map object*(which is an iterator)
    - *Syntax*
        
        ```python
        map(function, iterable)
        ```
        
    
    **b. reduce** 
    
    - Reduces iterable to a single value using a binary function (takes only 2 inputs at a time)
    - It is defined in “functools” module
    - *Syntax*
        
        ```python
        from functools import reduce
        
        reduce(function, iterable[,initial])
        
        **# initial -> optional
        # A startimg value. If provided, it is used as the first value in the reduction
        # Otherwise first element of the iterable is used**
        ```
        
    
    **c. filter** 
    
    - picks elements where functions returns *True*
    - *Syntax*
        
        ```python
        filter(function, sequence)
        ```
        
2. **First class objects** 
    - Functions are treated as first class objects → they can be used just like numbers, strings, or any other variable
        - Assign functions to a variable
        - Pass them as arguments to other functions → enables higher-order functions
        - Return them from functions
        - Store them in data structures such as lists or directories
3. **Lambda Function**
    - Anonymous, inline, simpler than regular functions
    - Single expression
4. **Higher Order functions**
    - Function that either
        - Takes another function as an argument
        - Returns a function as a result
    - Built-in higher order functions → map, filter, sorted
5. **Decorators** → Functions that modify the behavior of other functions or methods, returning a new function
6. **Generics**
    - Generics are parameterized types → allow a placeholder type that can be filled in later
    - **TypeVar** → used to define generic types; Creates a type variable object
    - **Purpose**:
        - **Type safety:** Catch type mismatches before runtime.
        - **Reusability**: Same class or function works with different types.
        - **Readability:** Code clearly communicates expected types.
    
    ```python
    from typing import Generic, List, Sequence, TypeVar
    
    T = TypeVar("T")
    
    **# Generic class**
    class Stack(Generic[T]):
        def __init__(self):
            self.items: List[T] = []
    
        def push(self, item: T):
            self.items.append(item)
            print(self.items)
    
        def pop(self) -> T:
            return self.items.pop()
    
    stack_int = Stack[int]()  # T is replaced with int
    stack_str = Stack[str]()  # T is replaced with str
    
    stack_int.push("hello")
    **# this works without errors -> Python is dynamically typed,
    # so it doesn't enforce the type 'int' at runtime
    # Generic[T] and Stack[int] are only for type hints / static type checking, not for runtime enforcement**
    
    **# Generic Method**
    def first_element(seq: Sequence[T]) -> T:
        if len(seq) == 0:
            raise ValueError("Sequence has no elements")
        return seq[0]
    elem = first_element([2])
    print(elem) # 2
    ```
    

1. **Overloading**
    - Doesn’t support traditional overloading(same name, different args)
    - Can do operator overloading or default arguments
2. **Script, Module, Package**
    1. **Script**
        - A single python file → executed directly
        - Contains a main block or specific task
        - May or may not be reusable
    2. **Module**
        - Python file that contains functions, classes, or variables
        - Can be imported into other scripts or modules
        - **Reusable\**
    3. **Package**
        - Collections of modules for organized, reusable code
        - Has `__init__`.py → can be empty to used to expose certain functions/classes
