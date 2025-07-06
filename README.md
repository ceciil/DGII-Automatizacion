# Prueba Técnica de Aseguramiento de la Calidad TI

Este proyecto automatiza escenarios de prueba de interfaz de usuario para una aplicación web utilizando Python, Behave (framework BDD) y Playwright (librería de automatización de navegador). La solución está diseñada siguiendo las mejores prácticas de la industria para garantizar la escalabilidad, mantenibilidad y robustez de las pruebas.

## Tecnologías Utilizadas

* **Python**: Lenguaje de programación principal utilizado para escribir el código de automatización.
* **Behave**: Un framework de Desarrollo Dirigido por Comportamiento (BDD) para Python. Permite definir el comportamiento de la aplicación en un lenguaje legible para humanos (Gherkin), facilitando la colaboración entre equipos técnicos y no técnicos.
* **Playwright**: Una potente librería de automatización de navegadores desarrollada por Microsoft. Soporta Chrome, Firefox y WebKit, y ofrece una API robusta y una auto-espera inteligente, lo que reduce la necesidad de esperas explícitas.
* **Allure Report**: Una herramienta de informes de prueba flexible y multilenguaje. Se integra con Behave a través de `allure-behave` para generar informes HTML interactivos y visualmente atractivos, que incluyen detalles de la ejecución, capturas de pantalla y un desglose claro de los pasos.
* **Gestión de Dependencias (requirements.txt)**: Un archivo para gestionar las dependencias del proyecto de Python, asegurando que todos los colaboradores puedan instalar el entorno de trabajo necesario de manera consistente.

## Enfoque y Arquitectura del Proyecto

El enfoque principal de este proyecto es la implementación de un **Modelo de Objeto de Página (Page Object Model - POM)** junto con el **Desarrollo Dirigido por Comportamiento (BDD)**.

### BDD con Behave

* **Descripción del Comportamiento**: Los escenarios de prueba se definen en archivos `.feature` utilizando la sintaxis Gherkin (Dado-Cuando-Entonces). Esto permite describir el comportamiento de la aplicación de una manera clara y comprensible para todos los miembros del equipo, incluyendo a los que no tienen conocimientos técnicos.
* **Separación de Preocupaciones**: Los archivos `.feature` se centran en *qué* se va a probar, mientras que los archivos de `steps/` se encargan de *cómo* se implementan esos pasos, usando el código de automatización.

### Arquitectura de Page Object Model (POM)

* **Reutilización y Mantenibilidad**: El POM se implementa mediante clases de página (en la carpeta `pages/`). Cada clase de página representa una interfaz de usuario o una sección significativa de la aplicación web (por ejemplo, `LoginPage`).
* **Abstracción de Elementos**: Los selectores de los elementos de la UI y los métodos para interactuar con ellos se encapsulan dentro de las clases de página. Si la UI cambia, solo es necesario actualizar el selector en la clase de página correspondiente, no en cada paso de prueba donde se utiliza el elemento.
* **Legibilidad del Código**: Los pasos de prueba son más legibles y se enfocan en las acciones de alto nivel, en lugar de en los detalles de implementación de la UI.

### Estructura del Proyecto

La organización del proyecto se adhiere a las mejores prácticas para mantener el código ordenado, modular y fácil de escalar:
```
DGII_Automatizacion/
├── features/               # Contiene los archivos Gherkin (.feature) que describen los escenarios.
│   ├── login.feature       # Definición de los escenarios de inicio de sesión.
│   └── environment.py      # Contiene los "hooks" (ganchos) de Behave para la configuración
│                           # y desmontaje del entorno (ej., lanzar/cerrar el navegador).
│   └── steps/              # Subdirectorio que contiene las definiciones de los pasos Behave
│       └── login_steps.py  # Archivo con la implementación de los pasos para los escenarios de login.
├── pages/                  # Implementación del Page Object Model.
│   ├── base_page.py        # Clase base con métodos comunes para todas las páginas.
│   └── login_page.py       # Clase para la página de inicio de sesión, encapsulando sus elementos y acciones.
├── reports/                # Directorio para los informes de prueba generados.
│   ├── allure-results/     # Contiene los datos brutos de las ejecuciones de Allure.
│   └── html/               # Contiene los informes HTML interactivos de Allure.
├── utils/                  # Clases y funciones de utilidad.
│   ├── config_reader.py    # Gestiona la configuración del proyecto (ej., URLs, credenciales).
│   └── browser_manager.py  # Encapsula la lógica para iniciar y cerrar el navegador Playwright.
├── behave.ini              # Archivo de configuración para Behave.
├── requirements.txt        # Lista de todas las dependencias de Python del proyecto.
└── README.md               # Este archivo de documentación.
```

## Buenas Prácticas Aplicadas

* **Aislamiento de Pruebas**: Cada escenario se ejecuta en un contexto de navegador nuevo y limpio (`context.page = context.browser_manager.launch_browser()` en `before_scenario`). Esto asegura que las pruebas son independientes entre sí y evita la contaminación de datos o estados entre ejecuciones.
* **Manejo de Errores y Reporting Detallado**:
    * En caso de fallo de un escenario, se captura automáticamente una **captura de pantalla** (`context.page.screenshot`) y se adjunta al informe de Allure. Esto es invaluable para la depuración.
    * Los informes de Allure proporcionan una visualización clara del estado de cada paso, facilitando la identificación de fallos.
* **Manejo de la Configuración**: La información sensible o variable (como URLs y credenciales) se centraliza en `utils/config_reader.py`, lo que facilita la gestión y actualización del entorno de pruebas. En un entorno de producción, las credenciales deberían gestionarse de forma más segura (ej., variables de entorno).
* **Utilidades Reutilizables**: Componentes como `BrowserManager` en `utils/` centralizan la lógica de inicialización y cierre del navegador, promoviendo la reutilización de código y reduciendo la duplicación.
* **Aserciones Claras con Playwright `expect`**: Se utilizan las aserciones de `playwright.sync_api.expect` para escribir verificaciones claras y concisas en los pasos de prueba, lo que mejora la legibilidad y fiabilidad de las validaciones.
* **Auto-espera Inteligente de Playwright**: Playwright maneja la mayoría de las esperas necesarias para que los elementos estén visibles y listos para la interacción de forma automática, reduciendo la necesidad de esperas explícitas manuales (`time.sleep()`), lo que hace que las pruebas sean más rápidas y menos propensas a ser "flaky" (inestables).

## Pasos de Instalación y Ejecución

### Prerrequisitos

* **Python 3.8+**: Asegúrate de tener una versión compatible de Python instalada.
* **Java**: Necesario para ejecutar la herramienta de línea de comandos de Allure Report.

### Instalación

1.  **Clonar el repositorio**:
    ```bash
    git clone <tu-url-del-repositorio-git>
    cd nombre_de_tu_proyecto
    ```
2.  **Crear y activar un entorno virtual**:
    ```bash
    python -m venv venv
    source venv/bin/activate # En Windows: venv\Scripts\activate
    ```
3.  **Instalar las dependencias de Python**:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Instalar los binarios del navegador Playwright**:
    ```bash
    playwright install
    ```
5.  **Instalar Allure Commandline**: Si no lo tienes, sigue las instrucciones de instalación de Allure Report CLI (usualmente requiere descargar el zip y añadirlo al PATH del sistema): [Allure Report Documentation](https://docs.qameta.io/allure/#_installation)

### Ejecución

1.  **Ejecutar las pruebas de Behave**:
    Asegúrate de estar en el directorio raíz del proyecto con el entorno virtual activado, y luego ejecuta:
    ```bash
    behave
    ```
    Esto ejecutará todos los escenarios definidos en tus archivos `.feature` y generará los datos brutos de los informes de Allure en `reports/allure-results/`.

## Generación y Visualización de Reportes

1.  **Generar el informe HTML de Allure**:
    Después de ejecutar las pruebas (paso anterior), utiliza el siguiente comando para generar el informe HTML interactivo:
    ```bash
    allure generate reports/allure-results --clean -o reports/html
    ```
    La opción `--clean` asegura que cualquier informe anterior en `reports/html` sea eliminado antes de generar el nuevo.

2.  **Abrir el informe de Allure en tu navegador**:
    Para ver el informe generado en tu navegador web predeterminado, ejecuta:
    ```bash
    allure open reports/html
    ```
    Esto te proporcionará una interfaz detallada y amigable para revisar los resultados de tus pruebas, incluyendo el estado de cada escenario, los pasos ejecutados y las capturas de pantalla de los fallos.
