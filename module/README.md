### Estructura de un Módulo
```txt
module
├── controllers
│   ├── *.py
│   └── __init__.py
├── data
│   └── *.xml
├── models
│   ├── *.py
│   └── __init__.py
├── security
│   ├── ir.mode.access.csv
│   └── *.csv
├── static
│   ├── description
│   │    ├── *.png
|   |    └── *.svg
│   └── src
│        ├── img
|        |    |── *.png
|        |    └── *.gif
│        ├── js
|        |    └── *.js
|        |── scss
|        |    └── *.js
|        └── xml
|             └── *.xml
├── test
│    |── *.py
│    └── __init__.py
├── views
│    └── *.xml
├── __init__.py
└── __manifest__.py
```

Ninguno es obligatorio

- Web controllers ([Controllers](./controllers/README.md)):
    - Controlan las solicitudes HTTP.
    - Redirecciones de URL
- Business objects ([Models](./models/README.md)):
    - Python Objets
    - Describe la lógica e información del negocio
- Objects views ([Views](./views/README.md)):
    - La forma como se verán los Business Objects (UI)
    - XML
- Data files ([Data](./data/README.md)):
    - Donde se declaran y guardan los datos del modelo
    - XML o CSV
- Static web data ([Static](.static/README.md)):
    - HTML, CSS, Javascript, Imagenes, etc.

