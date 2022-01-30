from dataclasses import dataclass

from model.mongo.OptionOiExpiryData import OptionOiExpiryData

@dataclass
class OptionOIStrikeData:
    underlying: str
    strikePriceData: list[OptionOiExpiryData]