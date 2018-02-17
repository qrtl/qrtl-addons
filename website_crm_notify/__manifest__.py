# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Website CRM Notification',
    'category': 'Website',
    'version': '10.0.1.0.0',
    'author': 'Quartile Limited',
    'website': 'https://www.quartile.co/',
    'licence': 'AGPL-3',
    'depends': ['website_crm'],
    'summary':"""""",
    'description': """
Sends notification email when contact form is submitted.
    """,
    'data': [
        'data/website_crm_notify_data.xml',
    ],
    'installable': True,
}
