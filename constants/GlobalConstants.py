import enum

from model.DataSourceEnum import DataSourceEnum
 
class GlobalConstants(enum.Enum):
    DATA_SOURCE = DataSourceEnum.OPSTRA.value
    MARKET_OPEN_DATES = [0,1,2,3,4]
    MARKET_START_TIME = 9.25 # .25 means 15 mins - scaled to 0-99
    MARKET_END_TIME = 15.8
    DATA_SNAPSHOT_TIME_GAP = 10 # in min
    DATA_SNAPSHOT_TIME_GAP_TOLERANCE = 3 # in sec
    MAX_RETRY = 10