from dataclasses import dataclass
from typing import Optional

from model.nse.OptionStrikePriceNseRawData import OptionStrikePriceNseRawData

@dataclass
class OptionStrikeNseRawData:
    strikePrice: int
    expiryDate: str
    CE: Optional[OptionStrikePriceNseRawData]
    PE: Optional[OptionStrikePriceNseRawData]