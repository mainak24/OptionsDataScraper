from dataclasses import dataclass
from typing import Dict, Optional
from model.mongo.OptionOiStrikeData import OptionOiStrikeData

@dataclass
class OptionOiExpiryData:
    expiryDate: str
    callStrikeData: Optional[Dict[str, OptionOiStrikeData]]
    putStrikeData: Optional[Dict[str, OptionOiStrikeData]]