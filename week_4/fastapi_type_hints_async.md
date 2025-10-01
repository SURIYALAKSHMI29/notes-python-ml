# Python Type Hints, Pydantic, and Asynchronous Programming in FastAPI

## Table of Contents

1. [Python Types](#python-types)
2. [Pydantic Models](#pydantic-models)
3. [Annotated / Metadata in Type Hints](#annotated--metadata-in-type-hints)
4. [Type Hints in FastAPI](#type-hints-in-fastapi)
5. [Coroutines](#coroutines)
6. [Async / Await Coroutine](#async--await-coroutine)
7. [Event Loop vs Thread Pool](#event-loop-vs-thread-pool)
8. [Dependencies (Depends)](#dependencies-depends)
9. [Background Tasks](#background-tasks)

---

# Python types

- **Type Hints →** special syntax that allow declaring the type of a variable
- Declare type hints as function parameters
- **Simple types →** can annotate parameters with built-in types like str, int, float, bool, bytes.
- **Generic / container types →** For more complex data structures, can use generic types from typing (or built-ins in newer Python):
    - *list[str], tuple[int, str], set[bytes]*
    - *dict[str, float]* specifying key and value types
    
    ```python
    def process_items(items_t: tuple[int, int, str], items_s: set[bytes]):
    	return items_t, items_s     
    **# items_t -> tuple of 3 items, first item - int, second item - int, third - str** 
    ```
    
- **Union / Optional / None →** variable may have one of multiple types
    - *Union[int, str],* similar to *int | str (python 3.10+)*
    - *Optional[str]* (equivalent to Union[str, None])
    - *Union* and *Optional* are imported from *typing* module
- **Classes / custom types →** can use classes as types

## **Pydantic models**

- A python library to perform data validation
- Shape of the data is declared as classes with attributes. Each attribute has a type, and Pydantic will validate and convert the input data automatically
- Automatically generates `__init__(), __repr__(), __eq__()` methods
- Accepts only kwargs (not positional) for initialization
- FastAPI builds on Pydantic

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str = "Guest"

new_user = User(id="101", name="Suriya")
print(new_user)  **# id=101 name='Suriya'**
```

## **Annotated / metadata in type hints**

- Python’s Annotated type (from typing or typing_extensions) lets to attach extra metadata to a type hint
- FastAPI takes advantage of **Annotated** to:
    - Add validation rules
    - Describe parameters in docs
    - Control request parsing

```python
from fastapi import Query
from typing import Annotated

# **field: Annotated[BaseType, ExtraMetadata]**
q: Annotated[str | None, Query(min_length=3, max_length=50)] = None

**# type -> str | None
# Metadata -> Query(min_length=3, max_length=50)**
```

## Type hints in FastAPI

- Define requirements from request path params, query params, headers, bodies, dependencies
- Convert data from the request to the required type
- Validate the incoming data from request by generating automatic errors returned to the client when the data is invalid
- Document the API using OpenAI → used by the automatic interactive documentation user interfaces


# Coroutines

- A coroutine is like a generator but can consume and produce values.
- It can pause execution (like *yield*) and resume later, making it ideal for general cooperative multitasking, asynchronous programming, or pipelines.
- Defined with a *def* function containing *yield* (or async *def* + await for modern async)
- Can send values into a coroutine using .*send()* and it resumes from where it paused
- When we call coroutine nothing happens, it runs only in response to the *next()* and *send()* method
- Coroutines → manual(*yield)* pause **where in Async / Await Coroutine → automatic pause (await)
- Coroutines → *.send()*  resumes where in Async / Await Coroutine → *await* finishes the task
- **def runs in threadpool; async/await runs in event loop**

# Async / Await Coroutine

- Web apps often wait for I/O bound operations(DB, Network files)
- Using *async* lets the server handle other requests while waiting → improves performance
- FastAPI is built on *Starlette* → which is async-ready
- Can mix async + sync functions; FastAPI handles them automatically
- **async def → coroutine**; Only inside *async def,* can use *await*
- *async makes a function asynchronous*
    - When you define a function with async def, it becomes a coroutine.
    - A coroutine doesn’t run immediately; it returns a coroutine object that can be awaited.
    - It allows Python to pause and switch to other tasks while waiting for I/O instead of blocking the whole program.
- *await actually pauses execution*
    - Inside an async def function, await is used on another coroutine or async task.
    - When Python hits await some_task():
        - The function pauses at that line.
        - Control goes back to the event loop, which can run other coroutines.
        - Once some_task finishes, execution resumes from that await line.
- Starlette(and FastAPI) are based on *AnyIO* → compatible with both python’s standard library *asyncio* and *Trio*

> functions with **async def** can only be called inside of functions defined with **async def** too.
> 

# Event Loop vs Thread Pool

### Event Loop

- Runs *async def* functions (coroutines).
- Can pause at *await* and run other tasks while waiting.
- Useful for I/O-bound operations (DB, network, files).

### Thread Pool

- Runs normal *def* functions for path operations or dependencies.
- Blocking code runs in a separate thread → server doesn’t get blocked.
- Useful for blocking CPU or I/O tasks.

## FastAPI automatically:

- Runs *async def* → event loop
- Runs *def* → thread pool

> Event loop → single-threaded, non-blocking
Thread pool → multi-threaded, handles blocking functions
> 

# Dependencies (Depends)

- Reuse code across multiple endpoints → like authentication, database connections
- Define a function that returns something (session, object, variable,..) → and FastAPI will inject it into the endpoint automatically

```python
from fastapi import Depends, FastAPI

app = FastAPI()
current_user = "Guest"

def get_current_user():
    return current_user

@app.get("/profile")
def read_profile(user: str = Depends(get_current_user)):
    return {"User": user}
    
**# Note : function name is given (without calling it)**
```

# Background tasks

- Run tasks that take time without delaying the API response
- API responds immediately, task is executed after the response in background

```python
@app.post("/send")
def send_notification(email: str, background_tasks: BackgroundTasks):
    **# add task to background**
    background_tasks.add_task(send_email, email)
    ...
```
