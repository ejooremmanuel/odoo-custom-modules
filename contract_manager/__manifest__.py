# -*- coding: utf-8 -*-
{
    'name': "Contract Manager",

    'summary': """
        Contract Management
        """,

    'description': """
        Contract Management
    """,

    'author': "LBA",
    'website': "http://www.lotusbetaanalytics.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services/Contract Manager',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],
    'application': True,

    # always loaded
    'data': [
        'security/support_contract_security.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'license': 'LGPL-3',
}
