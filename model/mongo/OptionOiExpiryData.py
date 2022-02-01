from dataclasses import dataclass
from typing import Dict, Optional
from model.mongo.OptionOiStrikeData import OptionOiStrikeData

@dataclass
class OptionOiExpiryData:
    expiryDate: str
    strikeData: Optional[Dict[str, OptionOiStrikeData]]