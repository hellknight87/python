import pymongo
from pymongo import MongoClient
client = MongoClient()
client = MongoClient('mongodb://localhost:27017/')
db = client.pytests
