## ¿Cuál es la diferencia entre Template y Record?
- Template hereda una vista y reemplaza o cambia completamente la vista, mientras que el record es una modificación por encima que para acceder a ella se necesita el id del record.
- Se recomienda el Template para modificaciones en el website y Record para cambios en menús y panel de control.


## No se aplican cambios por más que actualice el módulo
- Revisa que el módulo este instalado, por algún motivo no se debió instalar o quizás se desinstaló.
- Puedes actualizar la lista de aplicaciones e instalar el módulo o directamente desde la línea de comandos:
```bash
~/odoo/odoo/odoo.bin -c ~/odoo/odoo/debian/odoo.conf -i $Module
```

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