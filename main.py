from repository.OptionOiMongoRepository import OptionOiMongoRepository
from constants.RepositoryConstants import RepositoryConstants
from constants.GlobalConstants import GlobalConstants
from service.OptionOiConvertRawDataService import OptionOiConvertRawDataService


optionDataService = OptionOiConvertRawDataService()
data = optionDataService.convertDataToMongo(GlobalConstants.DATA_SOURCE.value, "NIFTY")

repo = OptionOiMongoRepository(RepositoryConstants.MONGO_URL.value, RepositoryConstants.DATABASE.value)


# print(repo.getRecord("NIFTY", "03-Feb-2022"))

repo.updateStrikePriceData("NIFTY", data)

# print(count)

# print(data)


