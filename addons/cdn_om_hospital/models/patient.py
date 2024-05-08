from odoo import models, fields, api
from datetime import date

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', tracking=True)
    date_of_birth = fields.Date(string='Date of Birth')
    age = fields.Integer(string='Age', compute='_compute_age')
    ref = fields.Char(string='Reference', tracking=True, help="Reference from patient record")
    gender = fields.Selection(string='Gender', selection=[('male', 'Male'), ('female', 'Female')], tracking=True, default='female')
    active = fields.Boolean(string='Active', default=True)
    appointment_id = fields.Many2one(comodel_name='hospital.appointment', string='Appointment')
    
    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0
    