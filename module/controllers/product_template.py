from odoo import http
from odoo.http import request

class CustomController(http.Controller):

    @http.route(['/products/<model("product.template"):template_id>'], type='json', auth="public", methods=['POST'], website=True)
    def get_product_data(self, product_id, **kw):
        product = request.env["product.category"].search([("id","=",product_id)])
        res = {
            "product": product 
        }
        return http.request.render('module_folder.template_id', res)
