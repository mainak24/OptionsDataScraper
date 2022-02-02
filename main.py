import time
from constants.OpstraConstants import OpstraConstants
from repository.OptionOiMongoRepository import OptionOiMongoRepository
from constants.RepositoryConstants import RepositoryConstants
from constants.GlobalConstants import GlobalConstants
from service.OptionOiConvertRawDataService import OptionOiConvertRawDataService
from service.SchedulerService import SchedulerService

scheduler = SchedulerService()

while True:
    scheduler.fetchIndexDataPeriodically()
    # print("Sleep End")
    time.sleep(60)

