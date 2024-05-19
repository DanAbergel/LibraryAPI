from fastapi import APIRouter
from models.book import Book
from schemas.book_schema import list_serializer
from databases.books_crud import add_book,remove_book,update_existing_book,get_all_books,get_book

router = APIRouter()

#API GET Method
@router.get('/books')
async def get_books(id:str = None):
    if id:
        books = get_book(id)
    else:
        books = get_all_books()
    if books:
        return list_serializer(books)
    else:
        return {"ERROR","Can't report matching books"}

#API Post Method
@router.post('/books' , response_description="Create a new book description")
async def add_one_book(book: Book):
    """
    Insert a new book record.
    A unique `id` will be created and provided in the response.
    """
    if add_book(book):
        return {"SUCCESS",f"'{book.name}' has been added "}
    else:
        return {"FAILED","Failed to add the new book"}

#API PUT Method
@router.put('/books/{id}', response_model=Book , response_description="Update a variable by ID")
async def update_book(id:str,book:Book):
    """
    Update an existing book record.
    Provide the `id` of the book to be updated along with the updated details in the request body.
    It needs to be updated with an entire document.
    """
    if update_existing_book(id=id , book=book):
        return {"SUCCESS":"Updated successfully!"}
    else:
        return {"FAILED":"Failed to upodate the book!"}


#API DELETE Method
@router.delete('/books/{id}')
async def delete_book(id:str):
    """
    Delete an existing book record.
    Provide the `id` of the book to be deleted.
    """
    if remove_book(id=id):
        return {"SUCCESS":"The book has been removed from the DB!"}
    else:
        return {"FAILED":"Failed to remove the book" }
