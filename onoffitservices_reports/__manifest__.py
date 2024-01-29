{
    'name': 'OnOffItservices Reports',
    'version': '16.0.1.0.0',
    'author': 'Hucke Media GmbH & Co. KG/IFE GmbH',
    'category': 'Customizations/Custom',
    'website': 'https://www.hucke-media.de/',
    'license': 'AGPL-3',
    'summary': 'Reports Customizations for OnOffItServices',
    'depends': [
        'l10n_din5008',
    ],
    'data': [
        'report/l10n_din5008_template.xml',
        'views/res_company_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}