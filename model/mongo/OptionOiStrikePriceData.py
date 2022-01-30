from dataclasses import dataclass
from datetime import date
from tokenize import Double

@dataclass
class OptionOIStrikePriceData:
    time: float
    openInterest: float
    totalTradedVolume: int
    impliedVolatility: float
    totalBuyQuantity: int
    totalSellQuantity: int
    bidQty: int
    bidprice: float
    askQty: int
    askPrice: float
    underlyingValue: float