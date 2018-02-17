# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import odoo


class WebsiteForm(odoo.addons.website_form.controllers.main.WebsiteForm):

    def insert_record(self, request, model, values, custom, meta=None):
        record_id = super(WebsiteForm, self).insert_record(
            request, model, values, custom, meta)

        if model.model == 'crm.lead':
            template = request.env.ref(
                'website_crm_notify.website_crm_notify_mail', False)
            if template:
                mail_id = template.sudo().send_mail(record_id, force_send=True)

        return record_id
