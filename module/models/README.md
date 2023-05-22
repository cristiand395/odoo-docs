## Models
- Se configura la lógica del negocio.
- Odoo utiliza su propia ORM (Object-Relational Mapping) para poder tener un mejor control de la base datos, el lugar de basarse en consultas SQL.
- Aquí se crean las tablas y columnas en la base de datos.
- Son básicamente clases de Python y todas extienden de la clase `Model`. 
```python
from odoo import models

class TestModel(models.Model):
  _name = "test.model"
```

### Campos (Fields):
Son los atributos que tiene un modelo que en PostgreSQL equivale a las columnas de una tabla.

#### Campos automáticos:
- `id`: Id en la base de datos
- `create_date` (`Datetime`): Fecha de creación del registro
- `create_uid`(`Many2one`): Usuario que creó el registro
- `write_date`(`Datetime`): Última modificación del registro
- `write_uid`(`Many2one`): Usuario que realizó la última modificación.
#### Otros campos:
- `_name`(**Requerido**): Nombre del modelo y por ende en la base de datos, se utiliza puntos pero en la base de datos se transforma en `_`.
  - Ejemplo: `product.template` => `product_template`
- `_inherit`: Permite extender o modificar el comportamiento de un modelo existente sin tener que crear uno nuevo desde cero.
  ```py
  class MyModel(models.Model):
    _name = 'my.module'
    _inherit = ['res.partner', 'res.users']
    _description = 'My Model'

    new_field = fields.Char(string='New Field')
  ```

##### Tipos de campos:
- `Char`: 
  - Requerido: string
  - Cadena de texto limitado a 256 caracteres
  - Ejemplos: Direcciones, email
    ```py
    street = fields.Char(string="Street")
    ```
- `Text`:
  - Requerido: string
  - Cadena de texto de longitud variable
  - Ejemplos: Comentarios, descripciones de productos
    ```py
    Comment = fields.Text(string="Comment")
    ```
- `Integer`:
  - Requerido: string
  - Números enteros
  - Ejemplos:días, nivel
    ```py
    level = fields.Integer(string="Street")
    ```
- `Float`:
  - Requerido: string
  - Números con decimales
  - Ejemplos: Precios, porcentajes
    ```py
    price = fields.Float(string="Street")
    ```
- `Boolean`:
  - Requerido: string
  - Validación de verdadero o falso de una condición
  - Ejemplos: Activo, publicado
    ```py
    active = fields.Boolean(string="Active")
     ```
- `Date`:
  - Requerido: string
  - Formato: YYYY-MM-DD
  - Ejemplos: Fecha de inicio, Fecha de vencimiento
    ```py
    due_date = fields.Date(string="Due Date")
    ```
- `DateTime`:
  - Requerido: string
  - Formato: YYYY-MM-DD HH:MM:SS
  - Ejemplos: Fecha de reunión, Fecha de creación
    ```py
    meeting_time = fields.Datetime(string="Meeting time")
    ```
- `Selection`:
  - Requerido: string, selection
  - Permite seleccionar una sola opción de una lista limitada
  - Ejemplos: Estados, Tipos
    ```py
    state = fields.Selection(
        selection=[("open", "Open"), ("done", "Done")],
        string="State",
        default="open",
        readonly=True,
    )
    ```
- `Binary`:
  - Requerido: string
  - Permite almacenar archivos binarios como imágenes, documentos, audio o video en formato Base64
  - Ejemplos: 
    ```py
    product_image = fields.Binary(
        string="Website detail image",
        attachment=True,
        help="Image of the attribute value for shop online product detail.",
    )
    ```
- `Many2one`:
  - Requerido: string, comodel_name
  - Permite vincular un campo con un solo campo de otro modelo. 
  - Ejemplos: Categorias, Compañía
    ```py
    product_category = fields.Many2one(
        string="Product category",
        comodel_name="product.category",
    )
    ```
- `Many2many`:
  - Requerido: string, comodel_name
  - Permite vincular un campo con varios campos de otro modelo.
  - Ejemplos: Clientes, Proyectos
    ```py
    customer_ids = fields.Many2many(
        string="Customers",
        comodel_name="res.partner",
    )
    ```
- `Monetary`:
  - Requerido: string, currency_field
  - Almacena valores monetarios en un moneda especifica.
  - Ejemplos: Clientes, Proyectos
    ```py
    company_currency_id = fields.Many2one(
        string="Company Currency", related="company_id.currency_id"
    )

    customer_ids = fields.Monetary(
        string="Customers",
        currency_field="company_currency_id",
    )
    ```
- `_sql_constraints`:
  - Propiedad utilizada para agregar restricciones o condiciones en **SQL** para asegurar la correcta definición o modificación de un registro. 
  - Se toman como campos a utilizar aquellos que tengan habilitadas el parámetro `index=True`
  - Sintaxis:
  ```python
  _sql_constraints = [
    ('constraint_name', 'SQL_condition', 'error_message'),
  ]
  ```
  - Ejemplo:
  ```python
  class MyModel(models.Model):
    _name = 'my.module'
    _description = 'My Model'

    name = fields.Char(string='Name', index=True)
    category = fields.Selection(
        [('A', 'Category A'),
         ('B', 'Category B'),
         ('C', 'Category C')],
        string='Category',
        index=True
    )
    date = fields.Date(string='Date')
    amount = fields.Float(string='Amount')

    _sql_constraints = [
        ('name_category_uniq', 'unique(name, category)', 'Name and Category must be unique'),
    ]

  ```
##### Parámetros:

| Nombre | Descripción | Ejemplo |
| --- | --- | --- |
| company_dependent | Si se establece en `True` indica que el campo debe tener diferente valor para cada compañía. Por defecto es `False` | `sale_discount = fields.Float(string="Discount",company_dependent=True)` |
| compute | Calcula el valor del campo mediante una función que se define en el modelo. | `total = fields.Float(compute='_compute_total')` |
| currency_field | Nombre del campo que se utilizará para almacenar el código de la moneda cuando se utiliza un campo "Monetary". | `price = fields.Monetary(string='Precio', currency_field='currency_id')` |
| default | Valor predeterminado del campo cuando se crea un nuevo registro. | `name = fields.Char(string='Nombre', default='Sin nombre')` |
| digits | Se utiliza para especificar el número de dígitos enteros y decimales que se mostrarán en el campo. | `price = fields.Float(string='Precio', digits=(6, 2))` |
| groups | Se utiliza para especificar los grupos de usuarios que tienen acceso al campo. | `name = fields.Char(string='Nombre', groups='base.group_user')` |
| help | Descripción adicional del campo que se mostrará como un tooltip en la interfaz de usuario. | `name = fields.Char(string='Nombre', help='Escriba el nombre del cliente')` |
| index | Crea un índice en el campo para acelerar las búsquedas en la base de datos. Su uso excesivo puede generar sobrecarga del servidor| `name = fields.Char(string='Nombre', index=True)` |
| inverse | Define una función que se ejecutará cuando se modifique el valor del campo y se actualizarán otros campos relacionados en consecuencia.|`price = fields.Float(inverse='_compute_tax')` 
| invisible | Define la visibilidad de unc campo, se pueden funciones . |`field1 = fields.Char(string='Field 1') field2 = fields.Char(string='Field 2', invisible=lambda self: self.field1 == 'Value')` |
| readonly | Si se establece en True, el campo será de solo lectura y no se podrá modificar su valor. | `name = fields.Char(string='Nombre', readonly=True)` |
| related | Se utiliza para obtener el valor de un campo relacionado en otro modelo. | `company_name = fields.Char(related='company_id.name', string='Nombre de la empresa')` |
| required | Indica si el campo es obligatorio o no. Si se establece en True, el campo no puede estar vacío. | `name = fields.Char(string='Nombre', required=True)` |
| size | Se utiliza para limitar el número máximo de caracteres que se pueden ingresar en el campo. | `name = fields.Char(string='Nombre', size=50)` |
| states | Define el comportamiento de un campo en función del estado del registro. | ```state = fields.Selection([('draft', 'Draft'),('open', 'Open'),('closed', 'Closed'),], string='State', default='draft') field1 = fields.Char(string='Field 1', states={'open': [('readonly', True)]}) field2 = fields.Char(string='Field 2', states={'closed': [('required', True)]})``` |
| store | Indica si los valores del campo se deben almacenar en la base de datos. Si se establece en False, el valor del campo se calculará cada vez que se acceda al registro. | `name = fields.Char(string='Nombre', store=True)` |
| string | Nombre del campo que se mostrará en la interfaz de usuario. | `name = fields.Char(string='Nombre')` |


### Built-in Functions:

Funciones integradas en los modelos que se utilizan para realizar operaciones comunes en los registros.

- `create()`: Crea un nuevo registro en el modelo utilizando los valores proporcionados en un diccionario. Devuelve el nuevo registro creado.

```py
class your_model(models.Model):
    _name='your.model'

    @api.model
    def create(self):
        values = {
          'name': 'New name',
          'price': 25.99,
          'category': 'Moda',
        }
        override_create = super(your_model,self).create(values)
        return override_create
```
- `write()`: Actualiza los valores de uno o varios registros existentes en un modelo. Permite modificar los campos específicos de un registro sin tener que crear un nuevo registro.

```py
class your_model(models.Model):
    _name='your.model'

    @api.model
    def write(self):
      values = {
        'name': 'New name',
        'price': 25.99,
        'category': 'Moda',
      }
      override_write = super(your_model,self).write(values)
      return override_write
```
- `unlink()`: Elimina **permanentemente** uno o varios registros existentes en un modelo.

```py
class your_model(models.Model):
    _name='your.model'

    @api.model
    def CustomFunction(self):
      # Logic here
      products = self.search([('category', '=', 'Factory')])
      # Eliminar los productos encontrados
      products.unlink()
```


### Odoo ORM:
Una [ORM]("https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping") (Object-Relational Mapping) es una técnica de programación que permite mapear objetos de una aplicación (Odoo) a entidades relacionales en una base de datos relacional (Postgresql). Proporciona una abstracción entre la lógica de la aplicación y la estructura de la base de datos, lo que facilita el manejo y la manipulación de los datos.

Odoo utiliza su propia capa de ORM llamada Odoo ORM, que está diseñada para facilitar la creación, actualización, búsqueda y eliminación de registros en la base de datos, además de ayudar con la seguridad.

Algunos ejemplos de uso de Odoo ORM:
- **Modelos**:
  - Los modelos en Odoo representan las entidades principales de la aplicación, como clientes, productos o pedidos.
  - Cada modelo esta asociado a una  tabla en la base de datos y define la estructura de los campos y los comportamientos del modelo.
```python
class Customer(models.Model):
    _name = 'my_module.customer'
    name = fields.Char(string='Name')
    email = fields.Char(string='Email')
```
- **Registros**:
  - Los registros son instancias individuales de un modelo y representan filas en la base de datos.
  - Se pueden crear, leer, actualizar y eliminar registros utilizando los [métodos](#built-in-functions) proporcionados por la ORM de Odoo.
```python
customer = Customer.create({'name': 'John Doe', 'email': 'john.doe@example.com'})
customer.name  # Acceder a un campo del registro
customer.write({'name': 'Jane Smith'})  # Actualizar un campo del registro
customer.unlink()  # Eliminar el registro
```
- **Consultas**:
  - Se pueden realizar consultas a la base de datos utilizando la sintaxis de dominio de Odoo.
  - La sintaxis de dominio permite filtrar y buscar registros basados en ciertos criterios.
```python
customers = Customer.search([('name', 'ilike', 'John')])  # Buscar registros que contengan 'John' en el campo 'name'
for customer in customers:
    print(customer.name)
```
- **Relaciones**:
  - Los modelos pueden tener relaciones entre sí para representar asociaciones o dependencias.
  - Se pueden definir diferentes tipos de relaciones, como One2Many, Many2one y Many2Many.
```python
class Order(models.Model):
    _name = 'my_module.order'
    customer_id = fields.Many2one('my_module.customer', string='Customer')
    product_ids = fields.Many2many('my_module.product', string='Products')
```


