# Vistas:
- Las vistas son los registros que serán visibles para los usuarios finales.
- Esta basado de XML lo cual permite ser editado independiente de los modelos.

#### Estructura básica
```xml
<record id="MODEL_view_TYPE" model="ir.ui.view">
  <field name="name">NAME</field>
  <field name="model">MODEL</field>
  <field name="arch" type="xml">
    <VIEW_TYPE>
      <VIEW_SPECIFICATIONS/>
    </VIEW_TYPE>
  </field>
</record>
```