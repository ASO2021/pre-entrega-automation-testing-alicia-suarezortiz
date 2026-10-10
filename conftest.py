import os
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from config import settings
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def pytest_addoption(parser):
    group = parser.getgroup("ui-automation")
    group.addoption("--browser", default=None, help="chrome | firefox | edge")
    group.addoption("--window-size", default=None, help="ej: 1366x768")
    group.addoption("--headless", action="store_true", default=False,
                    help="correr sin abrir la ventana del navegador")


def pytest_configure(config):
    """Los parametros de la linea de comandos pisan a las variables de entorno."""
    if config.getoption("--browser"):
        settings.BROWSER = config.getoption("--browser").lower()
    if config.getoption("--window-size"):
        settings.WINDOW_SIZE = config.getoption("--window-size")
    if config.getoption("--headless"):
        settings.HEADLESS = True


def _build_driver():
    width, height = settings.WINDOW_SIZE.split("x")
    browser = settings.BROWSER

    if browser == "firefox":
        options = FirefoxOptions()
        if settings.HEADLESS:
            options.add_argument("-headless")
        driver = webdriver.Firefox(options=options)
    elif browser == "edge":
        options = EdgeOptions()
        if settings.HEADLESS:
            options.add_argument("--headless=new")
        driver = webdriver.Edge(options=options)
    else:
        options = ChromeOptions()
        if settings.HEADLESS:
            options.add_argument("--headless=new")
        # Evita el popup de "cambiar contrasena" que a veces tapa la pantalla
        options.add_experimental_option(
            "prefs",
            {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
                "profile.password_manager_leak_detection": False,
            },
        )
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)

    driver.set_window_size(int(width), int(height))
    return driver


@pytest.fixture
def driver():
    driver = _build_driver()
    yield driver
    driver.quit()


@pytest.fixture
def login_page(driver):
    return LoginPage(driver).open()


@pytest.fixture
def inventory_page(login_page, driver):
    """Usuario ya logueado y parado en la pagina de productos."""
    login_page.login(settings.VALID_USER, settings.VALID_PASSWORD)
    page = InventoryPage(driver)
    assert page.title() == "Products"
    return page


@pytest.fixture
def cart_page(driver):
    return CartPage(driver)


@pytest.fixture
def checkout_page(driver):
    return CheckoutPage(driver)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Si un test falla, guarda un screenshot y lo adjunta al reporte HTML."""
    outcome = yield
    report = outcome.get_result()
    if report.when != "call" or report.passed:
        return
    driver = item.funcargs.get("driver")
    if driver is None:
        return
    os.makedirs("reports/screenshots", exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"reports/screenshots/{item.name}_{stamp}.png"
    driver.save_screenshot(path)
    try:
        import pytest_html

        extras = getattr(report, "extras", [])
        extras.append(pytest_html.extras.image(os.path.abspath(path)))
        report.extras = extras
    except ImportError:
        pass
