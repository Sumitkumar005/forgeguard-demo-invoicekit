"""Money helpers. Amounts are handled in cents."""

from .parser import LineItem


def total_cents(items: list[LineItem]) -> int:
    from decimal import Decimal, ROUND_HALF_UP
    total = Decimal('0')
    for item in items:
        # Convert unit_price to Decimal to avoid binary floating point issues
        price = Decimal(str(item.unit_price))
        total += price * item.quantity
    # Convert dollars to cents with rounding half up
    cents = (total * Decimal('100')).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
    return int(cents)


def format_money(cents: int, currency: str = "$") -> str:
    dollars = cents / 100
    return f"{currency}{dollars:,.2f}"
