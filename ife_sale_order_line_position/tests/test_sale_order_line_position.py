# -*- coding: utf-8 -*-
from odoo.addons.sale_order_line_position.tests.test_sale_order_line_position import TestSaleOrderLinePosition

class TestSaleOrderLinePositionExtended(TestSaleOrderLinePosition):
    def test_force_recompute_position_sent(self):
        """Check that when order is sent, force recomputes positions."""
        new_line = self.env["sale.order.line"].create(
            [
                {
                    "order_id": self.order.id,
                    "product_id": self.product.id,
                    "product_uom": self.product.uom_id.id,
                    "product_uom_qty": 15.0,
                }
            ]
        )
        self.assertEqual(new_line.position, 3)
        self.order.state = "sent"
        self.order.order_line[0].unlink()
        self.order.force_recompute_positions()
        self.assertEqual(new_line.position, 2)

    def test_force_recompute_position_sale(self):
        """Check that when order is sent, position are not recomputed."""
        new_line = self.env["sale.order.line"].create(
            [
                {
                    "order_id": self.order.id,
                    "product_id": self.product.id,
                    "product_uom": self.product.uom_id.id,
                    "product_uom_qty": 15.0,
                }
            ]
        )
        self.assertEqual(new_line.position, 3)
        self.order.state = "sent"
        self.order.order_line[0].unlink()
        self.order.action_confirm()
        self.order.force_recompute_positions()
        self.assertEqual(new_line.position, 3)
