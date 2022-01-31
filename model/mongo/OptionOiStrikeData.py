from dataclasses import dataclass
from typing import Optional
from model.mongo.OptionOiStrikePriceData import OptionOiStrikePriceData

@dataclass
class OptionOiStrikeData:
    strikePrice: float
    # strikePriceData: Optional[list[OptionOiStrikePriceData]]