from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..deps import get_db
from .. import schemas
from ..services import reservation_service

router = APIRouter()


@router.get("/", response_model=list[schemas.ReservationResponse])
def get_reservations(db: Session = Depends(get_db)):
    return reservation_service.get_all_reservations(db)


@router.delete("/{reservation_id}")
def cancel_reservation(reservation_id: int, db: Session = Depends(get_db)):
    error = reservation_service.cancel_reservation(db, reservation_id)

    if error:
        raise HTTPException(status_code=404, detail=error)

    return {"message": "Reservation cancelled"}
