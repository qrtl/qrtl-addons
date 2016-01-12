# -*- coding: utf-8 -*-
#    Odoo, Open Source Management Solution
#    Copyright (C) 2014 Rooms For (Hong Kong) Limited T/A OSCG
#    <https://www.odoo-asia.com>
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
    'name': 'Add Read-Only Accountant Group',
    'version': '7.0.1.0.0',
    'category': 'Accounting & Finance',
    'description': """
Overview:
===============================

* Odoo does not come with a read-only accountant group out of the box, which is inconvenient when you need to have an external accountant go through your accounting records in Odoo.  This module adds a group 'Accountant Read-Only' so it's easy to grant an external accountant access to your Odoo system.
* This group inherits the group 'Employee', thus minimum level of create/write/delete rights will be granted for some non-accounting related models. 
    """,
    'author': 'Rooms For (Hong Kong) Limited T/A OSCG',
    'website': 'https://www.odoo-asia.com',
    'license': 'AGPL-3',
    'depends': ['account_accountant'],
    'data': [
        'security/account_security.xml',
        'security/ir.model.access.csv',
        ],
    'installable': True,
    'application': False,
    'auto_install': False, 
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: