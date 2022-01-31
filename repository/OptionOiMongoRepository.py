# importing module
from dataclasses import asdict
from pymongo import MongoClient
from dacite import from_dict

from model.mongo.OptionOiExpiryData import OptionOiExpiryData

class OptionOiMongoRepository:

    def __init__(self, url, databaseName):
        self.client = MongoClient(url)
        self.database = self.client[databaseName]

    def addRecord(self, collection, rec):
        mycollection=self.database[collection]
        return mycollection.insert_one(rec)

    def addRecords(self, collection, rec):
        mycollection=self.database[collection]
        return mycollection.insert_many(rec)

    def updateRecord(self, collection, date, rec):
        mycollection=self.database[collection]
        return mycollection.update_one({"expiryDate": date}, {"$set":rec})

    def getRecord(self, collection, date) -> OptionOiExpiryData:
        mycollection=self.database[collection]
        record = mycollection.find_one({"expiryDate": date})
        if record != None:
            objectData = from_dict(data_class=OptionOiExpiryData, data=record)
            return objectData
        
        return None


    def updateStrikePriceData(self, collection, expiryDataList: list[OptionOiExpiryData]):
        for expiryData in expiryDataList:
            record = self.getRecord(collection=collection, date=expiryData.expiryDate)
            if record == None:
                self.addRecord(collection=collection, rec=asdict(expiryData))
            else:
                if record.callStrikeData != None:
                    for strikePrice in record.callStrikeData.keys():
                        if strikePrice in expiryData.callStrikeData.keys():
                            record.callStrikeData[strikePrice].strikePriceData.extend(expiryData.callStrikeData[strikePrice].strikePriceData)
                else:
                    record.callStrikeData = expiryData.callStrikeData.copy()

                if record.putStrikeData != None:
                    for strikePrice in record.putStrikeData.keys():
                        if strikePrice in expiryData.putStrikeData.keys():
                            record.putStrikeData[strikePrice].strikePriceData.extend(expiryData.putStrikeData[strikePrice].strikePriceData)
                else:
                    record.putStrikeData = expiryData.putStrikeData.copy()

                self.updateRecord(collection=collection, date=expiryData.expiryDate, rec=asdict(record))


