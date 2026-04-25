from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..services import reservation_service, book_service
from ..schemas import ReservationCreate, ReservationResponse
from .. import schemas
from ..deps import get_db

router = APIRouter()


@router.post("/{book_id}/reserve", response_model=ReservationResponse)
def reserve_book(book_id: int, data: ReservationCreate, db: Session = Depends(get_db)):
    reservation, error, status_code = reservation_service.create_reservation(
        db, book_id, data.user_name
    )

    if error:
        raise HTTPException(status_code=status_code, detail=error)

    return reservation


@router.post("/", response_model=schemas.BookResponse)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return book_service.create_book(
        db,
        title=book.title,
        author=book.author,
        total_copies=book.total_copies
    )


@router.get("/", response_model=list[schemas.BookResponse])
def get_books(db: Session = Depends(get_db)):
    reservation_service.cleanup_expired_reservations(db)
    return book_service.get_all_books(db)


@router.get("/stats")
def get_stats(db: Session = Depends(get_db)):
    # keep cleanup here OR move inside service if you prefer
    reservation_service.cleanup_expired_reservations(db)

    return book_service.get_stats(db)


@router.get("/{book_id}", response_model=schemas.BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    reservation_service.cleanup_expired_reservations(db)
    book = book_service.get_book_by_id(db, book_id)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return book
