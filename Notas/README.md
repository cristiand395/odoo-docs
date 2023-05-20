## ¿Cuál es la diferencia entre Template y Record?
- Template hereda una vista y reemplaza o cambia completamente la vista, mientras que el record es una modificación por encima que para acceder a ella se necesita el id del record.
- Se recomienda el Template para modificaciones en el website y Record para cambios en menús y panel de control.

## ¿Cómo acceder a la información de un módulo?
-  Desde un modelo:
```python
from odoo import models

class MyModel(model.Model):
    # Acceder a la tabla productos
    products = self.env[¨product.template¨]

    # Utilizar dominios para hacer filtros
    domain = [
        ("country", "=", "Spain"),
        ("name", "like", "Light"),
        ("category", "ilike", "last"),
        ("active", "!=", False),
        ("price", ">=", 2000)
    ]

    # Logic here 
```
- Desde un controller:
```python
from odoo import http

class MyModel(model.Model):
    # Acceder a la tabla productos
    products = http.request.env[¨product.template¨]

    # Utilizar dominios para hacer filtros
    domain = [
        ("country", "=", "Spain"),
        ("name", "like", "Light"),
        ("category", "ilike", "last"),
        ("active", "!=", False),
        ("price", ">=", 2000)
    ]

    # Logic here 
```