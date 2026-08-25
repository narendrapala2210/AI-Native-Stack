class BookNotFoundError(Exception):
    def __init__(self, book_id: int) -> None:
        super().__init__(f"Book with id {book_id} was not found")