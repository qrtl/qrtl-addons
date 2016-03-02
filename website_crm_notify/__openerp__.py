# -*- coding: utf-8 -*-
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2015 Rooms For (Hong Kong) Limited T/A OSCG
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

{
    'name': 'Website CRM Notification',
    'category': 'Website',
    'version': '9.0.1.0.0',
    'author': 'Rooms For (Hong Kong) Limited T/A OSCG',
    'website': 'https://www.odoo-asia.com/',
    'licence': 'AGPL-3',
    'depends': ['website_crm'],
    'summary':"""Send notification and remainder when submit contact form""",
    'description': """
Send notification and remainder when submit contact form
    """,
    'data': [
        'data/website_crm_notify_data.xml',
    ],
    'installable': True,
    'applitcation': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
