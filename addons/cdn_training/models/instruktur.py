from odoo import models, fields, api

class Instruktur(models.Model):
    _name = 'instruktur'
    _description = 'Instruktur'
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one(comodel_name='res.partner', string='Partner', required=True, ondelete='cascade')
    keahlian_ids = fields.Many2many(comodel_name='keahlian', string='Keahlian')
    jabatan_id = fields.Many2one(comodel_name='jabatan', string='Jabatan', required=True, ondelete='cascade')
    
class Keahlian(models.Model):
    _name = 'keahlian'
    _description = 'Keahlian'

    name = fields.Char(string='keahlian', required=True)

class Jabatan(models.Model):
    _name = 'jabatan'
    _description = 'Jabatan'

    name = fields.Char(string='Nama Jabatan', required=True)
    jenis_jabatan = fields.Selection(string='Jenis Jabatan', selection=[('kepala', 'Kepala / Pimpinan'),('wakil_kepala', 'Wakil Kepala Lembaga'),('staff', 'Staff')])
    keterangan = fields.Text(string='Keterangan')
    pejabat_id = fields.Many2one(comodel_name='instruktur', string='Pejabat')
    


