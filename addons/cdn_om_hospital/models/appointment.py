from odoo import models, fields, api

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'patient_id'

    patient_id = fields.Many2one(comodel_name='hospital.patient', string='Patient')
    gender = fields.Selection(related='patient_id.gender', readonly=False)
    appointment_time = fields.Datetime(string='Appoinment Time', default=fields.Datetime.now)
    booking_date = fields.Date(string='Booking Date', default=fields.Date.context_today)
    ref = fields.Char(string='Reference', tracking=True)
    prescription = fields.Html(string='Prescription')
    priority = fields.Selection(string='Priority', selection=[('0', 'Normal'), ('1', 'Low'), ('2', 'High'), ('3', 'Very High')])
    state = fields.Selection(string='Status', selection=[('draft', 'Draft'), ('in_consultation', 'In Consultation'), ('done', 'Done'), ('cancelled', 'Cancelled')], default='draft', required=True)
    doctor_id = fields.Many2one(comodel_name='res.users', string="Doctor", tracking=True)
    pharmacy_line_ids = fields.One2many(comodel_name='appointment.pharmacy.lines', 
                                        inverse_name='appointment_id', 
                                        string='Pharmacy Line')
    hide_price = fields.Boolean(string="Hide Price")
    
    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref
    
    def button_test(self):
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'okay!!',
                'type': 'rainbow_man'
            }
        }

    def action_in_consultation(self):
        for rec in self:
            rec.state = 'in_consultation'
    
    def action_done(self):
        for rec in self:
            rec.state = 'done'
    
    def action_cancel(self):
        for rec in self:
            rec.state = 'cancelled'
    
    def action_draft(self):
        for rec in self:
            rec.state = 'draft'



class AppointmentPharmacyLines(models.Model):
    _name = 'appointment.pharmacy.lines'
    _description = 'Appointment Pharmacy Lines'

    product_id = fields.Many2one(comodel_name='product.product', string='')
    price = fields.Float(string='Price', related='product_id.list_price')
    qty = fields.Integer(string='qty', default=1)
    appointment_id = fields.Many2one(comodel_name='hospital.appointment', string='Appointment')
    
    
    

