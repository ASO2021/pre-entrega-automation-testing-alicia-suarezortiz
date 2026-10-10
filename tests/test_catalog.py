"""Navegacion y verificacion del catalogo de productos (pagina de inventario)."""


def test_catalog_title(inventory_page, driver):
    # El titulo de la pestana y el de la pagina deben ser los correctos
    assert driver.title == "Swag Labs"
    assert inventory_page.brand_name() == "Swag Labs"
    assert inventory_page.title() == "Products"


def test_catalog_has_visible_products(inventory_page):
    names = inventory_page.product_names()

    assert len(names) > 0
    assert all(name for name in names)  # ningun nombre vacio


def test_catalog_has_main_ui_elements(inventory_page):
    assert inventory_page.has_menu()
    assert inventory_page.has_sort_filter()
    assert inventory_page.has_cart_icon()


def test_catalog_first_product_name_and_price(inventory_page):
    name, price = inventory_page.first_product_info()
    print(f"Primer producto: {name} - {price}")

    assert name != ""
    assert price.startswith("$")
