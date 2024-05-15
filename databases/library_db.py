from .settings import uri
from pymongo import MongoClient
import certifi
from models.book import Book
from schemas.book_schema import list_serializer
from fastapi import HTTPException , status
from bson import ObjectId
from fastapi.encoders import jsonable_encoder

client = MongoClient(uri,ssl=True, tlsCAFile=certifi.where())

db = client.library_db

library = db["library_collection"]

def is_valid_id(id):
    found_book = library.find({'_id':ObjectId(id)})
    if not [doc for doc in found_book]:
        print("Given ID does not exists in the DB")
        return False
    return True

def add_book(book:Book):
    try:
        library.insert_one(
            dict(book)
        )
    except Exception as e:
        raise Exception("Failed to insert a new book to the DB")
    return True

def remove_book(id:str):
    if is_valid_id(id):
        library.delete_one({'_id':ObjectId(id)})
        return True
    return False

def update_existing_book(id:str , book:Book):
    if is_valid_id(id):
        found_book = library.find_one({'_id':ObjectId(id)})
        updated_doc = {key:val if val else found_book.get(key) for key,val in jsonable_encoder(book).items()}
        condition = {'_id':ObjectId(id)}
        operation = {'$set':dict(updated_doc)}
        library.update_one(
            filter=condition,
            update=operation               
        )
        return True
    else:
        return False
    
def get_book(id:str):
    if is_valid_id(id):
        return library.find({'_id':ObjectId(id)})
    else:
        return None

def get_all_books():
    return library.find()