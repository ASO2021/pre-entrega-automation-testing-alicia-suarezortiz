# Test cases and traceability

Each requirement from the challenge is linked to its automated test.

| ID | Title | Test | Validation |
|----|-------|------|------------|
| TC 1.1 | Valid login | `test_login.py::test_tc_1_1_valid_login` | URL contains `inventory.html`, title is "Products" |
| Catalog | Title, visible products, menu / filter / cart icon, first product name and price | `test_catalog.py` (4 tests) | Tab title and logo are "Swag Labs", products present, UI elements visible |
| TC 1.2 | Invalid login | `test_login.py::test_tc_1_2_invalid_login` (5 data sets) | Error message text, user stays on login page |
| TC 1.3 | Login with slow user (extra) | `test_login.py::test_tc_1_3_login_with_slow_user` | Products load despite the delay |
| Cart flow | Add first product, check counter, open cart, verify item | `test_cart.py::test_add_first_product_and_verify_in_cart` | Badge 1, same product name in cart |
| TC 2.1 | Add single product | `test_cart.py::test_tc_2_1_add_single_product` | Badge shows 1 |
| TC 2.2 | Add multiple products | `test_cart.py::test_tc_2_2_add_multiple_products` (2, 3, 6) | Badge equals the quantity |
| TC 3.1 | Remove product | `test_cart.py::test_tc_3_1_remove_product_from_cart` | Item gone from cart, badge updated |
| TC 4.1 | Successful checkout | `test_checkout.py::test_tc_4_1_successful_checkout` | Subtotal = sum of items, total = items + tax, confirmation message |
| TC 4.2 | Checkout with missing details | `test_checkout.py::test_tc_4_2_checkout_with_missing_details` (4 data sets) | Field validation error |
| TC 5.1 | Sort low to high | `test_sorting.py::test_tc_5_1_sort_by_price_low_to_high` | Prices in ascending order |
| TC 6.1 | Logout | `test_logout.py::test_tc_6_1_logout` | Back on login page |
| Extra | Multi-resolution | `test_responsive.py` (4 sizes) | Add to cart works on desktop, tablet and phone sizes |

## Optional items from the challenge

| Optional item | Where |
|---------------|-------|
| Randomized / parametrized data | `utils/data.py` (Faker), `@pytest.mark.parametrize` |
| Cross-browser | `--browser` (chrome, firefox or edge), CI matrix |
| Multi-resolution | `--window-size`, `tests/test_responsive.py` |
| Retry for flaky tests | `pytest-rerunfailures` (`pytest.ini`) |
| Execution reports | `reports/report.html` + screenshots on failure |
