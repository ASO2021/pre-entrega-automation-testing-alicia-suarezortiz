def test_tc_6_1_logout(inventory_page, login_page, driver):
    inventory_page.logout()

    assert login_page.is_displayed()
    assert driver.current_url.rstrip("/") == "https://www.saucedemo.com"
