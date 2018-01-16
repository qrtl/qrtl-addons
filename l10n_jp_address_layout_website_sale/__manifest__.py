# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Japan Address Layout in E-commerce',
    'version': '11.0.1.0.0',
    'author': 'Quartile Limited',
    'website': 'https://www.odoo-asia.com',
    'category': 'Extra Tools',
    'license': "AGPL-3",
    'description': """
This module provides the Japan address input field layout in E-commerce.
    """,
    'summary': "",
    'depends': [
        'portal',
        'website_sale',
    ],
    'data': [
        'views/templates.xml',
    ],
    'installable': True,
}
