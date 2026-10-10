import pytest


@pytest.mark.smoke
def test_tc_2_1_add_single_product(inventory_page):
    product = inventory_page.product_names()[0]

    inventory_page.add_to_cart(product)

    assert inventory_page.cart_count() == 1


@pytest.mark.parametrize("quantity", [2, 3, 6])
def test_tc_2_2_add_multiple_products(inventory_page, quantity):
    added = inventory_page.add_first_n_products(quantity)

    assert len(added) == quantity
    assert inventory_page.cart_count() == quantity


def test_tc_3_1_remove_product_from_cart(inventory_page, cart_page):
    # Setup: dos productos en el carrito
    added = inventory_page.add_first_n_products(2)
    inventory_page.go_to_cart()
    assert cart_page.item_names() == added

    # Accion: quitar el primero
    cart_page.remove(added[0])

    # Validacion: queda solo el segundo y el badge se actualiza
    assert cart_page.item_names() == [added[1]]
    assert cart_page.badge_count() == 1


def test_tc_3_1_remove_last_product_clears_badge(inventory_page, cart_page):
    added = inventory_page.add_first_n_products(1)
    inventory_page.go_to_cart()

    cart_page.remove(added[0])

    assert cart_page.item_names() == []
    assert cart_page.badge_count() == 0


@pytest.mark.smoke
def test_add_first_product_and_verify_in_cart(inventory_page, cart_page):
    """Flujo de la consigna: agregar el primer producto, ver el contador y comprobarlo en el carrito."""
    name, _ = inventory_page.first_product_info()

    inventory_page.add_to_cart(name)
    assert inventory_page.cart_count() == 1

    inventory_page.go_to_cart()
    assert cart_page.item_names() == [name]
    assert cart_page.badge_count() == 1
