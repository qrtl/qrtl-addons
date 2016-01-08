# -*- coding: utf-8 -*-
#    Odoo, Open Source Management Solution
#    Copyright (C) 2015 Rooms For (Hong Kong) Limited T/A OSCG
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
    'name': 'POS Receipt Product Name',
    'version': '8.0.1.0.0',
    'category': 'Point of Sale',
    'description': """
* Add a field called 'POS Product Name' to keep the product names presentable on POS receipt printed through PosBox. (As of 26 Oct 2014, PosBox does not handle double-byte Japanese characters)
* This module only handles the part that adds a field in product; receipt design is updated separately
    """,
    'author': 'Rooms For (Hong Kong) Limited T/A OSCG',
    'website': 'https://www.odoo-asia.com',
    'license': 'AGPL-3',
    'depends': [
        "point_of_sale",
    ],
    'data': [
        'product.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False, 
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
