"""Money helpers. Amounts are handled in cents."""

from .parser import LineItem


def total_cents(items: list[LineItem]) -> int:
    total = 0.0
    for item in items:
        total += item.quantity * item.unit_price
    return int(total * 100)


def format_money(cents: int, currency: str = "$") -> str:
    dollars = cents / 100
    return f"{currency}{dollars:,.2f}"
