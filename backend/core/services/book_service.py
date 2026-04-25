from sqlalchemy.orm import Session
from .. import models


def create_book(db: Session, title: str, author: str, total_copies: int):
    book = models.Book(
        title=title,
        author=author,
        total_copies=total_copies,
        available_copies=total_copies
    )

    db.add(book)
    db.commit()
    db.refresh(book)

    return book


def get_all_books(db: Session):
    return db.query(models.Book).all()


def get_book_by_id(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def get_stats(db: Session):
    total_books = db.query(models.Book).count()
    total_reservations = db.query(models.Reservation).count()

    available = db.query(models.Book).with_entities(models.Book.available_copies).all()
    total_available = sum([a[0] for a in available])

    return {
        "total_books": total_books,
        "total_reservations": total_reservations,
        "available_copies": total_available
    }