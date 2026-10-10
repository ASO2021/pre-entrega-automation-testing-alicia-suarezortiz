def test_tc_5_1_sort_by_price_low_to_high(inventory_page):
    inventory_page.sort_by("lohi")

    prices = inventory_page.product_prices()
    assert len(prices) > 1
    assert prices == sorted(prices)


def test_tc_5_2_sort_by_price_high_to_low(inventory_page):
    inventory_page.sort_by("hilo")

    prices = inventory_page.product_prices()
    assert prices == sorted(prices, reverse=True)
