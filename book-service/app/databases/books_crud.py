from bson import ObjectId
from .books_db import books_table
from models.book import Book 
from fastapi.encoders import jsonable_encoder

def is_valid_id(id):
    found_book = books_table.find({'_id':ObjectId(id)})
    if not [doc for doc in found_book]:
        print("Given ID does not exists in the DB")
        return False
    return True

def add_book(book:Book):
    try:
        books_table.insert_one(
            dict(book)
        )
    except Exception as e:
        raise Exception("Failed to insert a new book to the DB")
    return True

def remove_book(id:str):
    if is_valid_id(id):
        books_table.delete_one({'_id':ObjectId(id)})
        return True
    return False

def update_existing_book(id:str , book:Book):
    if is_valid_id(id):
        found_book = library.find_one({'_id':ObjectId(id)})
        updated_doc = {key:val if val else found_book.get(key) for key,val in jsonable_encoder(book).items()}
        condition = {'_id':ObjectId(id)}
        operation = {'$set':dict(updated_doc)}
        books_table.update_one(
            filter=condition,
            update=operation               
        )
        return True
    else:
        return False
    
def get_book(id:str):
    if is_valid_id(id):
        return books_table.find({'_id':ObjectId(id)})
    else:
        return None

def get_all_books():
    return books_table.find()