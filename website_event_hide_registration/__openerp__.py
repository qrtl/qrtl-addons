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
    'name': 'Website Event Hide Registration',
    'summary': '',
    'version': '9.0.0.5.0',
    'category': 'Website',
    'description': """
* Adds a boolean field 'Show Registration' in event model.
* Show/hide registration section in the event screen on website depending on 'Show Registration' field value.
* Note: this module does not work with `event_sale` (intalling `event_sale` will negate the function of this module).
    """,
    'author': 'Rooms For (Hong Kong) Limited T/A OSCG',
    'website': 'https://www.odoo-asia.com',
    'license': 'AGPL-3',
    'depends': ["website_event"],
    'data': [
        'views/event_view.xml',
        'views/website_event.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
