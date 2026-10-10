from selenium.webdriver.common.by import By

from config import settings
from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.CSS_SELECTOR, "[data-test='username']")
    PASSWORD = (By.CSS_SELECTOR, "[data-test='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[data-test='login-button']")
    ERROR = (By.CSS_SELECTOR, "[data-test='error']")

    def open(self):
        self.driver.get(settings.BASE_URL)
        self.find(self.LOGIN_BUTTON)
        return self

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def error_message(self):
        return self.text_of(self.ERROR)

    def is_displayed(self):
        return self.is_present(self.LOGIN_BUTTON)
