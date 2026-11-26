"""Parse invoice line items from CSV text: description,quantity,unit_price"""

from dataclasses import dataclass


@dataclass
class LineItem:
    description: str
    quantity: int
    unit_price: float


def parse_csv(text: str) -> list[LineItem]:
    items = []
    lines = text.strip().split("\n")
    for line in lines[1:]:  # skip header
        description, quantity, unit_price = line.split(",")
        items.append(LineItem(description.strip(), int(quantity), float(unit_price)))
    return items
