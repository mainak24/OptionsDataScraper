import requests

from constants.NseConstants import NseConstants
from dacite import from_dict

from model.nse.OptionChainRawRecords import OptionChainRawRecords

class NseOptionDataService:

    def getOptionChainData(self, symbol):
        session = requests.Session()
        params = {"symbol": symbol}
        headers= {"User-Agent": "Python-Script", 
                  "Accept": "*/*", 
                  "Accept-Encoding": "gzip, deflate, br", 
                  "Connection": "keep-alive",
                  "Host": "www.nseindia.com"}
        response = session.get(url = NseConstants.URL.value, headers=headers, timeout=3, params=params)
        data = response.json()
        rawData = from_dict(data_class=OptionChainRawRecords, data=data["records"])
        return rawData