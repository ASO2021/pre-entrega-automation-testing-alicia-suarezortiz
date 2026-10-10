import os

BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com/")
BROWSER = os.getenv("BROWSER", "chrome").lower()          # chrome | firefox | edge
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
WINDOW_SIZE = os.getenv("WINDOW_SIZE", "1920x1080")        # ej: 1366x768
TIMEOUT = int(os.getenv("TIMEOUT", "30"))

VALID_USER = os.getenv("SAUCE_USER", "standard_user")
VALID_PASSWORD = os.getenv("SAUCE_PASSWORD", "secret_sauce")
