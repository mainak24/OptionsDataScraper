from dataclasses import asdict
from constants.NseConstants import NseConstants
from repository.OptionOiMongoRepository import OptionOiMongoRepository
from constants.RepositoryConstants import RepositoryConstants
from service.OptionOiConvertRawDataService import OptionOiConvertRawDataService
import json


# optionDataService = OptionOiConvertRawDataService()
# data = None
# count = 0
# while data == None and count != NseConstants.MAX_RETRY.value:
#     data = optionDataService.getOptionExpiryData("NIFTY")

# repo = OptionOiMongoRepository(RepositoryConstants.MONGO_URL.value, RepositoryConstants.DATABASE.value)


# print(repo.getRecord("NIFTY", "03-Feb-2022"))

# repo.updateStrikePriceData("NIFTY", data)

# print(count)

