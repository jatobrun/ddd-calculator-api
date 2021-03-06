from typing import Optional

from calculator.domain import Operation, OperationRepository
from calculator.application import OperationCommandUseCaseUnitOfWork


class OperationRepositoryImpl(OperationRepository):
    """BookRepositoryImpl implements CRUD operations related Book entity using SQLAlchemy."""

    def __init__(self, session):
        self.session = session

    def find_by_id(self, id: str) -> Optional[Operation]:
        try:
            operation_dto = self.session.query(BookDTO).filter_by(id=id).one()
        except NoResultFound:
            return None
        except:
            raise

        return operation_dto.to_entity()

    def find_by_isbn(self, isbn: str) -> Optional[Book]:
        try:
            book_dto = self.session.query(BookDTO).filter_by(isbn=isbn).one()
        except NoResultFound:
            return None
        except:
            raise

        return book_dto.to_entity()

    def create(self, book: Book):
        book_dto = BookDTO.from_entity(book)
        try:
            self.session.add(book_dto)
        except:
            raise

    def update(self, book: Book):
        book_dto = BookDTO.from_entity(book)
        try:
            _book = self.session.query(BookDTO).filter_by(id=book_dto.id).one()
            _book.title = book_dto.title
            _book.page = book_dto.page
            _book.read_page = book_dto.read_page
            _book.updated_at = book_dto.updated_at
        except:
            raise

    def delete_by_id(self, id: str):
        try:
            self.session.query(BookDTO).filter_by(id=id).delete()
        except:
            raise


class BookCommandUseCaseUnitOfWorkImpl(BookCommandUseCaseUnitOfWork):
    def __init__(
        self,
        session: Session,
        book_repository: BookRepository,
    ):
        self.session: Session = session
        self.book_repository: BookRepository = book_repository

    def begin(self):
        self.session.begin()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()