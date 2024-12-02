# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    locked_positions_force = fields.Boolean(compute="_compute_locked_positions_force")

    @api.depends("state")
    def _compute_locked_positions_force(self):
        for record in self:
            record.locked_positions_force = record.state not in ["draft", "sent"]

    def _recompute_positions(self):
        self.ensure_one()
        lines = self.order_line.filtered(lambda l: not l.display_type)
        lines.sorted(key=lambda x: (x.sequence, x.id))
        for position, line in enumerate(lines, start=1):
            line.position = position

    def recompute_positions(self):
        for sale in self:
            if sale.locked_positions or sale.company_id.disable_sale_position_recompute:
                continue
            sale._recompute_positions()

    def force_recompute_positions(self):
        for sale in self:
            if sale.locked_positions_force:
                continue
            sale._recompute_positions()
