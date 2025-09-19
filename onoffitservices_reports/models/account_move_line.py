from odoo import fields, models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    position = fields.Integer(readonly=True, index=True, default=False, string="Pos")