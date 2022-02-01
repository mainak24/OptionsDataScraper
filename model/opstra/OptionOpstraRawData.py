from dataclasses import dataclass
from typing import Dict, Optional

from model.opstra.OptionExpiryOpstraRawData import OptionExpiryOpstraRawData

@dataclass
class OptionOpstraRawData:
    symbol: str
    expiryData: Optional[Dict[str, OptionExpiryOpstraRawData]]