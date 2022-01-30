from dataclasses import asdict
from repository.OptionOiRepository import OptionOiRepository
from constants.RepositoryConstants import RepositoryConstants
from service.NseOptionDataService import NseOptionDataService


nseDataService = NseOptionDataService()

data = nseDataService.getOptionChainData("NIFTY")

repo = OptionOiRepository(RepositoryConstants.MONGO_URL.value, RepositoryConstants.DATABASE.value)

repo.addRecord("NIFTY", asdict(data))

