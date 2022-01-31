from dataclasses import dataclass

from model.mongo.OptionOiExpiryData import OptionOiExpiryData

@dataclass
class OptionOIStrikeData:
    underlying: str
    expiryData: list[OptionOiExpiryData]