from odoo import models, fields, api, _

class PatientTag(models.Model):
    _name = 'patient.tag'
    _description = 'Patient Tag'

    name = fields.Char(string="Name", required=True)
    active = fields.Boolean(string="Active", default=True)
    color = fields.Integer(string="Color")
    sequence= fields.Integer(default=1)

    _sql_constraints = [
        ("unique_tag_name","unique(name)","Tag name must be unique!"),
        ("check_sequence","check(sequence > 0)","Sequence must be greater than zero!")
        ]

    @api.returns('self',lambda value:value.id)
    def copy(self, default=None):
        if default is None:
            default={}
        default['name']=_("%s (copy)",self.name)
        default['sequence']=10 
        return super(PatientTag,self).copy(default)
