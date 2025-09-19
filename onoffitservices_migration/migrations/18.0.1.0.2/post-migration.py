import logging
from odoo import SUPERUSER_ID
from odoo.api import Environment
from odoo.upgrade import util

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    """
    Migration script performs the below:
    1. Deletes old view with external id
       syscoon_partner_accounts.res_config_settings_integrate_view_form
    2. Resets view syscoon_partner_accounts.res_config_settings_integrate_view_form
    3. Deletes old view with name 'onoff:report_saleorder_document'
    """
    env = Environment(cr, SUPERUSER_ID, {})

    # Delete old view by external ID
    view_old = env.ref(
        "syscoon_partner_accounts.res_config_settings_integrate_view_form"
    )
    if view_old:
        view_old.unlink()
        _logger.info(f"Deleted old view id: {view_old.id}")
    else:
        _logger.info(
            "No active view found with key "
            "syscoon_partner_accounts.res_config_settings_integrate_view_form"
        )

    # Delete old view by name
    view_by_name = env['ir.ui.view'].search([
        ('name', '=', 'onoff:report_saleorder_document')
    ])

    if view_by_name:
        _logger.info(f"Found {len(view_by_name)} view(s) with name 'onoff:report_saleorder_document'")
        for view in view_by_name:
            _logger.info(f"Deleting view id: {view.id}")
            view.unlink()
        _logger.info("Deleted all views with name 'onoff:report_saleorder_document'")
    else:
        _logger.info("No view found with name 'onoff:report_saleorder_document'")

    util.if_unchanged(
        cr,
        "syscoon_partner_accounts.res_config_settings_integrate_view_form",
        util.update_record_from_xml,
    )
    _logger.info("syscoon_partner_accounts.res_config_settings_integrate_view_form")