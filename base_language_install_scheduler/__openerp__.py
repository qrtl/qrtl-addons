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
    'name': 'Language Install Scheduler',
    'summary': '',
    'version': '9.0.0.6.0',
    'category': 'Extra Tools',
    'description': """
* Installs and overrides translation by scheduler.
* This module is intended to be used in a demo environment whose codebase \
gets updated periodically (you want to show the latest translation).
    """,
    'author': 'Rooms For (Hong Kong) Limited T/A OSCG',
    'license': 'AGPL-3',
    'depends': ["base_setup"],
    'data': [
        'views/res_config_view.xml',
        'data/base_language_install_data.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
