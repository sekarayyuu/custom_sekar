# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
import csv
import base64
import io


class sale_order(models.Model):
    _inherit = "sale.order"

    request_vendor = fields.Many2one(string="Request Vendor", comodel_name="res.partner")
    purchase_order_ids = fields.One2many('purchase.order', 'sale_order', string="Purchase Orders")
    no_kontrak = fields.Char(string="No Kontrak")
    with_purchase_order = fields.Boolean(string="With PO", default=False)
    excel_file = fields.Binary(string='Excel File')


    def action_confirm(self):
        for order in self:
            # Cek apakah No Kontrak sudah pernah diinputkan sebelumnya
            if order.no_kontrak and self.env['sale.order'].search([('no_kontrak', '=', order.no_kontrak), ('id', '!=', order.id)]):
                raise exceptions.UserError("No Kontrak sudah pernah diinputkan sebelumnya...!")
        # Jika No Kontrak belum pernah diinputkan sebelumnya, proses confirm akan berlanjut
        return super(sale_order, self).action_confirm()


    def action_create_po(self):
        PurchaseOrderLine = self.env['purchase.order.line']
        for order in self:
            po_vals = {
                'partner_id': order.request_vendor.id,
                'partner_ref': order.name,
            }
            po = self.env['purchase.order'].create(po_vals)
            for line in order.order_line:
                po_line_vals = {
                    'order_id': po.id,
                    'product_id': line.product_id.id,
                    'name': line.name or line.product_id.name,
                    'product_qty': line.product_qty,
                    'price_unit': line.price_unit,
                    'product_uom': line.product_uom.id
                }
                PurchaseOrderLine.create(po_line_vals)

        return True


    def update_purchase_order_ids(self):
        if self.request_vendor:
            purchase_orders = self.search([('request_vendor', '=', self.request_vendor.id)])
            self.purchase_order_ids = purchase_orders


    def open_import_so_lines_wizard(self):
            return {
                'name': 'Import Sale Order Lines',
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'res_model': 'import.so.lines.wizard',
                'target': 'new',
            }

    def export_sale_order_lines_to_excel(self):
        headers = ['Product', 'Qty', 'Unit Price']
        lines = self.order_line
        data = io.StringIO()
        writer = csv.writer(data)
        writer.writerow(headers)
        for line in lines:
            writer.writerow([line.product_id.name, line.product_uom_qty, line.price_unit])
        data.seek(0)
        binary_data = base64.b64encode(data.getvalue().encode())
        self.write({'excel_file': binary_data})

        excel_file = fields.Binary(string='Excel File')

