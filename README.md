# Automatización de pruebas web - SauceDemo

## Propósito del proyecto
Automatizar flujos básicos de navegación web sobre [saucedemo.com](https://www.saucedemo.com/),
un sitio demo para practicar testing. El proyecto valida:

- **Login:** ingreso con credenciales válidas y redirección a `/inventory.html`.
- **Catálogo:** título de la página, presencia de productos, elementos de la interfaz (menú, filtro, carrito) y nombre/precio del primer producto.
- **Carrito:** agregar un producto, verificar el contador y comprobar que aparece en el carrito.

Además incluye casos extra: login inválido, quitar productos, checkout completo, ordenamiento por precio, logout y pruebas en distintas resoluciones.

## Tecnologías utilizadas
- Python 3.10 o superior
- Selenium WebDriver
- Pytest (con `pytest-html` para el reporte y `pytest-rerunfailures` para reintentos)
- Faker (datos aleatorios)
- Git y GitHub

## Estructura del proyecto
```
tests/        Casos de prueba (login, catálogo, carrito, checkout, orden, logout, resoluciones)
pages/        Page Objects: localizadores y acciones de cada página
utils/        Funciones auxiliares (datos aleatorios, conversión de precios)
config/       Configuración (URL, navegador, tiempos, credenciales)
reports/      Reporte HTML, capturas de pantalla y logs de ejecución
docs/         Tabla de casos de prueba y guía para la demo
conftest.py   Fixtures de Pytest, creación del navegador y captura de pantalla al fallar
pytest.ini    Configuración de Pytest
```

## Instalación de dependencias
```bash
git clone <url-del-repositorio>
cd <nombre-del-repositorio>
python -m venv .venv
.venv\Scripts\activate             # Windows (en Mac/Linux: source .venv/bin/activate)
pip install -r requirements.txt
```
Selenium 4 descarga solo el driver del navegador. Solo hace falta tener Chrome instalado.

## Cómo ejecutar las pruebas
Todos los tests, generando el reporte HTML:
```bash
pytest -v --html=reporte.html
```

Otras opciones:
```bash
pytest -k tc_1_1                    # un solo test
pytest -m smoke                     # solo los flujos principales
pytest tests/test_catalog.py        # un solo archivo
pytest --browser firefox            # otro navegador
pytest --window-size 390x844        # tamaño de celular
pytest --headless                   # sin abrir la ventana del navegador
```

## Evidencias generadas
- **Reporte HTML:** `reporte.html` (o `reports/report.html` si se corre solo `pytest`).
- **Capturas de pantalla:** se guardan solas en `reports/screenshots/` cuando un test falla.
- **Logs de ejecución:** `reports/execution.log`.

## Decisiones de diseño
- Localizadores robustos: atributos `data-test` e ids, sin XPath absoluto.
- Esperas explícitas (`WebDriverWait`), sin `time.sleep`.
- Cada test es independiente: abre y cierra su propio navegador.
- Cada test separa preparación, acción y validación.

Hay una versión en inglés del README en [`README_EN.md`](README_EN.md).
