from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.book import Book
from src.schemas.book import BookCreate


class BookRepository:
    def create(self, db: Session, book_data: BookCreate) -> Book:
        book = Book(**book_data.model_dump())
        db.add(book)
        db.commit()
        db.refresh(book)
        return book

    def list(self, db: Session, skip: int = 0, limit: int = 100) -> list[Book]:
        statement = select(Book).offset(skip).limit(limit).order_by(Book.id)
        return list(db.scalars(statement).all())

    def get_by_id(self, db: Session, book_id: int) -> Book | None:
        return db.get(Book, book_id)

    def update(self, db: Session, book: Book, book_data: BookCreate) -> Book:
        for field, value in book_data.model_dump().items():
            setattr(book, field, value)
        db.commit()
        db.refresh(book)
        return book

    def delete(self, db: Session, book: Book) -> None:
        db.delete(book)
        db.commit()