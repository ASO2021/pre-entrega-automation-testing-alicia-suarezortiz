import pytest

RESOLUTIONS = [(1920, 1080), (1366, 768), (768, 1024), (390, 844)]


@pytest.mark.parametrize("width, height", RESOLUTIONS, ids=lambda v: str(v))
def test_add_to_cart_on_multiple_resolutions(inventory_page, driver, width, height):
    driver.set_window_size(width, height)
    product = inventory_page.product_names()[0]

    inventory_page.add_to_cart(product)

    assert inventory_page.cart_count() == 1
