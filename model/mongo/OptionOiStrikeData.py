from dataclasses import dataclass
from typing import Dict, Optional
from model.mongo.OptionOiStrikePriceData import OptionOiStrikePriceData

@dataclass
class OptionOiStrikeData:
    strikePrice: int
    strikePriceHistoricalData: Optional[Dict[str, OptionOiStrikePriceData]]