from odoo import models, fields

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    sale_order = fields.Many2one('sale.order', string="Sale Order")