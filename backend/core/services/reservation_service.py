from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from .. import models

EXPIRY_DAYS = 7


def cleanup_expired_reservations(db: Session):
    now = datetime.utcnow()

    expired = db.query(models.Reservation).filter(
        models.Reservation.expires_at < now
    ).all()

    for res in expired:
        book = db.query(models.Book).filter(models.Book.id == res.book_id).first()
        if book:
            book.available_copies = min(book.total_copies, book.available_copies + 1)
        db.delete(res)

    db.commit()


def get_all_reservations(db: Session):
    cleanup_expired_reservations(db)
    return db.query(models.Reservation).order_by(models.Reservation.id.desc()).all()


def create_reservation(db: Session, book_id: int, user_name: str):
    # STEP 1: Clean expired reservations
    cleanup_expired_reservations(db)

    # STEP 2: Get book
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        return None, "Book not found", 404

    # STEP 3: Check availability
    if book.available_copies <= 0:
        return None, "No copies available", 409

    # STEP 4: Create reservation
    expires_at = datetime.utcnow() + timedelta(days=EXPIRY_DAYS)

    reservation = models.Reservation(
        book_id=book_id,
        user_name=user_name,
        expires_at=expires_at
    )

    # STEP 5: Update copies
    book.available_copies -= 1

    db.add(reservation)
    db.commit()
    db.refresh(reservation)

    return reservation, None, None


def cancel_reservation(db: Session, reservation_id: int):
    reservation = db.query(models.Reservation).filter(
        models.Reservation.id == reservation_id
    ).first()

    if not reservation:
        return "Reservation not found"

    # restore copy ONLY if reservation is still active
    book = db.query(models.Book).filter(models.Book.id == reservation.book_id).first()
    if book:
        if reservation.expires_at > datetime.utcnow():
            book.available_copies = min(book.total_copies, book.available_copies + 1)

    db.delete(reservation)
    db.commit()

    return None
