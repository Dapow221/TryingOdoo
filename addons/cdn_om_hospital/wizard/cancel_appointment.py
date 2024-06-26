from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import datetime
from datetime import date
from dateutil import relativedelta

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
        cancel_days = self.env['ir.config_parameter'].get_param('cdn_om_hospital.cancel_days')
        allowed_date = self.appointment_id.booking_date - relativedelta.relativedelta(days=int(cancel_days))
        if allowed_date < date.today():
            raise ValidationError(_("Sorry"))
        self.appointment_id.state = 'cancelled'
        # auto reload page
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }
    
