from pymongo import MongoClient
import os


class Database:
    def __init__(self):
        self.client = MongoClient(os.environ.get('MONGODB_CONN'))
        #self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client.test
