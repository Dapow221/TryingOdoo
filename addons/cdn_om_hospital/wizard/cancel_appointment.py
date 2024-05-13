from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import datetime

class CancelAppointmentWizard(models.TransientModel):
    _name = 'cancel.appointment.wizard'
    _description = 'Cancel Appointment Wizard'

    @api.model
    def default_get(self, fields):
        res = super(CancelAppointmentWizard, self).default_get(fields)
        res['cancel_date'] = datetime.date.today()
        if self.env.context.get('active_id'):
            res['appointment_id'] = self.env.context.get('active_id')
        return res 

    appointment_id = fields.Many2one(comodel_name='hospital.appointment', string='Appointment', domain=[('state', '=', 'draft')])
    reason = fields.Text(string="Reason")
    cancel_date = fields.Date(string="Cancellation Date")

    def action_cancel(self):
        if self.appointment_id.booking_date == fields.Date.today():
            raise ValidationError(_("Sorry"))
        return 
    
