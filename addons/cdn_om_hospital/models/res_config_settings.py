from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    cancel_days = fields.Integer(string='Cancel Days', config_parameter='cdn_om_hospital.cancel_days')
    