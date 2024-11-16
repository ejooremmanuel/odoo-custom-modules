# -*- coding: utf-8 -*-
{
    'name': "Support Contract",

    'summary': """
        Support Contract Management
        """,

    'description': """
      Support Contract Management
    """,

    'author': "LBA",
    'website': "http://www.lotusbetaanalytics.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services/Support Contract',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','contract_manager'],
    'application': False,
    'installable':True,
    'auto_install':True,

    # always loaded
    'data': [
         'data/schedule_action_data.xml',
        'security/support_contract_security.xml',
        'security/ir.model.access.csv',
        'views/mail_template.xml',
        'views/support_contract_view.xml',
        'views/menu.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'license': 'LGPL-3',
}
