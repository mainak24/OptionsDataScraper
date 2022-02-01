from dataclasses import dataclass
from typing import Optional

from model.opstra.OptionStrikePriceOpstraRawData import OptionStrikePriceOpstraRawData

@dataclass
class OptionExpiryOpstraRawData:
    atmstrike: int
    data: Optional[list[OptionStrikePriceOpstraRawData]]
    futuresprice: float
    spotprice: float
    totalcalloi: int
    totalcallvolume: int
    totalputoi: int
    totalputvolume: int