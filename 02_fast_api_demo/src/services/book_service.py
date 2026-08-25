from sqlalchemy.orm import Session

from src.models.book import Book
from src.repositories.book_repository import BookRepository
from src.schemas.book import BookCreate
from src.utils.exceptions import BookNotFoundError


class BookService:
    def __init__(self, repository: BookRepository) -> None:
        self.repository = repository

    def create_book(self, db: Session, book_data: BookCreate) -> Book:
        return self.repository.create(db, book_data)

    def list_books(self, db: Session, skip: int, limit: int) -> list[Book]:
        return self.repository.list(db, skip, limit)

    def get_book(self, db: Session, book_id: int) -> Book:
        book = self.repository.get_by_id(db, book_id)
        if book is None:
            raise BookNotFoundError(book_id)
        return book

    def update_book(self, db: Session, book_id: int, book_data: BookCreate) -> Book:
        book = self.get_book(db, book_id)
        return self.repository.update(db, book, book_data)

    def delete_book(self, db: Session, book_id: int) -> None:
        book = self.get_book(db, book_id)
        self.repository.delete(db, book)