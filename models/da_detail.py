from odoo import fields, models


class DaDetail(models.Model):
    _name = 'medab.da_detail'

    article  = fields.Many2one(comodel_name='product.product',string='Product',required=False)
    qte  = fields.Float(
        string='',
        required=False)
    da_id = fields.Many2one(comodel_name='medab.da',string='Product',required=False)
