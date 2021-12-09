# -*- coding: utf-8 -*-
#    Odoo, Open Source Management Solution
#    Copyright (C) 2016 Rooms For (Hong Kong) Limited T/A OSCG
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
    'name': 'MRP BOM Line Reference',
    'summary': '',
    'version': '9.0.0.5.0',
    'category': 'Manufacturing',
    'description': """
* Adds `Reference` field in BOM line (expected to be used to keep mapping reference for parts in circuit diagram).
    """,
    'author': 'Rooms For (Hong Kong) Limited T/A OSCG',
    'license': 'AGPL-3',
    'depends': ["mrp"],
    'data': [
        'mrp_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
