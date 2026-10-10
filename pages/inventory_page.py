from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage
from utils.data import parse_price


class InventoryPage(BasePage):
    TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    LOGO = (By.CLASS_NAME, "app_logo")
    ITEMS = (By.CSS_SELECTOR, "[data-test='inventory-item']")
    ITEM_NAME = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    ITEM_PRICE = (By.CSS_SELECTOR, "[data-test='inventory-item-price']")
    CART_BADGE = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
    CART_LINK = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
    SORT = (By.CSS_SELECTOR, "[data-test='product-sort-container']")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.CSS_SELECTOR, "[data-test='logout-sidebar-link']")

    # Botones por producto, a partir del nombre (ej: "Sauce Labs Backpack")
    @staticmethod
    def _slug(product_name):
        return product_name.lower().replace(" ", "-")

    def _add_button(self, product_name):
        return (By.CSS_SELECTOR, f"[data-test='add-to-cart-{self._slug(product_name)}']")

    def _remove_button(self, product_name):
        return (By.CSS_SELECTOR, f"[data-test='remove-{self._slug(product_name)}']")

    def title(self):
        return self.text_of(self.TITLE)

    def is_displayed(self):
        return self.is_present(self.TITLE)

    def brand_name(self):
        """Texto del logo de la tienda (ej: 'Swag Labs')."""
        return self.text_of(self.LOGO)

    def has_menu(self):
        return self.find(self.MENU_BUTTON).is_displayed()

    def has_sort_filter(self):
        return self.find(self.SORT).is_displayed()

    def has_cart_icon(self):
        return self.find(self.CART_LINK).is_displayed()

    def first_product_info(self):
        """Devuelve (nombre, precio) del primer producto de la lista."""
        name = self.find_all(self.ITEM_NAME)[0].text
        price = self.find_all(self.ITEM_PRICE)[0].text
        return name, price

    def product_names(self):
        return [e.text for e in self.find_all(self.ITEM_NAME)]

    def product_prices(self):
        return [parse_price(e.text) for e in self.find_all(self.ITEM_PRICE)]

    def add_to_cart(self, product_name):
        self.click(self._add_button(product_name))
        self.find(self._remove_button(product_name))  # el boton cambia a "Remove"

    def add_first_n_products(self, n):
        names = self.product_names()[:n]
        for name in names:
            self.add_to_cart(name)
        return names

    def cart_count(self):
        if not self.is_present(self.CART_BADGE):
            return 0
        return int(self.text_of(self.CART_BADGE))

    def go_to_cart(self):
        self.click(self.CART_LINK)
        self.wait_for_url_contains("cart.html")

    def sort_by(self, value):
        """value: az | za | lohi | hilo"""
        Select(self.find(self.SORT)).select_by_value(value)

    def logout(self):
        self.click(self.MENU_BUTTON)
        self.click(self.LOGOUT_LINK)
