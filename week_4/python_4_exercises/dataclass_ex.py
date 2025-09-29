from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    pages: int = 100
    price: float = 99


book_1 = Book("Nothing Lasts Forever", "Sydney Sheldon", 287, 200)
book_2 = Book("Nothing Lasts Forever", "Sydney Sheldon", 287, 200)
book_3 = Book("Agni Siragugal", "APJ Kalam", 326, 399)

print(book_1)
# Book(title='Nothing Lasts Forever', author='Sydney Sheldon', pages=287, price=200)

print(book_1 == book_2)  # True


## Ordering
