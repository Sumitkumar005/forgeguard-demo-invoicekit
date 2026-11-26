from invoicekit import parse_csv


def test_parses_items():
    items = parse_csv("description,quantity,unit_price\nWidget,2,19.99\nGadget,1,5.50\n")
    assert [i.description for i in items] == ["Widget", "Gadget"]
    assert items[0].quantity == 2
