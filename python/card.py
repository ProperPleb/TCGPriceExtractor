from dataclasses import dataclass


@dataclass
class Card:
    quantity: int
    name: str
    set_number: str
    price: float
    condition: str
    edition: str
    dirty: chr
