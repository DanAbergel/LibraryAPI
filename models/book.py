from pydantic import BaseModel
from datetime import datetime
from typing import Annotated

class Book(BaseModel):
    name: str
    synopsis: str
    price: float
    author: str
    genre: str
    publication_date: datetime
    rating: Annotated[int , lambda x : 1 <= x <= 5]
