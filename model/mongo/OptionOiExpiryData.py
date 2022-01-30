from dataclasses import dataclass
from datetime import date
from tokenize import Double
from model.mongo.OptionOiStrikeData import OptionOiStrikeData

from model.mongo.OptionTypeEnum import OptionType

@dataclass
class OptionOiExpiryData:
    expiryDate: str
    type: OptionType
    strikePriceData: list[OptionOiStrikeData]