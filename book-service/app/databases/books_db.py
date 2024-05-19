from .settings import uri
from pymongo import MongoClient
import certifi


client = MongoClient(uri,ssl=True, tlsCAFile=certifi.where())

db = client.library_db

books_table = db["books_collection"]

