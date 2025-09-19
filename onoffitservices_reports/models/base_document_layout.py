from odoo import fields, models


class BaseDocumentLayout(models.TransientModel):
    _inherit = "base.document.layout"

    managing_director = fields.Char(
        related="company_id.managing_director", readonly=True
    )