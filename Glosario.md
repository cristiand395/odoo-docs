# Glosario

- **Identificador externo** (`xml_id`): Hace referencia a un registro independientemente de su ubicación en base de datos. En qué casos es útil:
  - _**Integración con sistemas externos**_: Cuando Odoo necesita interactuar con otros sistemas o aplicaciones externas, los identificadores externos permiten establecer una relación precisa entre los registros de Odoo y los registros correspondientes en el sistema externo. Esto facilita la sincronización de datos y el intercambio de información entre Odoo y otras plataformas.
  - _**Migración de datos**_: Si necesitas migrar datos desde otro sistema a Odoo, los identificadores externos pueden ser útiles para mantener la integridad de los datos. Puedes asignar identificadores externos a los registros en el sistema de origen y asegurarte de que esos identificadores se mantengan durante la migración a Odoo. De esta manera, puedes preservar las relaciones entre los datos y garantizar una migración precisa.
  - _**Integraciones personalizadas**_: Al desarrollar personalizaciones o integraciones específicas para tu implementación de Odoo, puedes utilizar identificadores externos para referenciar registros específicos en tus desarrollos. Esto te permite establecer relaciones y manipular datos de manera más precisa y controlada.

Nota:
- Los `id` de las vistas también son identificadores externos.
- Los identificadores externos son únicos por módulo.
- No se pueden agregar identificadores externos a registros ya creados desde la interfaz de Odoo.