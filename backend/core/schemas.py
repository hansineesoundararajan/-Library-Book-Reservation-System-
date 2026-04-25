from pydantic import BaseModel, ConfigDict
from pydantic import Field
from datetime import datetime


class BookCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    title: str = Field(min_length=1, max_length=200)
    author: str = Field(min_length=1, max_length=200)
    total_copies: int = Field(gt=0)


class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    total_copies: int
    available_copies: int

    model_config = ConfigDict(from_attributes=True)


class ReservationCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    user_name: str = Field(min_length=1, max_length=100)


class ReservationResponse(BaseModel):
    id: int
    book_id: int
    user_name: str
    reservation_date: datetime
    expires_at: datetime

    model_config = ConfigDict(from_attributes=True)
