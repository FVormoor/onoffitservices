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
    """

    env = Environment(cr, SUPERUSER_ID, {})

    # Delete old view
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

    util.if_unchanged(
        cr,
        "syscoon_partner_accounts.res_config_settings_integrate_view_form",
        util.update_record_from_xml,
    )
    logging.info("syscoon_partner_accounts.res_config_settings_integrate_view_form")
