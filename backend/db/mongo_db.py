from pymongo import MongoClient
from typing import List, Dict

class MongoDBHelper:
    """
    A helper class for MongoDB operations.
    """
    def __init__(self, db_uri: str, db_name: str, collection_name: str):
        self.client = MongoClient(db_uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_one(self, document: Dict) -> None:
        """Inserts a single document into the collection."""
        self.collection.insert_one(document)

    def find(self, query: Dict = {}) -> List[Dict]:
        """Finds documents matching the query."""
        return list(self.collection.find(query, {'_id': 0}))

    def update_one(self, query: Dict, update: Dict) -> None:
        """Updates a single document matching the query."""
        self.collection.update_one(query, {'$set': update})

    def delete_one(self, query: Dict) -> None:
        """Deletes a single document matching the query."""
        self.collection.delete_one(query)
