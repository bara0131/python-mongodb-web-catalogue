# Description:  The DTO class connects to and communicates with the MongoDB database.
# Author:       Chloe Lee-Hone
# Date:         14-07-2023
# Course:       CST8276 - Advanced Database Topics

from flask import current_app, g
from flask_pymongo import PyMongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import certifi


class DTO:
    URI = "mongodb+srv://bala0119:Algonquin@cluster0.x3qws2p.mongodb.net/?retryWrites=true"
    DATABASE = "item"
    REVIEW_COLLECTION = "review"
    DESCRIPTION_COLLECTION = "description"

    # Retrieves the database
    @staticmethod
    def get_database():
        # Set the Stable API version when creating a new client
        client = MongoClient(DTO.URI, tlsCAFile=certifi.where(), server_api=ServerApi('1'))

        # Creates the item database
        return client[DTO.DATABASE]

    # Inserts an item in to the description collection
    @staticmethod
    def insert_item(data):
        # insert data in try block
        database = DTO.get_database()

        collection = database[DTO.DESCRIPTION_COLLECTION]
        collection.insert_one(data)

    # Inserts a review to a specific item
    @staticmethod
    def insert_review(data):
        database = DTO.get_database()
        collection = database[DTO.REVIEW_COLLECTION]
        collection.insert_one(data)

    @staticmethod
    def get_all_item_data(self):
        database = DTO.get_database()
        collection = database[DTO.DESCRIPTION_COLLECTION]
        return collection.find({"description": {'$exists': True}})

    @staticmethod
    def get_item_data(self, item_id):
        database = DTO.get_database()
        collection = database[DTO.DESCRIPTION_COLLECTION]
        return collection.find_one({"_id": ObjectId(item_id)})

    @staticmethod
    def get_item_reviews(self, item_id):
        database = DTO.get_database()
        collection = database[DTO.REVIEW_COLLECTION]
        # return collection.find_one({"item_id": {"$eq": ObjectId(item_id)}})
        return collection.find({"item_id": {"$eq": ObjectId(item_id)}})

    @staticmethod
    def get_db(self):
        db = getattr(g, "_database", None)

        if db is None:
            db = g._database = PyMongo(current_app).db

        return db

    @staticmethod
    def insert_item_review(self, item_id):
        database = DTO.get_database()

        collection_name = database[DTO.DESCRIPTION_COLLECTION]
        collection_name.insert_one(item_id)

    # Pings deployment to determine if a connection to the database can be established
    @staticmethod
    def can_connect():
        # Set the Stable API version when creating a new client
        client = MongoClient(DTO.URI, tlsCAFile=certifi.where(), server_api=ServerApi('1'))

        # Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            print("Pinged the deployment. Successfully connected to MongoDB!")

            return True
        except Exception as e:
            print(e)
            return False
