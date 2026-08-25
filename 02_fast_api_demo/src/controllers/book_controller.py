from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from src.database.session import get_db
from src.repositories.book_repository import BookRepository
from src.schemas.book import BookCreate, BookResponse
from src.services.book_service import BookService
from src.utils.exceptions import BookNotFoundError


router = APIRouter(prefix="/books", tags=["Books"])


def get_book_service() -> BookService:
    return BookService(BookRepository())


@router.post("", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(
    book_data: BookCreate,
    db: Session = Depends(get_db),
    service: BookService = Depends(get_book_service),
) -> BookResponse:
    return service.create_book(db, book_data)


@router.get("", response_model=list[BookResponse])
def list_books(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=100),
    db: Session = Depends(get_db),
    service: BookService = Depends(get_book_service),
) -> list[BookResponse]:
    return service.list_books(db, skip, limit)


@router.get("/{book_id}", response_model=BookResponse)
def get_book(
    book_id: int,
    db: Session = Depends(get_db),
    service: BookService = Depends(get_book_service),
) -> BookResponse:
    try:
        return service.get_book(db, book_id)
    except BookNotFoundError as error:
        from fastapi import HTTPException

        raise HTTPException(status_code=404, detail=str(error)) from error


@router.put("/{book_id}", response_model=BookResponse)
def update_book(
    book_id: int,
    book_data: BookCreate,
    db: Session = Depends(get_db),
    service: BookService = Depends(get_book_service),
) -> BookResponse:
    try:
        return service.update_book(db, book_id, book_data)
    except BookNotFoundError as error:
        from fastapi import HTTPException

        raise HTTPException(status_code=404, detail=str(error)) from error


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(
    book_id: int,
    db: Session = Depends(get_db),
    service: BookService = Depends(get_book_service),
) -> None:
    try:
        service.delete_book(db, book_id)
    except BookNotFoundError as error:
        from fastapi import HTTPException

        raise HTTPException(status_code=404, detail=str(error)) from error