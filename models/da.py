from odoo import fields, models


class Da(models.Model):
    _name = 'medab.da'

    demandeur = fields.Char()
    description = fields.Char()
    departement = fields.Char()
    data = fields.Char()
