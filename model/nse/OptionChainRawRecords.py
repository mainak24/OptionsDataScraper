from dataclasses import dataclass

from model.nse.OptionStrikeRawData import OptionStrikeRawData

@dataclass
class OptionChainRawRecords:
    timestamp: str
    underlyingValue: float
    expiryDates: list[str]
    data: list[OptionStrikeRawData]
    strikePrices: list[int]