from typing import List, Iterator as TypingIterator
from abc import ABC, abstractmethod

# Интерфейс Итератора
class Iterator(ABC):
    """Интерфейс для итератора."""

    @abstractmethod
    def __next__(self):
        pass

    @abstractmethod
    def has_next(self):
        pass


# Конкретный Итератор
class BookIterator(Iterator):
    """Конкретный итератор для перебора книг на книжной полке."""

    def __init__(self, books: List[str]):
        self._books = books
        self._index = 0

    def __next__(self):
        if self.has_next():
            book = self._books[self._index]
            self._index += 1
            return book
        else:
            raise StopIteration

    def has_next(self):
        return self._index < len(self._books)


# Интерфейс Iterable
class Iterable(ABC):
    """Интерфейс для итерируемой коллекции."""

    @abstractmethod
    def create_iterator(self) -> Iterator:
        pass


# Конкретная итерируемая коллекция
class Bookshelf(Iterable):
    """Книжная полка, представляющая собой коллекцию книг."""

    def __init__(self):
        self._books = []

    def add_book(self, book: str):
        self._books.append(book)

    def create_iterator(self) -> Iterator:
        return BookIterator(self._books)


# Клиентский код
if __name__ == "__main__":
    bookshelf = Bookshelf()
    bookshelf.add_book("Book 1")
    bookshelf.add_book("Book 2")
    bookshelf.add_book("Book 3")

    iterator = bookshelf.create_iterator()

    while iterator.has_next():
        book = iterator.__next__()
        print(book)
    # Вывод:
    # Book 1
    # Book 2
    # Book 3
