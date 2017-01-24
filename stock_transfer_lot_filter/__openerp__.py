# -*- coding: utf-8 -*-
# Copyright 2015-2017 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Lot Filtering in Stock Transfer',
    'version': '8.0.1.1.2',
    'category': 'Stock',
    'description': """
* Adds a new function field 'lot_balance' to stock.production.lot for filtering
purpose.
* Limits lot/serial number selection to ones with inventory balance larger than
zero (except for incoming picking).
     """,
    'author': 'Rooms For (Hong Kong) Limited T/A OSCG',
    'website': 'https://www.odoo-asia.com',
    'license': 'AGPL-3',
    'depends': [
        "stock",
    ],
    'data': [
        'views/stock_transfer_details.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
