from dataclasses import dataclass

@dataclass
class OptionOiStrikePriceData:
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