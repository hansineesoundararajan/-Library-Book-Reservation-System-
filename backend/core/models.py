from sqlalchemy import CheckConstraint, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from datetime import datetime

from .database import Base


class Book(Base):
    __tablename__ = "books"
    __table_args__ = (
        CheckConstraint("total_copies > 0", name="ck_books_total_copies_positive"),
        CheckConstraint("available_copies >= 0", name="ck_books_available_non_negative"),
        CheckConstraint(
            "available_copies <= total_copies",
            name="ck_books_available_not_above_total",
        ),
    )

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    total_copies = Column(Integer, nullable=False)
    available_copies = Column(Integer, nullable=False)

    reservations = relationship("Reservation", back_populates="book", cascade="all, delete")


class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id", ondelete="CASCADE"), nullable=False)
    user_name = Column(String, nullable=False)

    reservation_date = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime, nullable=False)

    book = relationship("Book", back_populates="reservations")
