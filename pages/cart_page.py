from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    ITEMS = (By.CSS_SELECTOR, "[data-test='inventory-item']")
    ITEM_NAME = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    CART_BADGE = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "[data-test='checkout']")

    @staticmethod
    def _remove_button(product_name):
        slug = product_name.lower().replace(" ", "-")
        return (By.CSS_SELECTOR, f"[data-test='remove-{slug}']")

    def item_names(self):
        return [e.text for e in self.driver.find_elements(*self.ITEM_NAME)]

    def remove(self, product_name):
        self.click(self._remove_button(product_name))
        self.wait_until_gone(self._remove_button(product_name))

    def badge_count(self):
        if not self.is_present(self.CART_BADGE):
            return 0
        return int(self.text_of(self.CART_BADGE))

    def checkout(self):
        self.click(self.CHECKOUT_BUTTON)
        self.wait_for_url_contains("checkout-step-one")
