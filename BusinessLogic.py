# Description:  The BusinessLogic class is a layer between the DTO and the View classes. Any manipulation of data is
#               done here.
# Author:       Chloe Lee-Hone
# Date:         14-07-2023
# Course:       CST8276 - Advanced Database Topics

from bson import ObjectId
from DTO import DTO


class BusinessLogic:

    # The BusinessLogic class uses the DTO class to send requests to the MongoDB database
    db_communicator = DTO

    # Uses the DTO to insert an item
    def insert_item(self, request_data):
        data = request_data.values.dicts[1].to_dict()

        self.db_communicator.insert_item(self.remove_empty_attributes(self, data))

    # Uses the DTO to insert a review
    def insert_review(self, request_data):
        data = request_data.values.dicts[1].to_dict()
        data["item_id"] = ObjectId(data["item_id"])
        data = self.remove_empty_attributes(self, data)

        self.db_communicator.insert_review(self.remove_empty_attributes(self, data))

    # Uses the DTO to get all items from the database
    def retrieve_all_item_data(self):
        return self.db_communicator.get_all_item_data(self)

    # Uses the DTO to get a specific item using its unique database id (_id)
    def get_item_data(self, item_id):
        return self.db_communicator.get_item_data(self, item_id)

    # Uses the DTO to insert a review for a specific item using its database id (_id)
    def insert_item_review(self, item_id):
        return self.db_communicator.insert_item_review(self, item_id)

    def get_item_reviews(self, item_id):
        return self.db_communicator.get_item_reviews(self, item_id)

    # Remove keys where values are empty or null. This demonstrates the flexibility of NoSQL; In a relational
    # database, these items would need to be stored with a NULL value. In a NoSQL database, we do not need to store
    # attributes that do not describe or apply to a particular item
    @staticmethod
    def remove_empty_attributes(self, data):
        for key, value in list(data.items()):
            if value == "" or value is None:
                data.pop(key)

        return data
