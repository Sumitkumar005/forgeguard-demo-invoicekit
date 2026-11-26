import sys

from .money import format_money, total_cents
from .parser import parse_csv


def main(path: str) -> None:
    with open(path, encoding="utf-8") as f:
        items = parse_csv(f.read())
    for item in items:
        print(f"{item.description:<30} x{item.quantity:<4} {format_money(round(item.unit_price * 100))}")
    print(f"{'TOTAL':<36} {format_money(total_cents(items))}")


if __name__ == "__main__":
    main(sys.argv[1])
