# -*- coding: utf-8 -*-
# from odoo import http


# class CustomSekar(http.Controller):
#     @http.route('/custom_sekar/custom_sekar/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_sekar/custom_sekar/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_sekar.listing', {
#             'root': '/custom_sekar/custom_sekar',
#             'objects': http.request.env['custom_sekar.custom_sekar'].search([]),
#         })

#     @http.route('/custom_sekar/custom_sekar/objects/<model("custom_sekar.custom_sekar"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_sekar.object', {
#             'object': obj
#         })
