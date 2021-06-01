# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Medab',
    'version': '1.0',
    'category': 'Sales',
    'description': "Just for testing",
    'depends': ['purchase'],
    'data': [
            'security/security.xml',
            'security/ir.model.access.csv',
            'views/menu.xml',
            'views/da.xml',
             ],
    'website': 'https://www.odoo.com/page/community-builder',
}
