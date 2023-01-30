# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "syscoon Finanzinterface for Enterprise",
    "version": "15.0.0.0.2",
    "depends": [
        "account_accountant",
        "l10n_de_reports",
        "syscoon_financeinterface",
    ],
    "author": "syscoon OÜ",
    "license": "OPL-1",
    "website": "https://gitlab.syscoon.com/odoo-customer-addons/gfa-pfv",
    "summary": "Changes the main menu entry",
    "description": """Module that changes the main menu entry if enterprise is used.
                      It also removes several entries from the enterprise DATEV export that is not usable.""",
    "category": "Accounting",
    "data": [
        "views/l10n_de_report_views.xml",
        "views/syscoon_financeinterface.xml",
    ],
    "active": False,
    "installable": True,
}
