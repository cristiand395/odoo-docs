## Models
- Básicamente son clases de Python.
- Se configura la lógica del negocio.
- Odoo utiliza su propia ORM(Object-Relational Mapping) para poder tener un mejor control de la base datos, el lugar de basarse en consultas SQL.
- Esta compuesto por las siguientes partes.

### Campos o atributos:
- `_name`: Requerido
  - Nombre del modelo y por ende en la base de datos, se utiliza puntos pero en la base de datos se transforma en `_`.
  - Ejemplo: `product.template` => `product_template`
- `_inherit`: No requerido
  - Modelos de necesarios para su creación
- `id`: Creado por defecto
  - Id en la base de datos
- `create_date`: Creado por defecto
  - Fecha de creación del registro
- `create_uid`: Creado por defecto
  - Usuario que creó el registro
- `write_date`: Creado por defecto
  - Última modificación del registro
- `write_uid`: Creado por defecto
  - Usuario que realizó la última modificación.

#### Tipos de campos:
- `Char`: 
  - Parámetros: string
  - Cadena de texto limitado a 256 caracteres
  - Ejemplos: Direcciones, email
    ```py
    street = fields.Char(string="Street")
    ```
- `Text`:
  - Parámetros: string
  - Cadena de texto de longitud variable
  - Ejemplos: Comentarios, descripciones de productos
    ```py
    Comment = fields.Text(string="Comment")
    ```
- `Integer`:
  - Parámetros: string
  - Números enteros
  - Ejemplos:días, nivel
    ```py
    level = fields.Integer(string="Street")
    ```
- `Float`:
  - Parámetros: string
  - Números con decimales
  - Ejemplos: Precios, porcentajes
    ```py
    price = fields.Float(string="Street")
    ```
- `Boolean`:
  - Parámetros: string
  - Validación de verdadero o falso de una condición
  - Ejemplos: Activo, publicado
    ```py
    active = fields.Boolean(string="Active")
     ```
- `Date`:
  - Parámetros: string
  - Formato: YYYY-MM-DD
  - Ejemplos: Fecha de inicio, Fecha de vencimiento
    ```py
    due_date = fields.Date(string="Due Date")
    ```
- `DateTime`:
  - Parámetros: string
  - Formato: YYYY-MM-DD HH:MM:SS
  - Ejemplos: Fecha de reunión, Fecha de creación
    ```py
    meeting_time = fields.Datetime(string="Meeting time")
    ```
- `Selection`:
  - Parámetros: string, selection
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
  - Parámetros: string
  - Permite almacenar archivos binarios como imágenes, documentos, audio o video en formato Base64
  - Ejemplos: 
    ```py
    product_image = fields.Binary(
        string="Website detail image",
        attachment=True,
        help="Image of the attribute value for shop online product detail.",
    )
    ```
|Binary |	string
|Many2one | modelo relacionado
|One2many |	modelo relacionado, campo inverso
|Many2many |	modelo relacionado, tabla intermedia
|Monetary | string

