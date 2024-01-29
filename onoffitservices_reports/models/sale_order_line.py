from odoo import models, fields, _
from odoo.tools import format_date


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'


    def _prepare_invoice_line(self, **optional_values):
        res = super(SaleOrderLine, self)._prepare_invoice_line(**optional_values)
        res['position'] = self.position
        return res
