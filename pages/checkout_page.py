from decimal import Decimal

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.data import parse_price


class CheckoutPage(BasePage):
    # Paso 1: datos
    FIRST_NAME = (By.CSS_SELECTOR, "[data-test='firstName']")
    LAST_NAME = (By.CSS_SELECTOR, "[data-test='lastName']")
    POSTAL_CODE = (By.CSS_SELECTOR, "[data-test='postalCode']")
    CONTINUE = (By.CSS_SELECTOR, "[data-test='continue']")
    ERROR = (By.CSS_SELECTOR, "[data-test='error']")

    # Paso 2: resumen
    ITEM_PRICE = (By.CSS_SELECTOR, "[data-test='inventory-item-price']")
    SUBTOTAL = (By.CSS_SELECTOR, "[data-test='subtotal-label']")
    TAX = (By.CSS_SELECTOR, "[data-test='tax-label']")
    TOTAL = (By.CSS_SELECTOR, "[data-test='total-label']")
    FINISH = (By.CSS_SELECTOR, "[data-test='finish']")

    # Paso 3: confirmacion
    COMPLETE_HEADER = (By.CSS_SELECTOR, "[data-test='complete-header']")

    def fill_form(self, first_name, last_name, postal_code):
        # Se completan solo los campos con valor, asi se puede probar con campos vacios
        for locator, value in (
            (self.FIRST_NAME, first_name),
            (self.LAST_NAME, last_name),
            (self.POSTAL_CODE, postal_code),
        ):
            if value:
                self.type(locator, value)

    def continue_to_summary(self):
        self.click(self.CONTINUE)

    def error_message(self):
        return self.text_of(self.ERROR)

    def item_prices(self):
        return [parse_price(e.text) for e in self.find_all(self.ITEM_PRICE)]

    def subtotal(self):
        return parse_price(self.text_of(self.SUBTOTAL))

    def tax(self):
        return parse_price(self.text_of(self.TAX))

    def total(self):
        return parse_price(self.text_of(self.TOTAL))

    def expected_total(self):
        return sum(self.item_prices(), Decimal("0")) + self.tax()

    def finish(self):
        self.click(self.FINISH)

    def confirmation_message(self):
        return self.text_of(self.COMPLETE_HEADER)
