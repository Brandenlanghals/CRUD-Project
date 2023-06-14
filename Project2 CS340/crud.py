from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter:
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self, username, password):
        
        if username and password:
            self.client = MongoClient('mongodb://%s:%s@nv-desktop-services.apporto.com:31444' % (username, password))
            self.database = self.client['AAC']
            self.collection = self.database['animals']
    
    

    def create(self, data):
        """Inserts a document into the specified MongoDB database and collection"""
        if data:
            result = self.collection.insert_one(data)
            return result.inserted_id is not None
        else:
            raise ValueError("Nothing to save because data parameter is empty")

    def read(self, query):
        """Queries for documents from the specified MongoDB database and collection"""
        result = self.collection.find(query)
        if result:
            return list(result)
        else:
            return []

    def update(self, query, update_data):
        """Queries for and changes document(s) from the specified MongoDB database and collection"""
        result = self.collection.update_many(query, {"$set": update_data})
        return result.modified_count

    def delete(self, query):
        """Queries for and removes document(s) from the specified MongoDB database and collection"""
        result = self.collection.delete_many(query)
        return result.deleted_count
