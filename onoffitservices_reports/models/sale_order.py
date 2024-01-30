from odoo import models, fields, _
from odoo.tools import format_date


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _compute_l10n_din5008_addresses(self):
        for record in self:
            record.l10n_din5008_addresses = data = []
            if record.partner_shipping_id == record.partner_invoice_id:
                data.append((_("Invoicing and Shipping Address:"), record.partner_shipping_id))
            else:
                data.append((_("Shipping Address:"), record.partner_shipping_id))
                data.append((_("Invoicing Address:"), record.partner_invoice_id, record.partner_id.vat))
    

    def recompute_positions(self):
        for sale in self:
            #if sale.locked_positions or sale.company_id.disable_sale_position_recompute:
                #continue
            lines = sale.order_line.filtered(lambda l: not l.display_type)
            lines.sorted(key=lambda x: (x.sequence, x.id))
            for position, line in enumerate(lines, start=1):
                line.position = position