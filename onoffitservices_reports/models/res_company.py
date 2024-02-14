from odoo import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    managing_director = fields.Char(string='Managing Director(s)', size=60)