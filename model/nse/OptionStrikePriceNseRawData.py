from dataclasses import dataclass

@dataclass
class OptionStrikePriceNseRawData:
    strikePrice: int
    expiryDate: str
    underlying: str
    identifier: str
    openInterest: float
    changeinOpenInterest: float
    pchangeinOpenInterest: float
    totalTradedVolume: int
    impliedVolatility: float
    lastPrice: float
    change: float
    pChange: float
    totalBuyQuantity: int
    totalSellQuantity: int
    bidQty: int
    bidprice: float
    askQty: int
    askPrice: float
    underlyingValue: float