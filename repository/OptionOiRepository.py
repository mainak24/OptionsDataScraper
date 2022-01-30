# importing module
from pymongo import MongoClient
from dacite import from_dict

class OptionOiRepository:

    def __init__(self, url, databaseName):
        self.client = MongoClient(url)
        self.database = self.client[databaseName]

    def addRecord(self, collection, rec):
        mycollection=self.database[collection]
        return mycollection.insert_one(rec)

    def getRecord(self, collection, date):
        mycollection=self.database[collection]
        return mycollection.find({"date": date})

