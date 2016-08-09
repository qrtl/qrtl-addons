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

from openerp import tools
from openerp.osv import osv, fields
from openerp.tools.safe_eval import safe_eval
from openerp import api

# class base_language_install_scheduler(osv.osv):
#     _name = "base.language.install.scheduler"
#     _description = "Install Language by Scheduler"
#
#
#     _columns = {
#         'lang': fields.selection(tools.scan_languages(),'Language', required=True),
#     }
#
#
#     def lang_install_scheduler(self, cr, uid, ids=[], context=None):
#         lang_id = self.search(cr, uid, ids)[0]
#         language_rec = self.browse(cr, uid, [lang_id])[0]
#         lang = language_rec.lang
#         if lang:
#             modobj = self.pool.get('ir.module.module')
#             mids = modobj.search(cr, uid, [('state', '=', 'installed')])
#             context = {'overwrite': True}
#             modobj.update_translations(cr, uid, mids, lang, context or {})


class base_language_install_scheduler(osv.osv):
    _name = "base.language.install.scheduler"
    _description = "Install Language by Scheduler"


    # @api.model
    # def _lang_get(self):
    #     languages = self.env['res.lang'].search([])
    #     return [(language.code, language.name) for language in languages]
    #
    #
    # _columns = {
    #     'lang': fields.selection(_lang_get, 'Language', required=True),
    # }


    def lang_install_scheduler(self, cr, uid, ids=[], context=None):
        # # lang_id = self.search(cr, uid, ids)[0]
        # lang_id = self.pool.get('base.config.settings').default_lang
        # language_rec = self.browse(cr, uid, [lang_id])[0]
        # lang = language_rec.lang
        # lang = self.pool.get('base.config.settings').get_default_lang['default_lang']
        # lang = self.pool.get('base.config.settings').browse(cr, uid, [0]).get_default_lang
        icp = self.pool.get('ir.config_parameter')
        lang = safe_eval(icp.get_param(cr, uid, 'base_language_install.default_lang', 'False')),
        if lang:
            modobj = self.pool.get('ir.module.module')
            mids = modobj.search(cr, uid, [('state', '=', 'installed')])
            context = {'overwrite': True}
            modobj.update_translations(cr, uid, mids, lang, context or {})
