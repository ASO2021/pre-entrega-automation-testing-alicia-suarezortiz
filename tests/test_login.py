import pytest

from config import settings
from pages.inventory_page import InventoryPage


@pytest.mark.smoke
def test_tc_1_1_valid_login(login_page, driver):
    login_page.login(settings.VALID_USER, settings.VALID_PASSWORD)

    inventory = InventoryPage(driver)
    assert "/inventory.html" in driver.current_url
    assert inventory.title() == "Products"
    assert inventory.brand_name() == "Swag Labs"


@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        ("invalid_user", "secret_sauce",
         "Username and password do not match any user in this service"),
        ("standard_user", "wrong_password",
         "Username and password do not match any user in this service"),
        ("", "secret_sauce", "Username is required"),
        ("standard_user", "", "Password is required"),
        ("locked_out_user", "secret_sauce", "this user has been locked out"),
    ],
    ids=["bad_user", "bad_password", "empty_user", "empty_password", "locked_user"],
)
def test_tc_1_2_invalid_login(login_page, username, password, expected_error):
    login_page.login(username, password)

    assert expected_error in login_page.error_message()
    assert login_page.is_displayed()


def test_tc_1_3_login_with_slow_user(login_page, driver):
    """performance_glitch_user tarda en cargar: prueba que las esperas explicitas funcionan."""
    login_page.login("performance_glitch_user", settings.VALID_PASSWORD)

    inventory = InventoryPage(driver)
    assert inventory.title() == "Products"
    assert len(inventory.product_names()) == 6
