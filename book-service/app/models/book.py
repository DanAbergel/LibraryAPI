from pydantic import BaseModel

class Book(BaseModel):
    name: str = None
    synopsis: str = None
    price: float = None
    author: str = None
    genre: str = None
    publication_date: str = None
    rating: int = 0

