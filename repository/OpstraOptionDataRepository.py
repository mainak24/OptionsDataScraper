import requests

from constants.OpstraConstants import OpstraConstants
from model.opstra.OptionExpiryOpstraRawData import OptionExpiryOpstraRawData
from model.opstra.OptionOpstraRawData import OptionOpstraRawData
from dacite import from_dict

class OpstraOptionDataRepository:
    def getOptionChainData(self, symbol) -> OptionOpstraRawData:
        output = OptionOpstraRawData(symbol=symbol, expiryData={})
        expiryDates = self.__getExpiryDates()
        for expiryDate in expiryDates:
            optionData = self.__getOptionData(symbol, expiryDate)
            if optionData != None:
                output.expiryData[expiryDate] = optionData

        return output

    def __getExpiryDates(self) -> list[str]:
        session = requests.Session()
        headers= {"User-Agent": "Python-Script", 
                  "Accept": "*/*", 
                  "Accept-Encoding": "gzip, deflate, br", 
                  "Connection": "keep-alive",
                  "Host": "opstra.definedge.com"}
        response = session.get(url = OpstraConstants.OPTION_EXPIRY_URL.value, headers=headers, timeout=3)
        try:
            data = response.json()
        except:
            data = None

        return data

    def __getOptionData(self, symbol, expiryDate) -> OptionExpiryOpstraRawData:
        session = requests.Session()
        headers= {"User-Agent": "Python-Script", 
                  "Accept": "*/*", 
                  "Accept-Encoding": "gzip, deflate, br", 
                  "Connection": "keep-alive",
                  "Host": "opstra.definedge.com"}
        url = OpstraConstants.OPTION_CHAIN_URL.value + symbol + "&" + expiryDate
        response = session.get(url = url, headers=headers, timeout=3)
        try:
            data = response.json()
            rawData = from_dict(data_class=OptionExpiryOpstraRawData, data=data)
        except:
            rawData = None

        return rawData