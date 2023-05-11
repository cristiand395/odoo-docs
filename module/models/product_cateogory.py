from odoo import api, fields, models

class ProductCateogory(models.Model):
    _name = "product.category"
    _description = 'Product ribbon'

    name = fields.Char(string='Nombre', required=True, translate=True)
    default_code = fields.Integer(string='Default code', required=False)
    price = fields.Float(string='Price', required=False)
    is_published = fields.Boolean(string='Is published', default=False, store=True)
    product_type = fields.Selection(
        [
            ("consumable", "Consumable"),
            ("service", "Service"),
            ("product", "Product"),
        ],
        default="expense",
        required=True,
        string="Type",
    )