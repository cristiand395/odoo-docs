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

#### Composición de un módulo
Ninguno es obligatorio

- Business objects (Objetos de negocio):
    - Python Objets
    - Describe la lógica e información del negocio
- Objects views (Vistas):
    - La forma como se verán los Business Objects (UI)
    - XML
- Data files (Archivos de información):
    - Donde se declaran y guardan los datos del modelo
    - XML o CSV
- Static web data (Información de la web):
    - HTML, CSS, Javascript, Imagenes, etc.
- Web controllers:
    - Manejan requests de los navegadores.
    - Redirecciones de URL

