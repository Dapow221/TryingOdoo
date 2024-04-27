# -*- coding: utf-8 -*-
# from odoo import http


# class CdnOmHospital(http.Controller):
#     @http.route('/cdn_om_hospital/cdn_om_hospital', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cdn_om_hospital/cdn_om_hospital/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cdn_om_hospital.listing', {
#             'root': '/cdn_om_hospital/cdn_om_hospital',
#             'objects': http.request.env['cdn_om_hospital.cdn_om_hospital'].search([]),
#         })

#     @http.route('/cdn_om_hospital/cdn_om_hospital/objects/<model("cdn_om_hospital.cdn_om_hospital"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cdn_om_hospital.object', {
#             'object': obj
#         })
