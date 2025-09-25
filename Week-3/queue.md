# Queues in Python
---

# Table of Contents

1. [Queues](#queues)

   - [Deque](#deque)
   - [SimpleQueue](#simplequeue)
   - [queue.Queue](#queuequeue)
   - [queue.LifoQueue](#queuelifoqueue)
   - [queue.PriorityQueue](#queuepriorityqueue)
2. [multiprocessing](#multiprocessing)
3. [asyncio](#asyncio)
4. [heapq](#heapq)


# Queues

- Used for thread-safe(synchronized) communication
- Except SimpleQueue, all are bounded by providing max size

## Deque

- Collections.deque is *thread-safe* double-ended queue designed for fast inserting and removing from both ends
- Bounded → created with a fixed maximum length
- If bounded queue is full, when element is added, it discards an item from the opposite end
- Removing elements from middle in deque is not fast
- `__add__` is not supported, but in-place add `__iadd__` is supported
- Append and popleft
    - In Deque → thread-safe, atomic operations
    - In List → not thread-safe, because these operations may involve multiple steps internally

```python
from collections import deque

dq = deque(maxlen=3)  # max 3 items
dq.extend([1, 2, 3])

dq.append(4)  # Oldest item (1) is automatically discarded
print(dq)     # Output: deque([2, 3, 4], maxlen=3)

dq.appendleft(5)    # deque([5, 2, 3], maxlen=3) -> 4 got discarded

dq.rotate(2)    # deque([2, 3, 5], maxlen=3) -> right rotate

dq.rotate(-2)  # deque([5, 2, 3], maxlen=3) -> left rotate
````

## SimpleQueue

* Unbounded FIFO Queue
* Only supports put(), get(), empty(), qsize()

```python
from queue import SimpleQueue

q = SimpleQueue()

q.put(10)
q.put(20)

print(q.get())  # Output: 10
print(q.get())  # Output: 20

# Check if queue is empty
print(q.empty())  # Output: True
```

## queue.Queue

* Thread-safe **FIFO queue** from the *queue* module.
* Implements locking internally, so multiple threads can safely *put()* and *get()*

```python
import queue

q = queue.Queue()

q.put(10)  # Add item
q.put(20)

print(q.get())  **# Remove first item (10)**
```

## queue.LifoQueue

* **Stack behavior** (Last-In-First-Out)
* Thread-safe like *Queue*; Useful for tasks where you want the most recent item processed first

```python
import queue

stack = queue.LifoQueue()

stack.put(1)
stack.put(2)

print(stack.get())  **# Output: 2**
```

## queue.PriorityQueue

* FIFO with **priority**: lowest valued entries retrieved first
* Thread-safe

```python
import queue

pq = queue.PriorityQueue()

pq.put((2, "task2"))
pq.put((1, "task1"))
pq.put((3, "task3"))

print(pq.get())  **# Output: (1, 'task1')**
```

# multiprocessing

* Queues designed for inter-process communication, not just threads → *process saf*
* Implements own unbounded SimpleQueue and bounded Queue (similar to queue package)
* JoinableQueue is provided for task management (task_done() + join())

# asyncio

* Queues work with async/await for non-blocking task management
* Designed for event loop and coroutines, not threads/processes.
* Provides Queue, LifoQueue, PriorityQueue, and JoinableQueue asynchronously

# heapq

* Does not implement a queue class, but provides functions like *heappush* and *heappop*
* Porvides PrioritQueue operations - smallest first ordering; Treats list as a heap
* No thread/async safe;
