from dataclasses import dataclass

@dataclass
class OptionStrikePriceOpstraRawData:
    CITMP: float
    CallChng: float
    CallDelta: float
    CallGamma: float
    CallIV: float
    CallLTP: float
    CallOI: float
    CallOIChng: float
    CallTheta: float
    CallVega: float
    CallVolume: float
    PITMP: float
    PutChng: float
    PutDelta: float
    PutGamma: float
    PutIV: float
    PutLTP: float
    PutOI: float
    PutOIChng: float
    PutTheta: float
    PutVega: float
    PutVolume: float
    StrikePrice: int