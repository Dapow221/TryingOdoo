from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import date
from dateutil import relativedelta

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', tracking=True)
    date_of_birth = fields.Date(string='Date of Birth')
    age = fields.Integer(string='Age', 
                        compute='_compute_age', 
                        inverse='_inverse_compute_age', 
                        search='_search_age',
                        tracking=True)
    ref = fields.Char(string='Reference', tracking=True, help="Reference from patient record")
    gender = fields.Selection(string='Gender', selection=[('male', 'Male'), ('female', 'Female')], tracking=True, default='female')
    active = fields.Boolean(string='Active', default=True)
    appointment_id = fields.Many2one(comodel_name='hospital.appointment', string='Appointment')
    images = fields.Image(string="Image")
    tag_ids = fields.Many2many(comodel_name='patient.tag', string='Tags')
    appointment_count = fields.Integer(
        string="Appointments count",
        compute="_compute_appointment_count",
        store=True,
    )
    appointment_ids = fields.One2many(
        string="Appointments",
        comodel_name="hospital.appointment",
        inverse_name="patient_id"
    )
    parent = fields.Char(
        string="Parent"
    )

    marital_state = fields.Selection(
        selection=[("married", "Married"),
                   ("single", "Single")],
        string="Marital State",
        tracking=True,
    )

    partner_name = fields.Char(
        string="Partner Name",
    )

    is_birthday = fields.Boolean(
        string="Birthday ?",
        compute='_compute_is_birthdate'
    )
    # contact
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    website = fields.Char(string='Website')
    
    

    @api.depends('date_of_birth')
    def _compute_is_birthdate(self):
        for record in self:
            if record.date_of_birth:
                today = date.today()
                if record.date_of_birth.day == today.day and record.date_of_birth.month == today.month:
                    record.is_birthday = True
                else:
                    record.is_birthday = False
            else:
                record.is_birthday=False

    @api.depends('appointment_ids')
    def _compute_appointment_count(self):
        # Search count method
        for record in self:
            record.appointment_count = self.env["hospital.appointment"].search_count(
                [("patient_id", "=", record.id)])
    
    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).create(vals)
    
    def write(self, vals):
        if not self.ref and not vals.get('ref'):
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).write(vals)

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0
    
    @api.depends('age')
    def _inverse_compute_age(self):
        today = date.today()
        for rec in self:
            rec.date_of_birth = today - relativedelta.relativedelta(years=rec.age)
    
    def _search_age(self, operator, value):
        date_of_birth = date.today() - relativedelta.relativedelta(years=value)
        start_year = date_of_birth.replace(day=1, month=1)
        end_year = date_of_birth.replace(day=31, month=12)
        return [('date_of_birth', ">=", start_year), ("date_of_birth", "<=", end_year)]

    
    @api.ondelete(at_uninstall=False)
    def _check_appointments(self):
        for rec in self:
            if rec.appointment_ids:
                raise ValidationError(_("You cannot delete patient with appointment!"))
    
    def name_get(self):
        patient_list = []
        for record in self:
            name = record.ref + ' ' + record.name
            patient_list.append((record.id, name))
        
        return patient_list
        # best practice return [(record.id, "[%s] %s" % (record.ref, record.name)) for record in self]
    
    @api.constrains("date_of_birth")
    def _check_date_of_birth(self):
        for rec in self:
            if rec.date_of_birth and rec.date_of_birth > fields.Date.today():
                raise ValidationError(_("Enter Valid date!"))

    def action_button(self):
        print('clicked')
        return
    