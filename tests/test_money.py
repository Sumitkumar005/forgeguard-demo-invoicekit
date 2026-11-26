from invoicekit import LineItem, format_money, total_cents


def test_total_simple():
    assert total_cents([LineItem("a", 2, 19.99), LineItem("b", 1, 5.50)]) == 4548


def test_format_money():
    assert format_money(123456) == "$1,234.56"
