# -*- coding: utf-8 -*-
# from odoo import http


# class Custom/contractManager(http.Controller):
#     @http.route('/custom/contract_manager/custom/contract_manager', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom/contract_manager/custom/contract_manager/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom/contract_manager.listing', {
#             'root': '/custom/contract_manager/custom/contract_manager',
#             'objects': http.request.env['custom/contract_manager.custom/contract_manager'].search([]),
#         })

#     @http.route('/custom/contract_manager/custom/contract_manager/objects/<model("custom/contract_manager.custom/contract_manager"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom/contract_manager.object', {
#             'object': obj
#         })
