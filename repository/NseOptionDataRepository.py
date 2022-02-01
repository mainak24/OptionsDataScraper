import requests

from constants.NseConstants import NseConstants
from dacite import from_dict

from model.nse.OptionChainNseRawRecords import OptionChainNseRawRecords

class NseOptionDataRepository:

    def getOptionChainData(self, symbol) -> OptionChainNseRawRecords:
        session = requests.Session()
        params = {"symbol": symbol}
        headers= {"User-Agent": "Python-Script", 
                  "Accept": "*/*", 
                  "Accept-Encoding": "gzip, deflate, br", 
                  "Connection": "keep-alive",
                  "Host": "www.nseindia.com"}
        response = session.get(url = NseConstants.URL.value, headers=headers, timeout=3, params=params)
        try:
            data = response.json()
            rawData = from_dict(data_class=OptionChainNseRawRecords, data=data["records"])
        except:
            rawData = None

        return rawData