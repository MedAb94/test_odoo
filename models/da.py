from odoo import fields, models
import dateutil.parser
import datetime


class Da(models.Model):
    _name = 'medab.da'

    name = fields.Char(string='Ref', required=True)

    demandeur = fields.Many2one(comodel_name='res.users', string='Demandeur', required=False)

    fournisseur = fields.Many2one(comodel_name='res.partner', string='Fournisseur', required=True)

    description = fields.Text()

    note = fields.Text()

    status = fields.Boolean(string="Statut", default=False)

    status_char = fields.Char(string="Statut", default="En attente")

    departement = fields.Many2one(comodel_name='hr.department', string='Departement', required=False,
                                  retaled='demandeur.department_id')

    date = fields.Date(string='Date', required=False)

    da_ids = fields.One2many(
        comodel_name='medab.da_detail',
        inverse_name='da_id',
        string='Details',
        required=False)

    def validate_da_and_create_devis(self):
        self.status = True
        self.status_char = "Validée"

        vals = {
            'origin': self.name,
            'date_order': self.date,
            'partner_id': self.fournisseur.id,
            'state': 'purchase',
            'invoice_status': 'to invoice',
            # 'date_approve': dateutil.parser.parse(self.date).date(),
        }
        res = self.env['purchase.order'].create(vals)
        if res:
            for rec in self.da_ids:
                vals2 = {
                    'name': self.name,
                    'product_qty': rec.qte,
                    'product_id': rec.article.id,
                    'product_uom': rec.article.uom_id.id,
                    'price_unit': 0,
                    'price_subtotal': 0,
                    'price_total': 0,
                    # 'price_tax':0,
                    'order_id': self.id,
                    'partner_id': self.fournisseur.id,
                    #'date_planned': rec.operation_date,
                    #'qty_received': rec.net_weight
                }
                res2 = self.env['purchase.order.line'].create(vals2)
                print(res2)

