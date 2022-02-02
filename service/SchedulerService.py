from datetime import datetime
import time
from constants.OpstraConstants import OpstraConstants
from repository.OptionOiMongoRepository import OptionOiMongoRepository
from constants.RepositoryConstants import RepositoryConstants
from constants.GlobalConstants import GlobalConstants
from service.OptionOiConvertRawDataService import OptionOiConvertRawDataService

class SchedulerService:
    def __init__(self) -> None:
        self.optionDataService = OptionOiConvertRawDataService()
        self.repo = OptionOiMongoRepository(RepositoryConstants.MONGO_URL.value, RepositoryConstants.DATABASE.value)
        self.lastUpdatedTime = datetime.now()
        return

    def fetchIndexDataPeriodically(self):

        if self.__isWeekDay() and self.__isMarketOpen():
            if  self.__isDelayLapsed():
                self.lastUpdatedTime = datetime.now()
                print("Fetching Data")
                bankNiftyData = self.optionDataService.fetchDataForMongo(GlobalConstants.DATA_SOURCE.value, OpstraConstants.NIFTY_BANK.value)
                niftyData = self.optionDataService.fetchDataForMongo(GlobalConstants.DATA_SOURCE.value, OpstraConstants.NIFTY.value)

                print("Saving Data")
                self.repo.updateStrikePriceData(OpstraConstants.NIFTY_BANK.value, bankNiftyData)
                self.repo.updateStrikePriceData(OpstraConstants.NIFTY.value, niftyData)

                print("Data Saved, Party!!!")
                time.sleep(GlobalConstants.DATA_SNAPSHOT_TIME_GAP.value * 60 - GlobalConstants.DATA_SNAPSHOT_TIME_GAP_TOLERANCE.value * 10)
        else:
            print("Market Off, Sleeping")
            sec = self.__getSecondsTillMarketOpen()
            time.sleep(sec)

        return

    def __isWeekDay(self):
        if datetime.now().weekday() in GlobalConstants.MARKET_OPEN_DATES.value:
            return True
        
        return False

    def __isMarketOpen(self):
        time = datetime.now().hour + datetime.now().minute/60
        if time >= GlobalConstants.MARKET_START_TIME.value and time <= GlobalConstants.MARKET_END_TIME.value:
            return True
        
        return False

    def __isDelayLapsed(self):
        difference = (datetime.now() - self.lastUpdatedTime)
        differenceInMin = divmod(difference.days * 24*60*60 + difference.seconds, 60)
        print(differenceInMin)
        if differenceInMin[0] >= GlobalConstants.DATA_SNAPSHOT_TIME_GAP.value and differenceInMin[1] >= GlobalConstants.DATA_SNAPSHOT_TIME_GAP_TOLERANCE.value:
            return True
        
        return False

    def __getSecondsTillMarketOpen(self):
        output = 0
        currentTime = datetime.now()
        if self.__isWeekDay():
            time = currentTime.hour + currentTime.minute/60
            if time < GlobalConstants.MARKET_START_TIME.value:
                output += (GlobalConstants.MARKET_START_TIME.value - time) * 60 * 60 - GlobalConstants.DATA_SNAPSHOT_TIME_GAP_TOLERANCE.value * 5;
            elif time < GlobalConstants.MARKET_START_TIME.value and (GlobalConstants.MARKET_START_TIME.value - time) * 60 * 60 < GlobalConstants.DATA_SNAPSHOT_TIME_GAP_TOLERANCE.value * 10:
                return 0
            elif time > GlobalConstants.MARKET_END_TIME.value:
                output += (24.0 - GlobalConstants.MARKET_END_TIME.value + GlobalConstants.MARKET_START_TIME.value) * 60 * 60 - GlobalConstants.DATA_SNAPSHOT_TIME_GAP_TOLERANCE.value * 5;
        else:
            output += (24.0 - GlobalConstants.MARKET_END_TIME.value) * 60 * 60;
            output += (6 - currentTime.weekday()) * 24 * 60 * 60 + GlobalConstants.MARKET_START_TIME.value * 60 * 60 - GlobalConstants.DATA_SNAPSHOT_TIME_GAP_TOLERANCE.value * 5


        return output
