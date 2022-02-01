from repository.OptionOiMongoRepository import OptionOiMongoRepository
from constants.RepositoryConstants import RepositoryConstants
from constants.GlobalConstants import GlobalConstants
from service.OptionOiConvertRawDataService import OptionOiConvertRawDataService


optionDataService = OptionOiConvertRawDataService()
data = optionDataService.convertDataToMongo(GlobalConstants.DATA_SOURCE.value, "NIFTY")

repo = OptionOiMongoRepository(RepositoryConstants.MONGO_URL.value, RepositoryConstants.DATABASE.value)

repo.updateStrikePriceData("NIFTY", data)


