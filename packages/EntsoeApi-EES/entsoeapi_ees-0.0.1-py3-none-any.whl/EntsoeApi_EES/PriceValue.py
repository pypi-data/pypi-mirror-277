from dataclasses import dataclass
from datetime import datetime

@dataclass
class PriceValue:
    date_start : datetime
    date_end : datetime
    price : float
    unit : str