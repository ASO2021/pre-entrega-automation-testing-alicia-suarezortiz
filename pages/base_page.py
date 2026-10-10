import logging

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import settings

logger = logging.getLogger(__name__)


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, settings.TIMEOUT)

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_all(self, locator):
        self.wait.until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def click(self, locator):
        logger.info("Click en %s", locator)
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        logger.info("Escribir '%s' en %s", text, locator)
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def texts_of(self, locator):
        for attempt in range(3):
            try:
                return [element.text for element in self.driver.find_elements(*locator)]
            except StaleElementReferenceException:
                logger.info("Elemento obsoleto, reintentando %s", locator)
                if attempt == 2:
                    raise

    def text_of(self, locator):
        return self.find(locator).text

    def is_present(self, locator):
        return len(self.driver.find_elements(*locator)) > 0

    def wait_until_gone(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def wait_for_url_contains(self, fragment):
        return self.wait.until(EC.url_contains(fragment))
