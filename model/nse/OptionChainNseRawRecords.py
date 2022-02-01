from dataclasses import dataclass

from model.nse.OptionStrikeNseRawData import OptionStrikeNseRawData

@dataclass
class OptionChainNseRawRecords:
    timestamp: str
    underlyingValue: float
    expiryDates: list[str]
    data: list[OptionStrikeNseRawData]
    strikePrices: list[int]