# Guia para la demo en vivo

## Como explicar el proyecto en 1 minuto
"Automatice la tienda SauceDemo con Python, Selenium y Pytest, usando Page Object Model.
Cada pagina tiene su clase con los locators y las acciones. Los tests solo llaman a esas acciones
y validan el resultado. Uso esperas explicitas, datos aleatorios con Faker y un reporte HTML.
Ademas lo deje corriendo en GitHub Actions con Chrome y Firefox."

## Orden sugerido para mostrar el codigo
1. `pages/base_page.py`: esperas explicitas y metodos reutilizables.
2. `pages/inventory_page.py`: locators con `data-test` y acciones de negocio.
3. `conftest.py`: fixture `inventory_page` (usuario ya logueado) y screenshot al fallar.
4. `tests/test_checkout.py`: el flujo mas completo, separado en setup, accion y validacion.
5. `.github/workflows/ui-tests.yml`: el CI.

## Preguntas probables y respuestas cortas
- **Por que Page Object Model?** Los locators quedan en un solo lugar. Si cambia la pagina, se arregla en una clase y no en todos los tests.
- **Por que no usas `sleep`?** Es fragil y lento. Uso `WebDriverWait`, que espera solo lo necesario.
- **Por que `data-test` y no XPath?** Son atributos pensados para testing. No cambian si cambia el diseno.
- **Que hace el fixture `inventory_page`?** Hace el login y devuelve la pagina de productos, asi los tests no repiten pasos.
- **Como validas el total del checkout?** Sumo los precios del resumen y comparo con el subtotal. Despues verifico que total = items + impuesto. Uso `Decimal` para no tener errores de redondeo con floats.
- **Que pasa si un test es inestable?** Pytest lo reintenta una vez. Si sigue fallando, el reporte trae un screenshot.
- **Como pruebas otro navegador?** `pytest --browser firefox`. En el CI corre en Chrome y Firefox.
- **Como probas otra resolucion?** `pytest --window-size 390x844`, y hay tests parametrizados en `test_responsive.py`.
- **Para que sirve `performance_glitch_user`?** Es un usuario con carga lenta. Sirve para demostrar que las esperas explicitas manejan contenido dinamico.
- **Que mejorarias?** Agregar Allure, correr en paralelo con `pytest-xdist` y sumar tests de API.

## Comandos para la demo
```
pytest                              # todo
pytest -m smoke                     # solo flujos principales
pytest -k tc_4_1                    # un test
pytest --browser firefox            # otro navegador
pytest --window-size 390x844        # tamano de celular
pytest --headless                   # sin abrir ventana
```
Reporte: abrir `reports/report.html`.

## Si algo falla en vivo
1. Lee el mensaje de error: casi siempre dice que elemento no encontro.
2. Abre el screenshot en `reports/screenshots/`.
3. Explica que harias: revisar el locator en las DevTools del navegador (F12).
