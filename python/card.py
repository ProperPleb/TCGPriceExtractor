from dataclasses import dataclass


@dataclass
class Card:
    quantity: int
    name: str
    set_number: str
    condition: str
    edition: str
    rarity: str
    dirty: chr
    price: float
