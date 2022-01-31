import time
from repository.NseOptionDataService import NseOptionDataService
from model.mongo.OptionOiExpiryData import OptionOiExpiryData
from model.mongo.OptionOiStrikeData import OptionOiStrikeData
from model.mongo.OptionOiStrikePriceData import OptionOiStrikePriceData


class OptionOiConvertRawDataService:

    def getOptionExpiryData(self, symbol) -> list[OptionOiExpiryData]:
        nseDataService = NseOptionDataService()
        timeStamp = time.time()
        outputExpiryData = []
        optionRawData = nseDataService.getOptionChainData(symbol)

        # print(optionRawData.data)

        for expiryDate in optionRawData.expiryDates:
            optionExpiryData = OptionOiExpiryData(expiryDate=expiryDate, callStrikeData={}, putStrikeData={})
            for data in optionRawData.data:
                if expiryDate != data.expiryDate:
                    continue
                
                if data.CE != None:
                    optionStrikeCallData = OptionOiStrikeData(strikePrice = data.strikePrice, strikePriceData=[])
                    optionStrikePriceCallData = OptionOiStrikePriceData(
                        time = timeStamp,
                        openInterest=data.CE.openInterest,
                        totalTradedVolume=data.CE.totalTradedVolume,
                        impliedVolatility=data.CE.impliedVolatility,
                        totalBuyQuantity=data.CE.totalBuyQuantity,
                        totalSellQuantity=data.CE.totalSellQuantity,
                        bidQty=data.CE.bidQty,
                        bidprice=data.CE.bidprice,
                        askQty=data.CE.askQty,
                        askPrice=data.CE.askPrice,
                        underlyingValue=data.CE.underlyingValue
                    )
                    optionStrikeCallData.strikePriceData = [optionStrikePriceCallData]
                    optionExpiryData.callStrikeData[str(data.CE.strikePrice)] = optionStrikeCallData

                if data.PE != None:
                    optionStrikePutData = OptionOiStrikeData(strikePrice = data.strikePrice, strikePriceData=[])
                    optionStrikePricePutData = OptionOiStrikePriceData(
                        time = timeStamp,
                        openInterest=data.PE.openInterest,
                        totalTradedVolume=data.PE.totalTradedVolume,
                        impliedVolatility=data.PE.impliedVolatility,
                        totalBuyQuantity=data.PE.totalBuyQuantity,
                        totalSellQuantity=data.PE.totalSellQuantity,
                        bidQty=data.PE.bidQty,
                        bidprice=data.PE.bidprice,
                        askQty=data.PE.askQty,
                        askPrice=data.PE.askPrice,
                        underlyingValue=data.PE.underlyingValue
                    )
                    optionStrikePutData.strikePriceData = [optionStrikePricePutData]
                    optionExpiryData.putStrikeData[str(data.PE.strikePrice)] = optionStrikePutData

            outputExpiryData.append(optionExpiryData)


        return outputExpiryData