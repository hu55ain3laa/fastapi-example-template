from typing import Optional
from sqlmodel import Field, SQLModel


class BookBase(SQLModel):
    name: str
    rating: int | None = Field(default=0, gt=0 , lt = 5)
    description: str

class Book(BookBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class BookCreate(BookBase):
    pass

class BookRead(BookBase):
    class Config:
        orm_mode = True

class BookUpdate(SQLModel):
    name: Optional[str] = None
    rating: Optional[int] = None
    description: Optional[str] = None