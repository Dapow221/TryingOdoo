from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "sequence"
    _order = "id desc"

    patient_id = fields.Many2one(comodel_name='hospital.patient', string='Patient', ondelete="restrict")
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
    sequence = fields.Char()
    operation_id = fields.Many2one(comodel_name='hospital.operation', string='Operation', tracking=True)
    progress = fields.Integer(string="Progress", compute='_compute_progress')
    duration = fields.Float(string="Duration")
    
    
    @api.model
    def create(self, values):
        result = super(HospitalAppointment, self)
        values["sequence"] = self.env["ir.sequence"].next_by_code(
            "hospital.appointment")
        return result.create(values)

    def write(self, values):
        res = super(HospitalAppointment, self)
        if not self.sequence:
            values["sequence"] = self.env["ir.sequence"].next_by_code(
                "hospital.appointment")
        return res.write(values)
        
    def unlink(self):
        for rec in self:
            if rec.state != 'draft':
                raise ValidationError(_("Can only delete selain drafted Records"))
        return super(HospitalAppointment, self).unlink()

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
            if rec.state == 'draft':
                rec.state = 'in_consultation'
    
    def action_done(self):
        for rec in self:
            rec.state = 'done'
    
    def action_cancel(self):
        action = self.env.ref('cdn_om_hospital.cancel_appointment_wizard_action').read()[0]
        return action
    
    def action_draft(self):
        for rec in self:
            rec.state = 'draft'
    
    @api.depends('state')
    def _compute_progress(self):
        for rec in self:
            progress = 0
            if rec.state == 'draft':
                progress = 33
            elif rec.state == 'in_consultation':
                progress = 66
            elif rec.state == 'done':
                progress = 100
            rec.progress = progress


class AppointmentPharmacyLines(models.Model):
    _name = 'appointment.pharmacy.lines'
    _description = 'Appointment Pharmacy Lines'

    product_id = fields.Many2one(comodel_name='product.product', string='')
    price = fields.Float(string='Price', related='product_id.list_price')
    qty = fields.Integer(string='qty', default=1)
    appointment_id = fields.Many2one(comodel_name='hospital.appointment', string='Appointment')
    
    
    

