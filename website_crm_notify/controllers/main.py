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

import openerp
from openerp import SUPERUSER_ID

class WebsiteForm(openerp.addons.website_form.controllers.main.WebsiteForm):

    def insert_record(self, request, model, values, custom, meta=None):
        record_id = super(WebsiteForm, self).insert_record(request, model, values, custom, meta)

        cr, context = request.cr, request.context
        local_context = context.copy()
        template_id = request.registry['ir.model.data'].get_object_reference(cr, SUPERUSER_ID, 'website_crm_notify', 'website_crm_notify_mail')[1]
        mail_id = request.registry['mail.template'].send_mail(cr, SUPERUSER_ID, template_id, int(record_id), context=local_context, force_send=True)

        return record_id

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
