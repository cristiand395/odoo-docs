### Estructura de un Módulo
```txt
module
├── models
│   ├── website_sale.py
│   │__ __init__.py
├── data
│   └── *.xml
├── security
│   └── ir.mode.access.csv
├── views
│   └── templates.xml
├── __init__.py
└──  __manifest__.py
```
Ninguno es obligatorio

- Business objects (Models):
    - Python Objets
    - Describe la lógica e información del negocio
- Objects views (Views):
    - La forma como se verán los Business Objects (UI)
    - XML
- Data files (Data):
    - Donde se declaran y guardan los datos del modelo
    - XML o CSV
- Static web data (Static):
    - HTML, CSS, Javascript, Imagenes, etc.
- Web controllers (Controllers):
    - Manejan requests de los navegadores.
    - Redirecciones de URL

