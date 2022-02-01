import enum

from model.DataSourceEnum import DataSourceEnum
 
class GlobalConstants(enum.Enum):
    DATA_SOURCE = DataSourceEnum.OPSTRA.value
    MAX_RETRY = 10