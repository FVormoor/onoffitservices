from odoo import models, fields, _
from odoo.tools import format_date


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    position = fields.Integer(
        readonly=True, 
        index=True, 
        default=False,
        string="Pos"
    )