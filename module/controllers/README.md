# Controlllers:

Siguen el patrón de diseño Model-View-Controller (MVC). En este patrón, los controllers actúan como la capa de control que maneja las solicitudes y coordina las interacciones entre los modelos de datos y las vistas.

Un módulo de Odoo puede tener uno o más controllers. Cada controller se define como una clase en Python que hereda de odoo.http.Controller. Los controllers pueden tener métodos decorados con los decoradores `@http.route` para especificar las rutas URL que se manejarán.

Cuando una solicitud HTTP llega al servidor Odoo, el enrutador HTTP de Odoo identifica la ruta correspondiente y dirige la solicitud al controlador adecuado. Luego, el controlador ejecuta el método asociado a la ruta y genera una respuesta HTTP, que puede ser una página HTML, un archivo descargable, una respuesta JSON, entre otros.

Los controllers en Odoo brindan la capacidad de personalizar y extender la funcionalidad del servidor Odoo a través de la implementación de nuevas rutas y acciones personalizadas. Esto permite crear API personalizadas, integraciones con sistemas externos y gestionar acciones específicas en respuesta a las solicitudes del usuario.

En resumen, los controllers en un módulo de Odoo son componentes que manejan las solicitudes HTTP y generan respuestas correspondientes. Son parte del patrón MVC y permiten personalizar y extender la funcionalidad del servidor Odoo.

## API
### **Routing** [Fuente](https://github.com/odoo/odoo/blob/15.0/odoo/http.py#L442)
```
odoo.http.route(route=None, **kw)
``` 
Se utilliza para especificar la URL que activara la funcion definida.

#### Parámetros:
- route (string): Especifica la ruta o rutas URL que se manejarán.

- type (string): Especifica el tipo de respuesta que se espera. Los valores comunes incluyen:
    - 'http': Respuesta HTTP estándar.
    - 'json': Respuesta en formato JSON.
    - 'jsonify': Respuesta en formato JSON con cabecera adecuada.

- methods (list): Especifica los métodos HTTP permitidos para la ruta URL.
    - 'GET': Respuesta
    - 'POST': Respuesta
  
- auth (cadena): Define el nivel de autenticación requerido para acceder a la ruta URL. Los valores comunes incluyen:
    - 'none': No se requiere autenticación.
    - 'public': Acceso permitido para usuarios no autenticados.
    - 'user': Acceso permitido solo para usuarios autenticados.
  
- website (boolean): Especifica si la ruta URL debe estar disponible en el sitio web público de Odoo.

- csrf (boolean): Indica si se debe habilitar la protección CSRF (Cross-Site Request Forgery) para la ruta URL.

- cors (cadena o booleano): Habilita la configuración CORS (Cross-Origin Resource Sharing) para la ruta URL.

#### Ejemplo:
```python
    @http.route(
        ['/route','/route2'], 
        type='http', 
        auth='none', 
        method=['GET','POST'],
        cors='*', 
        csrf=False, 
        website=True,
        save_session=False)
    def function(self):
        # Logic
        return res
```

### **Request** [fuente](https://github.com/odoo/odoo/blob/15.0/odoo/http.py#L163)
```
odoo.http.WebRequest(httprequest)
``` 
Este decorador permite acceder y manipular los datos de la solicitud HTTP entrandte, como parametro GET, POST o archivos adjuntos. Puedes utilizarlo para validar datos, realizar acciones especificas antes que se procese la solicitud o modificar los datos recibidos.


### **Response** [fuente](https://github.com/odoo/odoo/blob/15.0/odoo/http.py#L1184)
```
odoo.http.Response(*args, **kw)
``` 
Se utiliza para personalizar la respuesta HTTP que el servidor enviara al cliente. Puedes usarlo para modificar los header, establecer cookies, redirigir a otra URL o devolver contendio.
