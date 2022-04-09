from typing import List


class Book:
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return f"Book {self.name}"


class BookShelf:
    def __init__(self, *books: List[Book]):
        self.books = books

    def __str__(self) -> str:
        return f"Bookshelf with {len(self.books)} books."


book = Book("Harry Potter")
book2 = Book("Python 101")

shelf = BookShelf(book, book2)

print(shelf)
