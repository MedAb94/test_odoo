from odoo import fields, models


class Da(models.Model):
    _name = 'medab.da_detail'

    article = fields.Char()
    qte = fields.Char()

