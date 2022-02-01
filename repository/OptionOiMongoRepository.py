# importing module
from dataclasses import asdict
from pymongo import MongoClient
from dacite import from_dict
from model.mongo.OptionOiData import OptionOiData

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


    def updateStrikePriceData(self, collection, optionData: OptionOiData):
        for expiryData in optionData.expiryData.values():
            record = self.getRecord(collection=collection, date=expiryData.expiryDate)
            if record == None:
                rec = asdict(expiryData)
                self.addRecord(collection=collection, rec=rec)
            else:
                for strikePrice in record.strikeData.keys():
                    if strikePrice in expiryData.strikeData.keys():
                        for time in expiryData.strikeData[strikePrice].strikePriceHistoricalData.keys():
                            record.strikeData[strikePrice].strikePriceHistoricalData[time] = expiryData.strikeData[strikePrice].strikePriceHistoricalData[time]

                rec = asdict(record)
                self.updateRecord(collection=collection, date=expiryData.expiryDate, rec=rec)


