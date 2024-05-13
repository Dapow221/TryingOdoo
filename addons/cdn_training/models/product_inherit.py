from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = 'product.product'

    product_training = fields.Selection([
        ('non_training', 'Non Produk Training'),
        ('konsumsi', 'Konsumsi Training'),
        ('training_kit', 'Peralatan Training')
    ], string='Jenis Product Training', default='non_training')



class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    product_training = fields.Selection([
        ('non_training', 'Non Produk Training'),
        ('konsumsi', 'Konsumsi Training'),
        ('training_kit', 'Peralatan Training')
    ], string='Jenis Product Training', default='non_training')



class Contact(models.Model):
    _inherit = 'res.partner'

    jenis_kel = fields.Selection(string='Jenis Kelamin', selection=[('l', 'Laki-laki'), ('p', 'Perempuan'),])
