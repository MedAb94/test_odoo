from odoo import fields, models


class Da(models.Model):
    _name = 'medab.da'

    name = fields.Char(string='Ref', required=True)

    demandeur = fields.Many2one(comodel_name='res.users', string='Demandeur', required=False)

    description = fields.Text()

    note = fields.Text()

    status = fields.Boolean(string="Statut", default=False)

    departement = fields.Many2one(comodel_name='hr.department', string='Departement', required=False,
                                  retaled='demandeur.department_id')

    date = fields.Date(string='Date', required=False)

    da_ids = fields.One2many(
        comodel_name='medab.da_detail',
        inverse_name='da_id',
        string='Details',
        required=False)

    def validate_da(self):
        self.status = True
