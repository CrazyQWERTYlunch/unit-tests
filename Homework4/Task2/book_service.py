from Homework4.Task2.book import Book
from Homework4.Task2.book_repository import BookRepository


class BookService:
    def __init__(self, book_repository: BookRepository):
        self._book_repository = book_repository

    @property
    def book_repository(self):
        return self._book_repository

    def find_by_id(self, book_id: int) -> Book:
        return self._book_repository.find_by_id(book_id)

    def find_all(self) -> list[Book]:
        return self._book_repository.find_all()