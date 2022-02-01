from dataclasses import dataclass
from typing import Dict, Optional

from model.mongo.OptionOiExpiryData import OptionOiExpiryData

@dataclass
class OptionOiData:
    underlying: str
    expiryData: Optional[Dict[str, OptionOiExpiryData]]