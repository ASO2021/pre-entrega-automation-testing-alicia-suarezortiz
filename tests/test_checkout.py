import pytest

from utils.data import random_checkout_data


@pytest.mark.smoke
def test_tc_4_1_successful_checkout(inventory_page, cart_page, checkout_page):
    # Setup: 3 productos en el carrito y formulario completo
    inventory_page.add_first_n_products(3)
    inventory_page.go_to_cart()
    cart_page.checkout()
    checkout_page.fill_form(**random_checkout_data())
    checkout_page.continue_to_summary()

    # Validacion del resumen: total = suma de items + impuesto
    prices = checkout_page.item_prices()
    assert len(prices) == 3
    assert checkout_page.subtotal() == sum(prices)
    assert checkout_page.total() == checkout_page.expected_total()

    # Accion final y confirmacion
    checkout_page.finish()
    assert checkout_page.confirmation_message() == "Thank you for your order!"


@pytest.mark.parametrize(
    "missing_field, expected_error",
    [
        ("first_name", "First Name is required"),
        ("last_name", "Last Name is required"),
        ("postal_code", "Postal Code is required"),
        ("all", "First Name is required"),
    ],
)
def test_tc_4_2_checkout_with_missing_details(
    inventory_page, cart_page, checkout_page, missing_field, expected_error
):
    inventory_page.add_first_n_products(1)
    inventory_page.go_to_cart()
    cart_page.checkout()

    data = random_checkout_data()
    if missing_field == "all":
        data = {key: "" for key in data}
    else:
        data[missing_field] = ""
    checkout_page.fill_form(**data)
    checkout_page.continue_to_summary()

    assert expected_error in checkout_page.error_message()
