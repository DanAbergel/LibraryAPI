from .settings import uri
from pymongo import MongoClient
import certifi

client = MongoClient(uri,ssl=True, tlsCAFile=certifi.where())

db = client.library_db

library = db["library_collection"]