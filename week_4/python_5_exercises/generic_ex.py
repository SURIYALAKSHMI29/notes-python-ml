from typing import Generic, List, Sequence, TypeVar

T = TypeVar("T")


# Generic class
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

# stack_int.push("hello")
# this works without errors -> Python is dynamically typed,
# so it doesn't enforce the type 'int' at runtime
# Generic[T] and Stack[int] are only for type hints / static type checking, not for runtime enforcement


# Generic Method
def first_element(seq: Sequence[T]) -> T:
    if len(seq) == 0:
        raise ValueError("Sequence has no elements")
    return seq[0]


elem = first_element([2])
print(elem)
