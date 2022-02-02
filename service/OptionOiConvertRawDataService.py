from dataclasses import asdict
from datetime import datetime
import json
from constants.GlobalConstants import GlobalConstants
from repository.OpstraOptionDataRepository import OpstraOptionDataRepository
from model.DataSourceEnum import DataSourceEnum
from model.mongo.OptionOiData import OptionOiData
from model.nse.OptionStrikePriceNseRawData import OptionStrikePriceNseRawData
from repository.NseOptionDataRepository import NseOptionDataRepository
from model.mongo.OptionOiExpiryData import OptionOiExpiryData
from model.mongo.OptionOiStrikeData import OptionOiStrikeData
from model.mongo.OptionOiStrikePriceData import OptionOiStrikePriceData


class OptionOiConvertRawDataService:

    def fetchDataForMongo(self, source, symbol) -> OptionOiData:
        output = None
        if source == DataSourceEnum.NSE.value:
            output = self.__convertNseOptionData(symbol)
        elif source == DataSourceEnum.OPSTRA.value:
            output = self.__convertOpstraOptionData(symbol)
            
        return output

    def __convertNseOptionData(self, symbol) -> OptionOiData:
        output = OptionOiData(underlying = symbol, expiryData = {})
        nseDataRepository = NseOptionDataRepository()
        currentTime = datetime.now().strftime("%D - %H:%M:%S")
        count = 0
        optionRawData = None
        while optionRawData == None and count < GlobalConstants.MAX_RETRY.value:
            optionRawData = nseDataRepository.getOptionChainData(symbol)

        for expiryDate in optionRawData.expiryDates:
            expiryDate = expiryDate.replace("-", "", -1)
            optionExpiryData = OptionOiExpiryData(expiryDate=expiryDate, strikeData={})
            for data in optionRawData.data:
                if expiryDate != data.expiryDate:
                    continue
                
                if data.CE == None:
                    data.CE = OptionStrikePriceNseRawData(
                        strikePrice = 0,
                        expiryDate = expiryDate,
                        underlying = data.PE.underlying,
                        identifier = data.PE.identifier,
                        openInterest = 0,
                        changeinOpenInterest = 0,
                        pchangeinOpenInterest = 0,
                        totalTradedVolume = 0,
                        impliedVolatility = 0.0,
                        lastPrice = 0,
                        change = 0,
                        pChange = 0,
                        totalBuyQuantity = 0,
                        totalSellQuantity = 0,
                        bidQty = 0,
                        bidprice = 0,
                        askQty = 0,
                        askPrice = 0.0,
                        underlyingValue = data.PE.underlyingValue
                    )
                
                if data.PE == None:
                    data.PE = OptionStrikePriceNseRawData(
                        strikePrice = 0,
                        expiryDate = expiryDate,
                        underlying = data.CE.underlying,
                        identifier = data.CE.identifier,
                        openInterest = 0,
                        changeinOpenInterest = 0,
                        pchangeinOpenInterest = 0,
                        totalTradedVolume = 0,
                        impliedVolatility = 0.0,
                        lastPrice = 0,
                        change = 0,
                        pChange = 0,
                        totalBuyQuantity = 0,
                        totalSellQuantity = 0,
                        bidQty = 0,
                        bidprice = 0,
                        askQty = 0,
                        askPrice = 0.0,
                        underlyingValue = data.CE.underlyingValue
                    )

                optionStrikeData = OptionOiStrikeData(strikePrice = data.strikePrice, strikePriceHistoricalData={})
                optionStrikePriceData = OptionOiStrikePriceData(
                    time = currentTime,
                    CITMP = 0.0,
                    CallChng = data.CE.change,
                    CallDelta = 0.0,
                    CallGamma = 0.0,
                    CallIV = data.CE.impliedVolatility,
                    CallLTP = 0.0,
                    CallOI = data.CE.openInterest,
                    CallOIChng = data.CE.changeinOpenInterest,
                    CallTheta = 0.0,
                    CallVega = 0.0,
                    CallVolume = data.CE.totalTradedVolume,
                    PITMP = 0.0,
                    PutChng = data.PE.change,
                    PutDelta = 0.0,
                    PutGamma = 0.0,
                    PutIV = data.PE.impliedVolatility,
                    PutLTP = 0.0,
                    PutOI = data.PE.openInterest,
                    PutOIChng = data.PE.changeinOpenInterest,
                    PutTheta = 0.0,
                    PutVega = 0.0,
                    PutVolume = data.PE.totalTradedVolume,
                    underlyingAssetValue = data.PE.underlyingValue,
                    futurePrice = 0.0
                )
                optionStrikeData.strikePriceHistoricalData[currentTime] = optionStrikePriceData

                optionExpiryData.strikeData[str(data.strikePrice)] = optionStrikeData

            output.expiryData[expiryDate] = optionExpiryData


        return output

    def __convertOpstraOptionData(self, symbol) -> OptionOiData:
        output = OptionOiData(underlying = symbol, expiryData = {})
        currentTime = datetime.now().strftime("%D - %H:%M:%S")
        opstraDataRepository = OpstraOptionDataRepository()
        count = 0
        optionRawData = None
        while optionRawData == None and count < GlobalConstants.MAX_RETRY.value:
            optionRawData = opstraDataRepository.getOptionChainData(symbol)

        for expiryDate in optionRawData.expiryData.keys():
            optionExpiryData = OptionOiExpiryData(expiryDate=expiryDate, strikeData={})
            for data in optionRawData.expiryData[expiryDate].data:

                optionStrikeData = OptionOiStrikeData(strikePrice = data.StrikePrice, strikePriceHistoricalData={})
                optionStrikePriceData = OptionOiStrikePriceData(
                    time = currentTime,
                    CITMP = data.CITMP,
                    CallChng = data.CallChng,
                    CallDelta = data.CallDelta,
                    CallGamma = data.CallGamma,
                    CallIV = data.CallIV,
                    CallLTP = data.CallLTP,
                    CallOI = data.CallOI,
                    CallOIChng = data.CallOIChng,
                    CallTheta = data.CallTheta,
                    CallVega = data.CallVega,
                    CallVolume = data.CallVolume,
                    PITMP = data.PITMP,
                    PutChng = data.PutChng,
                    PutDelta = data.PutDelta,
                    PutGamma = data.PutGamma,
                    PutIV = data.PutIV,
                    PutLTP = data.PutLTP,
                    PutOI = data.PutOI,
                    PutOIChng = data.PutOIChng,
                    PutTheta = data.PutTheta,
                    PutVega = data.PutVega,
                    PutVolume = data.PutVolume,
                    underlyingAssetValue = optionRawData.expiryData[expiryDate].spotprice,
                    futurePrice = optionRawData.expiryData[expiryDate].futuresprice
                )
                optionStrikeData.strikePriceHistoricalData[currentTime] = optionStrikePriceData

                optionExpiryData.strikeData[str(data.StrikePrice)] = optionStrikeData

            output.expiryData[expiryDate] = optionExpiryData


        return output