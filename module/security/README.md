# Security
- Basado en la estructura de [datos](../data/README.md) que acepta Odoo.
- Es obligatorio su definición, si no, Odoo asume que ningún usuario tiene acceso a este modulo.
- Este archivo suele llamarse `ir.model.access.csv`.
- Actualizar el modulo cuando se actualicen los permisos.

Ejemplo:
```csv
id,name,model_id/id,group_id/id,perm_read,perm_write,perm_create,perm_unlink
access_test_model,access_test_model,model_test_model,base.group_user,1,0,0,0
``` 

| id | name | model_id:id | group_id | read | write | create | unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| access_test_model | access_test_model | model_test_model | base.group_user | 1 | 0 | 0 | 0 |
| Identificador externo | Nombre del `ir.model.access` | model_<model_name> | grupo de acceso | Leer | Actualizar | Crear | Eliminar |  