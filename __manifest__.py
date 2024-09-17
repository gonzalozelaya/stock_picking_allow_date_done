# -*- coding: utf-8 -*-
{
    'name': "Allow date done in stock picking",

    'summary': """
        Este modulo permite modificar la fecha efectiva en recibos y entregas de Stock""",

    'description': """
        Este modulo permite modificar la fecha efectiva en recibos y entregas de Stock
    """,

    'author': "OutsourceArg",
    'website': "http://www.outsourcearg.com",
    'installable':True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
}