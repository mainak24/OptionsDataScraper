from dataclasses import dataclass
from tokenize import Double
from typing import Optional

from model.nse.OptionStrikePriceRawData import OptionStrikePriceRawData

@dataclass
class OptionStrikeRawData:
    strikePrice: int
    expiryDate: str
    CE: Optional[OptionStrikePriceRawData]
    PE: Optional[OptionStrikePriceRawData]