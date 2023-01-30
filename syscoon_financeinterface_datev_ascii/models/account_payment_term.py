# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class AccountPaymentTerm(models.Model):
    _inherit = "account.payment.term"

    datev_payment_conditons_id = fields.Integer("DATEV Payment Term ID")
