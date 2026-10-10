# SauceDemo UI Automation

GUI test automation for the [SauceDemo](https://www.saucedemo.com/) shop.
Built with Python, Selenium and Pytest, using the Page Object Model.

## What it covers

| ID | Scenario | File |
|----|----------|------|
| TC 1.1 | Valid login | `tests/test_login.py` |
| Catalog | Title, visible products, UI elements, first product name and price | `tests/test_catalog.py` |
| TC 1.2 | Invalid login (wrong user, wrong password, empty fields, locked user) | `tests/test_login.py` |
| TC 2.1 | Add one product to the cart | `tests/test_cart.py` |
| TC 2.2 | Add multiple products to the cart | `tests/test_cart.py` |
| TC 3.1 | Remove a product from the cart | `tests/test_cart.py` |
| TC 4.1 | Successful checkout (total = items + tax) | `tests/test_checkout.py` |
| TC 4.2 | Checkout with missing details | `tests/test_checkout.py` |
| TC 5.1 | Sort products by price, low to high | `tests/test_sorting.py` |
| TC 6.1 | Logout | `tests/test_logout.py` |

Extra: slow-loading user, sort by price high to low, removing the last product, and add to cart on 4 screen sizes.

The full mapping is in [`docs/test_cases.md`](docs/test_cases.md).

## Project structure

```
config/settings.py     URL, browser, timeouts, credentials (all from env vars)
pages/                 Page objects: locators and reusable actions
  base_page.py         Explicit waits, click, type, helpers
  login_page.py
  inventory_page.py
  cart_page.py
  checkout_page.py
tests/                 Test cases, one file per feature
docs/                  Test case traceability and demo guide
.github/workflows/     CI pipeline (GitHub Actions)
utils/data.py          Random test data (Faker) and price parsing
conftest.py            Driver setup, fixtures, screenshot on failure
pytest.ini             Pytest options, HTML report, retries
```

## Design decisions

- **Locators:** only `data-test` attributes and ids. No absolute XPath.
- **Waits:** explicit waits only (`WebDriverWait`). No `time.sleep`.
- **Structure:** each test follows setup, action, validation.
- **Fixtures:** `inventory_page` gives a logged-in user, so tests do not repeat the login steps.
- **Test data:** random checkout data with Faker. Parametrized tests for login, quantities and missing fields.
- **Flaky tests:** one automatic retry with `pytest-rerunfailures`.
- **Failures:** a screenshot is saved and attached to the HTML report.

## Requirements

- Python 3.10 or higher
- Google Chrome (or Firefox / Edge)
- Selenium 4.6+ downloads the browser driver by itself. No manual driver setup.

## Setup

```bash
git clone <your-repo-url>
cd saucedemo-ui-automation
python -m venv .venv
source .venv/bin/activate          # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run the tests

```bash
pytest                              # all tests, Chrome
pytest -m smoke                     # only the main flows
pytest tests/test_checkout.py       # one file
pytest -k "tc_4_1"                  # one test
```

The HTML report is saved in `reports/report.html`.
Failure screenshots go to `reports/screenshots/`. Execution logs go to `reports/execution.log`.

## Options

Use command line flags:

```bash
pytest --browser firefox            # chrome | firefox | edge
pytest --window-size 390x844        # phone size
pytest --headless                   # no browser window
pytest --browser firefox --headless --window-size 1366x768
```

Or environment variables: `BROWSER`, `HEADLESS`, `WINDOW_SIZE`, `TIMEOUT`, `BASE_URL`.
Flags win over environment variables.

## CI/CD

The workflow in `.github/workflows/ui-tests.yml` runs on every push and pull request.
It runs all tests in headless mode on Chrome and Firefox, and uploads the HTML report as an artifact.

## Notes

- Valid user: `standard_user` / `secret_sauce`.
- The `locked_out_user` case checks the locked account error message.
