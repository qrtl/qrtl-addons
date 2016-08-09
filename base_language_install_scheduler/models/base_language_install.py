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

from openerp.osv import osv, fields
from openerp.tools.safe_eval import safe_eval


class base_language_install_scheduler(osv.osv):
    _name = "base.language.install.scheduler"
    _description = "Install Language by Scheduler"


    def lang_install_scheduler(self, cr, uid, ids=[], context=None):
        icp = self.pool.get('ir.config_parameter')
        lang = safe_eval(icp.get_param(cr, uid, 'base_language_install.default_lang', 'False')),
        if lang:
            modobj = self.pool.get('ir.module.module')
            mids = modobj.search(cr, uid, [('state', '=', 'installed')])
            context = {'overwrite': True}
            modobj.update_translations(cr, uid, mids, lang, context or {})
