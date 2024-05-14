from fastapi import APIRouter
from models.book import Book
from schemas.book_schema import list_serializer
from databases.library_db import library
from bson import ObjectId

router = APIRouter()

@router.get('/')
async def get_all_books():
    return list_serializer(library.find())


@router.post('/')
async def add_one_book(book: Book):
    library.insert_one(dict(book))


