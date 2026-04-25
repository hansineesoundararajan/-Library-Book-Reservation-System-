from datetime import datetime, timedelta

from core import models
from core.database import SessionLocal


def test_reservation_flow(client):
    book = client.post(
        "/books/",
        json={
            "title": "Reserve Book",
            "author": "Tester",
            "total_copies": 2,
        },
    ).json()

    book_id = book["id"]

    r1 = client.post(f"/books/{book_id}/reserve", json={"user_name": "A"})
    assert r1.status_code == 200

    r2 = client.post(f"/books/{book_id}/reserve", json={"user_name": "B"})
    assert r2.status_code == 200

    r3 = client.post(f"/books/{book_id}/reserve", json={"user_name": "C"})
    assert r3.status_code == 409

    res_id = r1.json()["id"]
    cancel = client.delete(f"/reservations/{res_id}")
    assert cancel.status_code == 200

    r4 = client.post(f"/books/{book_id}/reserve", json={"user_name": "D"})
    assert r4.status_code == 200


def test_reservation_for_missing_book_returns_404(client):
    response = client.post("/books/999/reserve", json={"user_name": "A"})

    assert response.status_code == 404


def test_expired_reservations_free_copies(client):
    book = client.post(
        "/books/",
        json={
            "title": "Old Hold",
            "author": "Tester",
            "total_copies": 1,
        },
    ).json()

    db = SessionLocal()
    try:
        stored_book = db.query(models.Book).filter(models.Book.id == book["id"]).one()
        stored_book.available_copies = 0
        db.add(
            models.Reservation(
                book_id=book["id"],
                user_name="Expired User",
                reservation_date=datetime.utcnow() - timedelta(days=8),
                expires_at=datetime.utcnow() - timedelta(days=1),
            )
        )
        db.commit()
    finally:
        db.close()

    response = client.get(f"/books/{book['id']}")

    assert response.status_code == 200
    assert response.json()["available_copies"] == 1
    assert client.get("/reservations/").json() == []
