from dataclasses import dataclass

from model.mongo.OptionOiStrikePriceData import OptionOIStrikePriceData


@dataclass
class OptionOiStrikeData:
    strikePrice: float
    strikePriceData: list[OptionOIStrikePriceData]